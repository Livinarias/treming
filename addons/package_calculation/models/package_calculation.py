from odoo import fields, models


class PackageCalculation(models.Model):
    _name = "package.calculation"
    _description = "this module create a package calculation records"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = "partner_name"

    partner_name = fields.Char(string="User name", required=True)
    partner_street = fields.Text(string="street name", required=True)
    partner_city = fields.Many2one("res.country", string="User city", required=True)
    company_id = fields.Many2one(
        comodel_name="res.company",
        required=True,
        index=True,
        default=lambda self: self.env.company,
    )
