import datetime

import pytz

from odoo import api, fields, models


class PackageCalculation(models.Model):
    _name = "package.calculation"
    _description = "this module create a package calculation records"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = "partner_name"

    _headers = {"X-RapidAPI-Key": "", "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"}

    partner_name = fields.Char(string="User name", required=True, tracking=True)
    partner_street = fields.Text(string="street name", required=True, tracking=True)
    country_id = fields.Many2one(
        "res.country", string="User Country", required=True, tracking=True
    )
    vat_type = fields.Many2one(
        "l10n_latam.identification.type",
        string="Type of VAT",
        required=True,
        tracking=True,
    )
    partner_vat = fields.Char(string="VAT Number", required=True, tracking=True)
    company_id = fields.Many2one(
        "res.company",
        required=True,
        index=True,
        default=lambda self: self.env.company,
    )
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("done", "Done"),
            ("cancel", "Cancel"),
            ("wait", "Wait for Localization"),
        ],
        default="draft",
        tracking=True,
    )
    packages_ids = fields.Many2many("product.product", string="Packages Selected")
    cost_product_id = fields.Many2one(
        "product.product",
        string="Cost Product",
        required=True,
    )

    delivery_cost = fields.Float(readonly=True, tracking=True)
    currency_id = fields.Many2one(
        "res.currency",
        readonly=True,
    )
    delivery_time = fields.Datetime(
        string="Delivery Date", readonly=True, tracking=True
    )
    partner_id = fields.Many2one("res.partner", string="Partner")

    _sql_constraints = [("partner_vat_uniq", "unique(partner_vat)", "Vat must unique.")]

    # Functions

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            company = self.env["res.company"].browse(self.env.company.id)
            vals["currency_id"] = company.currency_id.id
        return super().create(vals_list)

    # Buttons
    def action_draft(self):
        for rec in self:
            rec.state = "draft"

    def action_cancel(self):
        for rec in self:
            rec.state = "cancel"

    def open_wizard(self):
        if not self.partner_id:
            return {
                "name": "Open Wizard Package",
                "type": "ir.actions.act_window",
                "res_model": "validate.data.wizard",
                "view_mode": "form",
                "view_id": self.env.ref(
                    "package_calculation.view_validate_data_wizard_form"
                ).id,
                "target": "new",
                "context": {
                    "default_partner_name": self.partner_name,
                    "default_partner_street": self.partner_street,
                    "default_country_id": self.country_id.id,
                    "default_vat_type": self.vat_type.id,
                    "default_partner_vat": self.partner_vat,
                    "default_package_calculation_id": self.id,
                },
            }
        self.state = "wait"

    def action_wait(self):
        self.calc_differece_timezone()
        order_line = [
            (0, 0, {"product_id": line.id, "product_uom_qty": 1})
            for line in self.packages_ids
        ]
        order_line.append(
            (
                0,
                0,
                {
                    "product_id": self.cost_product_id.id,
                    "product_uom_qty": 1,
                    "price_unit": self.delivery_cost,
                },
            )
        )
        self.env["sale.order"].create(
            {
                "partner_id": self.partner_id.id,
                "company_id": self.company_id.id,
                "currency_id": self.currency_id.id,
                "partner_shipping_id": self.partner_id.id,
                "partner_invoice_id": self.partner_id.id,
                "commitment_date": self.delivery_time,
                "order_line": order_line,
                "note": "Created from package calculation",
            }
        )
        self.state = "done"

    def consume_api_countries(self, headers):
        url_countries = (
            self.env["ir.config_parameter"].sudo().get_param("url_countries")
        )
        params = {"countryIds": self.country_id.code}
        return self.env["api.georef.template"].get_countries(
            headers, params, url_countries
        )

    def consume_api_timezone(self):
        api_key = self.env["ir.config_parameter"].sudo().get_param("geo_db_api_key")
        headers = self._headers.copy()
        headers["X-RapidAPI-Key"] = api_key
        country_data = self.consume_api_countries(headers)
        data_id = country_data["data"][0].get("wikiDataId", "")
        url_timezone = self.env["ir.config_parameter"].sudo().get_param("url_timezone")
        url_timezone = f"{url_timezone}/{data_id}/dateTime"
        return self.env["api.georef.template"].get_time_zone(headers, url_timezone)

    def calc_differece_timezone(self):
        country_time = self.consume_api_timezone()["data"]
        country_time_formatted = country_time[:26] + country_time[-6:]
        country_time = datetime.datetime.fromisoformat(
            country_time_formatted.replace("T", " ")
        )
        local_time = country_time.astimezone(pytz.timezone(self.env.user.tz))
        differece_timezone = country_time - local_time
        hours, _ = divmod(differece_timezone.seconds, 3600)
        self.delivery_time = fields.Datetime.now() + datetime.timedelta(
            days=1, hours=hours
        )
        self.delivery_cost = 10 if hours > 4 else 0
