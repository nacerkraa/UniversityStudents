# -*- coding: utf-8 -*-
# from odoo import http


# class SchoolManagement(http.Controller):
#     @http.route('/school_management/school_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/school_management/school_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('school_management.listing', {
#             'root': '/school_management/school_management',
#             'objects': http.request.env['school_management.school_management'].search([]),
#         })

#     @http.route('/school_management/school_management/objects/<model("school_management.school_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('school_management.object', {
#             'object': obj
#         })
