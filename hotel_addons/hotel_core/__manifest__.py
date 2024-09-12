
{
    'name': 'Global Hotel Management',
    'version': '1.0',
    'summary': 'Complete module template for Odoo',
    'description': 'This is a full template module for Odoo, created by Younes Ellouza. It contains all possible components of an Odoo module.',
    'author': 'Younes Ellouza',
    'website': 'https://www.softarena.ma',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/17.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'depends': ['base', 'web'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/my_model_views.xml',
        'views/menu_views.xml',
        'reports/report_file.xml',
        'data/data_file.xml',
    ],
    'demo': ['demo/demo_data.xml'],
    'qweb': ['static/src/xml/*.xml'],
    'installable': False,
    'application': False,
    'auto_install': False,
}
