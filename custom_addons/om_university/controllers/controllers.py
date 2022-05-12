# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import base64

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
    def upload_files(self, **post):
        values = {}
        if post.get('task_attachment', False):
            Attachments = request.env['ir.attachment']
            name = post.get('task_attachment').filename
            file = post.get('task_attachment')
            project_id = post.get('ref')
            firstname = post.get('first_name')
            attachment = file.read()
            attachment_id = Attachments.sudo().create({
                'name': name,
                # 'datas_fname': name,
                'res_name': name,
                'type': 'binary',
                'res_model': 'model.model',
                'res_id': project_id,
                'datas': base64.b64encode(attachment),
            })

            values = {
                'ref': project_id,
                'first_name': firstname,
                'task_attachment': attachment_id,
            }

            request.env['university.student'].sudo().create(values)

        return request.render("om_university.student_thanks", {})
