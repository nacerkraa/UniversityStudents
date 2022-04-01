# -*- coding: utf-8 -*-
from odoo import http


class TestWebsite(http.Controller):
    @http.route('/test_website/test_website', auth='public')
    def index(self, **kwargs):
        return "Hello, world"

    @http.route('/test_website/test_website/objects', auth='public')
    def list(self, **kw):
        return http.request.render('test_website.listing', {
            'root': '/test_website/test_website',
            'objects': http.request.env['test_website.test_website'].search([]),
        })

#     @http.route('/test_website/test_website/objects/<model("test_website.test_website"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_website.object', {
#             'object': obj
#         })
