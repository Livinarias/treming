from random import randint

from odoo import fields, models


class PackageProduct(models.Model):
    _inherit = "product.product"

    def _get_default_color(self):
        return randint(1, 11)

    color = fields.Integer(default=_get_default_color)
