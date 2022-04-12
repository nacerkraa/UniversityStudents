# -*- coding: utf-8 -*-
from odoo import http


class Academy(http.Controller):

    @http.route('/academy/academy/', auth='public')
    def index(self, **kw):
        Students = http.request.env['school.student']
        return http.request.render('school_management.index', {
            'student': Students.search([])
        })

    # @http.route('/custom', auth='public', website=True)
    # def index(self):
    #     student = http.request.env['school.student'].search([])
    #     return http.request.render(
    #         'school_management.index', {'students': student}
    #     )

    # @http.route('/test_website/test_website/objects', auth='public')
    # def list(self, **kw):
    #     return http.request.render('test_website.listing', {
    #         'root': '/test_website/test_website',
    #         'objects': http.request.env['test_website.test_website'].search([]),
    #     })

#     @http.route('/test_website/test_website/objects/<model("test_website.test_website"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_website.object', {
#             'object': obj
#         })
