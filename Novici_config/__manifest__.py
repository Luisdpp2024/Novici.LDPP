{
    'name': 'Config Novici Module',
    'version': '1.0',
    'summary': 'A module to add a boolean field to Config Novici',
    'category': 'Tools',
    'author': 'Your Name',
    'website': 'http://www.yourwebsite.com',
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
