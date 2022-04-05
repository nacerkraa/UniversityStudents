from odoo import api, fields, models

class UniversityStudent(models.Model):
    _name = 'university.student'
    _description = 'University Student'

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    email = fields.Char(string="Email")
    phone = fields.Integer(string="¨Phone")
    faculty = fields.Selection([('ntic', 'Faculté de Nouvelles technologies'), ('eco', 'Faculté des sciences économiques')], string="Gender")

