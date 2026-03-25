{
    'name': "Good Old POS UI Bundle",
    'summary': "Bundle for Good Old POS UI modules including debranding, price display and category scroll",
    'description': """
Good Old POS UI Bundle.
This module installs all the useful POS UI adjustments provided by Wedo Technologies.

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
    'depends': [
        'pos_display_category_to_horizontal_scroll',
        'pos_display_debrand_odoo',
        'pos_display_price_in_product_card',
        'pos_display_single_piece_price_on_order_line'
    ],
    'data': [],
    'demo': [],
    'installable': True,
    'application': True,
}
