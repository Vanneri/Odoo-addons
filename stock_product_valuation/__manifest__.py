# -*- coding: utf-8 -*-
{
    'name': "Stock Valuation in Product",

    'summary': """
        Module will display valuation amount and details in Product""",

    'description': """""",
    'author': "Vishnu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Operations/Inventory',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['stock_account'],

    # always loaded
    'data': [
        'views/product.xml',
        'views/stock.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
