from datetime import date
from odoo import api, fields, models


class UniversityStudent(models.Model):
    _name = 'university.student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'University Student from university'
    _rec_name = 'ref'

    ref = fields.Char(string="Ref")
    first_name = fields.Char(string="Firstname")
    task_attachment = fields.Many2many(comodel_name="ir.attachment",
                                       relation="m2m_ir_identity_card_rel",
                                       column1="m2m_id",
                                       column2="attachment_id",
                                       string="Identity Card")
    e_level = fields.Selection([('1', '1er année de licence'),
                                ('2', '2eme année de licence'),
                                ('3', '3eme année de licence'),
                                ('4', '1ere master'),
                                ('5', '2eme master')], string="Level")
    n_years = fields.Integer(string="Years number on university", compute='_cumpute_years')
    establish_date = fields.Date(string="Establish Date")
    n_years_repeating = fields.Integer(string="numbre des annie rdeblement")
    c_academic = fields.Selection([('1', 'Oui'),
                                   ('0', 'Non')], string="number de cange acadimique")
    # last_name = fields.Char(string="Lastname")
    # email = fields.Char(string="Email")
    # age = fields.Integer(string="Age")
    # address = fields.Char(string="Address")
    # nationality = fields.Char(string="Nationality")
    # s_bac = fields.Char(string="Serie de Bac")
    # f_bac = fields.Char(string="Filiere de Bac")
    # rate = fields.Float(string="Rate")
    # current_university = fields.Char(string="University")
    # current_faculty = fields.Char(string="Faculty1")
    # next_faculty = fields.Char(string="Faculty2")

    # Other fields
    # type_transfer = fields.Char(string="type", compute='_cumpute_transfer')
    comment = fields.Html(string="comment")
    active = fields.Boolean(string="Active", default=True)
    state = fields.Selection([('draft', 'Draft'),
                              ('under_review', 'Under Review'),
                              ('accepted', 'Accepted'),
                              ('refused', 'Refused')], default='draft', string='Status', required=True, tracking=True,
                             compute='_cumpute_status')

    def action_send_reply_by_email(self):
        template_obj = self.env['mail.mail']
        template_data = {
            'subject': 'messege from the university of : ' + self.university,
            'body_html': 'the message here',
            'email_from': 'name@univ.edu',
            'email_to': self.email
        }
        template_id = template_obj.create(template_data)
        template_obj.send(template_id)

    @api.depends('establish_date')
    def _cumpute_years(self):
        for rec in self:
            today = date.today()
            if rec.establish_date:
                rec.n_years = today.year - rec.establish_date.year
            else:
                rec.n_years = 0

    @api.depends('e_level', 'c_academic', 'n_years_repeating')
    def _cumpute_status(self):
        for rec in self:
            # numbre_des_annies = 3 - int(rec.c_academic) + int(rec.n_years_repeating)
            if int(rec.e_level) + int(rec.n_years_repeating) > 3 + int(rec.c_academic):
                rec.state = 'refused'
            else:
                rec.state = 'accepted'

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
