# -*- coding: utf-8 -*-
{
    'name': "moduloapg",

    'summary': """
        Módulo realizado por Andrés Samuel Podadera González, SGE 24-25
        """,

    'description': """
        Modulo que sirve para gestionar información de una biblioteca
    """,

    'author': "Andrés Samuel Podadera González",
    'website': "https://www.andrescoder.dev/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Extra Tools',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
}