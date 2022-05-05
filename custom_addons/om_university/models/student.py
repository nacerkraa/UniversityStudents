from  datetime import date
from odoo import api, fields, models
class UniversityStudent(models.Model):
    _name = 'university.student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'University Student'
    _rec_name = 'ref'




    # gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    ref = fields.Char(string="Ref")
    name = fields.Char(string="Name")
    age = fields.Integer(string="Age", compute='_cumpute_years')
    email = fields.Char(string="Email")
    phone = fields.Char(string="¨Phone")
    current_university = fields.Char(string="University")
    current_faculty = fields.Char(string="University")
    rate = fields.Float(string="Rate")
    establish_date = fields.Date(string="Establish Date")
    type_transfer = fields.Char(string="type", compute='_cumpute_transfer')
    comment = fields.Html(string="comment")
    active = fields.Boolean(string="Active", default=True)
    file = fields.Binary(string='file', attachment=True)
    file_name = fields.Char("File Name")
    state = fields.Selection([('draft', 'Draft'),
                                ('under_review', 'Under Review'),
                                ('accepted', 'Accepted'),
                                ('refused', 'Refused')], default='draft', string='Status', required=True, tracking=True)



    @api.constrains('file')
    def _check_file(self):
        if str(self.file_name.split(".")[1]) != 'pdf':
            raise ValidationError("Cannot upload file different from .pdf file")


    @api.depends('establish_date')
    def _cumpute_years(self):
        for rec in self:
            today = date.today()
            if rec.establish_date:
                rec.age = today.year - rec.establish_date.year
            else:
                rec.age = 0


    @api.depends('current_university')
    def _cumpute_transfer(self):
        for rec in self:
            if rec.current_university == 'Université abdelhamid mehri constantine 2':
                rec.type_transfer = 'Interne'
            else:
                rec.type_transfer = 'Extarne'


    # action on click on button
    def action_draft(self):
        for rec in self:
                rec.state = 'draft'

    def action_in_review(self):
        for rec in self:
                rec.state = 'under_review'

    def action_accepted(self):
        for rec in self:
                rec.state = 'accepted'

    def action_refused(self):
        for rec in self:
                rec.state = 'refused'


