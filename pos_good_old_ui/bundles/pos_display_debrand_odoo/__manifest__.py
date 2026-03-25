{
    'name': "POS Display Debrand Odoo",
    'summary': "Debrands Odoo from the Point of Sale UI",
    'description': """
POS Display Debrand Odoo.

Published by Wedo Technologies Marketing.
Website: https://www.wedo.om
LinkedIn: https://www.linkedin.com/company/wedo-technologies/
    """,
    'author': "Wedo Technologies Marketing",
    'website': "https://www.wedo.om",
    'license': 'LGPL-3',
    'category': 'Point of Sale',
    'version': '1.0',
    'images': ['static/description/banner.png'],
    'depends': ['point_of_sale'],
    'data': [],
    'demo': [],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_display_debrand_odoo/static/src/**/*',
        ],
        'point_of_sale.customer_display_assets': [
            'pos_display_debrand_odoo/static/src/customer_display/**/*',
        ],
    }
}
