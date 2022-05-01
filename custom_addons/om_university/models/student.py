from  datetime import date
from odoo import api, fields, models
class UniversityStudent(models.Model):
    _name = 'university.student'
    _description = 'University Student'
    _rec_name = 'ref'




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
    type_transfer = fields.Char(string="type", compute='_cumpute_transfer')
    active = fields.Boolean(string="Active", default=True)

    state = fields.Selection([('draft', 'Draft'),
                                ('under_review', 'Under Review'),
                                ('accepted', 'Accepted'),
                                ('refused', 'Refused')], default='draft', string='Status', required=True)



    @api.depends('establish_date')
    def _cumpute_years(self):
        for rec in self:
            today = date.today()
            if rec.establish_date:
                rec.age = today.year - rec.establish_date.year
            else:
                rec.age = 0


    @api.depends('univ_id')
    def _cumpute_transfer(self):
        for rec in self:
            if rec.univ_id.name == 'Université abdelhamid mehri constantine 2':
                rec.type_transfer = 'Interne'
            else:
                rec.type_transfer = 'Extarne'

    def action_test(self):
        print("Button Clicked!!!!!!!!!!!!!!!!!!!!!!!!!")
