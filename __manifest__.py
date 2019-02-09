# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'digizilla',
    'version' : '1.0',
    'summary': 'a module in a task from digizilla company',
    'sequence': '30',
    'description': """
a module in a task from digizilla company .
    """,
    'category': 'task',
    'website': '',
    'images' : [],
    'depends' : ['base', 'mail'],
    'data': [
    'views/digizilla.xml',
    'views/report.xml'
    ],
    'demo': [
    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}
