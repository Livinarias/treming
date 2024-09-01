from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    geo_db_api_key = fields.Char("GeoDB API Key")
    url_countries = fields.Char("URL API Countries")
    url_timezone = fields.Char("URL API TimeZone")

    @api.model
    def get_values(self):
        res = super().get_values()
        res.update(
            geo_db_api_key=self.env["ir.config_parameter"]
            .sudo()
            .get_param("geo_db_api_key"),
            url_countries=self.env["ir.config_parameter"]
            .sudo()
            .get_param("url_countries"),
            url_timezone=self.env["ir.config_parameter"]
            .sudo()
            .get_param("url_timezone"),
        )
        return res

    def set_values(self):
        res = super().set_values()
        self.env["ir.config_parameter"].sudo().set_param(
            "geo_db_api_key", self.geo_db_api_key
        )
        self.env["ir.config_parameter"].sudo().set_param(
            "url_countries", self.url_countries
        )
        self.env["ir.config_parameter"].sudo().set_param(
            "url_timezone", self.url_timezone
        )
        return res
