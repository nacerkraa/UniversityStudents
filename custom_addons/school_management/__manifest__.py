# -*- coding: utf-8 -*-
{
    'name': "School Management",
    'version': '1.0.0',
    'category': 'School',
    'summary': "School Management System",
    'description': """School Management System""",
    'author': 'Nacer KRAA',
    'depends': [],
    'data': [
        # 'security/ir.model.access.csv',
        'views/menu.xml',
        'views/student_view.xml',

    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'sequence': -100,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'website': "http://www.yourcompany.com",
}
