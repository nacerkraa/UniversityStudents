from datetime import date
from odoo import api, fields, models


class UniversityStudent(models.Model):
    _name = 'university.student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'University Student'
    _rec_name = 'ref'

    ref = fields.Char(string="Ref")
    first_name = fields.Char(string="Firstname")
    last_name = fields.Char(string="Lastname")
    email = fields.Char(string="Email")
    age = fields.Integer(string="Age")
    address = fields.Char(string="Address")
    nationality = fields.Char(string="Nationality")
    s_bac = fields.Char(string="Serie de Bac")
    f_bac = fields.Char(string="Filiere de Bac")
    rate = fields.Float(string="Rate")
    e_level = fields.Selection([('L1', '1er année de licence'),
                                ('L2', '2eme année de licence'),
                                ('L3', '3eme année de licence'),
                                ('M1', '1ere master'),
                                ('M2', '2eme master')], string="Level")
    establish_date = fields.Date(string="Establish Date")
    n_years_repeating = fields.Integer(string="numbre des annie rdeblement")
    c_academic = fields.Selection([('Oui', 'Oui'),
                                   ('Non', 'Non')], string="Level")
    current_university = fields.Char(string="University")
    current_faculty = fields.Char(string="Faculty1")
    next_faculty = fields.Char(string="Faculty2")

    n_years = fields.Integer(string="Years number on university", compute='_cumpute_years')
    type_transfer = fields.Char(string="type", compute='_cumpute_transfer')
    comment = fields.Html(string="comment")
    active = fields.Boolean(string="Active", default=True)
    file = fields.Binary(string='file', attachment=True)
    file_name = fields.Char("File Name")
    state = fields.Selection([('draft', 'Draft'),
                              ('under_review', 'Under Review'),
                              ('accepted', 'Accepted'),
                              ('refused', 'Refused')], default='draft', string='Status', required=True, tracking=True)

    def action_send_reply_by_email(self):
        template_id = self.env.ref('om_university.student_card_email_template').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.ref, force_send=True)

    @api.constrains('file')
    def _check_file(self):
        if str(self.file_name.split(".")[1]) != 'pdf':
            raise ValidationError("Cannot upload file different from .pdf file")

    @api.depends('establish_date')
    def _cumpute_years(self):
        for rec in self:
            today = date.today()
            if rec.establish_date:
                rec.n_years = today.year - rec.establish_date.year
            else:
                rec.n_years = 0

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
