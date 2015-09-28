# -*- coding: utf-8 -*-
# See README.rst file on addon root folder for license details

{
    'name': "SAT",

    'summary': """SAT""",

    'description': """
        SAT
    """,

    'author': "Algios",
    'website': "http://www.algios.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/sat_security.xml',
        'security/ir.model.access.csv',
        'views/sat_config_view.xml',
    ],

    # only loaded in demonstration mode
    'demo': [],
}
