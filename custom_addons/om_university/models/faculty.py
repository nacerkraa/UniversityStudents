from odoo import api, fields, models

class UniversityTransfer(models.Model):
    _name = 'university.faculty'
    _description = 'University Faculty'

    ref = fields.Char(string="Ref")
    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    univ_id = fields.Many2one('university.univ', string="University")



