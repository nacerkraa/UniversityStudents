# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Academy(http.Controller):

    @http.route('/academy/academy/', auth='public', website=True)
    def index(self, **kw):
        Students = http.request.env['school.student']
        return http.request.render('school_management.index', {
            'students': Students.search([])
        })

class School(http.Controller):

    @http.route('/student_webform', type="http", auth="public", website=True)
    def student_webform(self, **kw):
        return http.request.render('school_management.create_student', {'student_name': 'Odoo Mates Test 123',
                                                                  'doctor_rec': 'doctor_rec'})

    @http.route('/create/webstudent', type="http", auth="public", website=True)
    def create_webpatient(self, **kw):
        request.env['school.student'].sudo().create(kw)
        return request.render("school_management.student_thanks", {})

