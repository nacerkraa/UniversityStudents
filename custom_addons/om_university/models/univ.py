from odoo import api, fields, models

class univs(models.Model):
    _name = 'university.univ'
    _description = 'University'

    ref = fields.Char(string="Ref")
    name = fields.Char(string="Name")
    email = fields.Char(string="Email")