# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Academy(http.Controller):

    @http.route('/test_website/test_website', auth='public', website=True)
    def hello(self, **kw):
        return "Hello, world"

    @http.route('/academy/academy/', auth='public', website=True)
    def index(self, **kw):
        Students = http.request.env['university.student']
        return http.request.render('om_university.index', {
            'students': Students.search([])
        })

class School(http.Controller):

    @http.route('/student_webform', type="http", auth="public", website=True)
    def student_webform(self, **kw):
        return http.request.render('om_university.create_student', {'first_name': 'Nacer'})

    @http.route('/create/webstudent', type="http", auth="public", website=True)
    def create_webpatient(self, **kw):
        request.env['university.student'].create(kw)
        return request.render("om_university.student_thanks", {})

