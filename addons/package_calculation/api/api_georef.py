import logging

import requests

from odoo import models


class ApiGeorefTemplate(models.AbstractModel):
    _name = "api.georef.template"
    _description = "Api georef Template"

    def get_countries(self, headers=None, params=None, url=""):
        try:
            response = requests.get(url, headers=headers, params=params, timeout=10)
            if response.status_code == 200:
                return response.json()
            logging.info(response.json())
        except requests.exceptions.HTTPError as errh:
            logging.error(errh.message)

    def get_time_zone(self, headers=None, url=""):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                return response.json()
            logging.info(response.json())
        except requests.exceptions.HTTPError as errh:
            logging.error(errh.message)
