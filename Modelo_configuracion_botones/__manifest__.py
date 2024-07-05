{
    'name': 'Config Novici Module',
    'version': '1.0',
    'summary': 'Este es un modulo de prueba para crear tus propias configuraciones',
    'category': 'Tools',
    'author': 'Novici',
    'website': 'https://www.odoo.com/es/partners/novici-12925418',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/config_novici_data.xml',
        'views/config_novici_views.xml',
    ],
    'installable': True,
    'application': True,
}
