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

    @http.route('/student_webform', type="http", auth="user", website=True)
    def student_webform(self, **kw):
        return http.request.render('om_university.create_student', {'first_name': 'Nacer'})

    @http.route('/create/webstudent', type="http", auth="user", website=True)
    def create_webpatient(self, **kw):

        if request.httprequest.method == 'POST':
            # ...
            # code that creates and fills a dictonary with validated data
            # ...
            new_task = request.env['university.student'].sudo().create(kw)
            if 'task_attachment' in request.params:
                attached_files = request.httprequest.files.getlist('task_attachment')
                for attachment in attached_files:
                    attached_file = attachment.read()
                    request.env['ir.attachment'].sudo().create({
                        'name': attachment.filename,
                        'res_model': 'project.task',
                        'res_id': new_task.ref,
                        'type': 'binary',
                        'datas_fname': attachment.filename,
                        'datas': attached_file.encode('base64'),
                    })

        # request.env['university.student'].sudo().create(kw)
        return request.render("om_university.student_thanks", {})
