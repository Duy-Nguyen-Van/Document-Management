{
	'name': 'Document Management',
	'description': '[test]Manage your personal Document tasks.',
	'author': 'ISLab Team',
	'depends': ['base','mail','hr'],
	'application': True,
	'images':['images/icon.png'],
	'data': [
		'views/qlcv_menu.xml',
        'views/qlcv_view.xml',
		'security/user_groups.xml',
		'security/ir.model.access.csv',
		'security/qlcv_access_rule.xml',
		'data/mail_template_data.xml',
	],
	'demo' : [
		# 'data/doc_task.csv'
		'data/doc_data.xml'
	],
	'qweb' : ['static/src/xml/qweb.xml'],
}
