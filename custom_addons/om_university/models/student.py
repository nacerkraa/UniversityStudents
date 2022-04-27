from odoo import api, fields, models

class UniversityStudent(models.Model):
    _name = 'university.student'
    _description = 'University Student'




    ref = fields.Char(string="Ref")
    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    email = fields.Char(string="Email")
    phone = fields.Char(string="¨Phone")
    faculty_id = fields.Many2one('university.faculty', string="Faculty")
    rate = fields.Float(string="Rate")
    establish_date = fields.Datetime(string="Establish Date", default=fields.Datetime.now)
    active = fields.Boolean(string="Active", default=True)
