from odoo import models, fields, api

class ConfigNovici(models.Model):
    _name = 'config.novici'
    _description = 'Config Novici'

    name = fields.Char(string='Name', readonly=True, default='Default Config Novici')
    is_active = fields.Boolean(string='Active', default=True)

