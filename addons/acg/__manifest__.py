# -*- coding: utf-8 -*-
{
	'name': 'ACG',

	'summary': """
        Real Estate Management""",

	'description': """
        Real Estate Management"
    """,

	'author': "Thanh Cong A Chau",
	'website': "http://www.vietinterview.com",

	# Categories can be used to filter modules in modules listing
	# Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
	# for the full list
	'category': 'insurance, human resource, recuirement', 'payrole'
														  'version': '0.1',

	'application': True,

	# any module necessary for this one to work correctly
	'depends': ['base'],
	# always loaded
	'data': [
		# 'security/ir.model.access.csv',
        #'data/location.xml',
        'data/mail.xml',
        #'data/copyright.xml',
		#'data/hr.xml',

	],
	# only loaded in demonstration mode
	'demo': [
		'demo/demo.xml',
	],
}
