# -*- coding: utf-8 -*-
{
    'name': "Hospital Manager",
    'summary': "Product for hospitals and patients",
    'description': """
          using this module for complete manage your hospital and get good reports 
    """,
    'author': "Mahmoud Hashem",
    'website': "https://www.hashem.com",
    'category': 'Uncategorized',
    'version': '0.1.1',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/data.xml',
        'wizards/add_appointment.xml',
        'views/templates.xml',
        'views/views.xml',
        'views/doctors.xml',
        'views/appointments.xml',
        'views/medicines.xml',
        'views/menus.xml'
    ],
}

