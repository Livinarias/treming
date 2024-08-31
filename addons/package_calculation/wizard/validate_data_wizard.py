from odoo import fields, models


class ValidateDataWizard(models.TransientModel):
    _name = "validate.data.wizard"
    _description = "validate data wizard"

    partner_name = fields.Char(string="User name", readonly=True)
    partner_street = fields.Text(string="street name", readonly=True)
    country_id = fields.Many2one("res.country", string="User city", readonly=True)
    vat_type = fields.Many2one(
        "l10n_latam.identification.type",
        string="Type of VAT",
        readonly=True,
    )
    partner_vat = fields.Char(string="VAT Number", readonly=True)
    package_calculation_id = fields.Many2one("package.calculation", readonly=True)

    def action_confirm(self):
        partner = self.env["res.partner"].create(
            {
                "name": self.partner_name,
                "street": self.partner_street,
                "country_id": self.country_id.id,
                "vat": self.partner_vat,
                "l10n_latam_identification_type_id": self.vat_type.id,
                "company_type": "person",
            }
        )
        self.package_calculation_id.write({"partner_id": partner, "state": "done"})
