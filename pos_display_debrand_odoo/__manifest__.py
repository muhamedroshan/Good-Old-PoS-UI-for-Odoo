{
    'name': "POS Display Debrand Odoo",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Wedo Technologies",
    'website': "https://www.wedo.om",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_display_debrand_odoo/static/src/**/*',
        ],
        'point_of_sale.customer_display_assets': [
            'pos_display_debrand_odoo/static/src/customer_display/**/*',
        ],
    }
}
