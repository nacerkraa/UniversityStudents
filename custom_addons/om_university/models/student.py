from  datetime import date
from odoo import api, fields, models
class UniversityStudent(models.Model):
    _name = 'university.student'
    _description = 'University Student'




    ref = fields.Char(string="Ref")
    name = fields.Char(string="Name")
    age = fields.Integer(string="Age", compute='_cumpute_years')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    email = fields.Char(string="Email")
    phone = fields.Char(string="¨Phone")
    univ_id = fields.Many2one('university.univ', string="University")
    faculty_id = fields.Many2one('university.faculty', string="Faculty")
    rate = fields.Float(string="Rate")
    establish_date = fields.Date(string="Establish Date")
    type_transfer = fields.Char(string="type")
    active = fields.Boolean(string="Active", default=True)

    @api.depends('establish_date')
    def _cumpute_years(self):
        for rec in self:
            today = date.today()
            if rec.establish_date:
                rec.age = today.year - rec.establish_date.year
            else:
                rec.age = 0

    # @api.depends('univ_id')
    # def _cumpute_transfer(self):
    #     for rec in self:
    #         if rec.univ_id  == 'constantine2':
    #             rec.type_transfer  = 'intarne'
    #         else:
    #             rec.type_transfer  = 'extarne'
