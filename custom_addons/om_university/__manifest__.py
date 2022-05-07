# -*- coding: utf-8 -*-
{
    'name': "University Transfers",
    'version': '1.0.0',
    'category': 'University',
    'summary': "University Transfers System",
    'description': """University Transfers System""",
    'author': 'Nacer KRAA',
    'depends': ['mail', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/student_view.xml',
        'views/faculty_view.xml',
        'views/univ_view.xml',
        'views/website_form.xml',
        'data/mail_template.xml',
    ],
    'demo': [],
    'sequence': -100,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'website': "http://www.yourcompany.com",

}

