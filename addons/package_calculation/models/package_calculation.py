from odoo import api, fields, models


class PackageCalculation(models.Model):
    _name = "package.calculation"
    _description = "this module create a package calculation records"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = "partner_name"

    partner_name = fields.Char(string="User name", required=True, tracking=True)
    partner_street = fields.Text(string="street name", required=True, tracking=True)
    partner_city = fields.Many2one(
        "res.country", string="User city", required=True, tracking=True
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
        [("draft", "Draft"), ("done", "Done"), ("cancel", "Cancel")],
        default="draft",
        tracking=True,
    )
    package_ids = fields.Many2many("product.product", string="Packages Selected")
    delivery_cost = fields.Float(string="Costo de Envío", readonly=True, tracking=True)
    currency_id = fields.Many2one(
        "res.currency",
        readonly=True,
    )
    delivery_time = fields.Char(
        string="Tiempo de Entrega", readonly=True, tracking=True
    )
    duration = fields.Char(
        readonly=True,
    )

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

    def action_validate_data(self):
        for rec in self:
            rec.state = "done"

    def action_cancel(self):
        for rec in self:
            rec.state = "cancel"
