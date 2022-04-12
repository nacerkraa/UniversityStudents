# -*- coding: utf-8 -*-

from odoo import models, fields, api


class school_management(models.Model):
    _name = 'school.student'
    _description = 'this is a school for student'

    name = fields.Char(string="Name")
    age = fields.Integer(string="Age")
    description = fields.Text(string="Text")
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
