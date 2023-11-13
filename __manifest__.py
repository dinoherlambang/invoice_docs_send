#-*- coding: utf-8 -*-

{
	"name": "Invoice Docs Send",
	"version": "1.0", 
	"depends": [
		'base','account'
	],
	"author": "Dino Herlambang",
	"category": "Utility",
	"website": "dino.herlambang@gmail.com",
	"images": ["static/description/images/main_screenshot.jpg"],
	"price": "10",
	"license": "LGPL-3",
	"currency": "USD",
	"summary": "This is the Invoice Docs Send module",
	"description": """

Information
======================================================================

* created menus
* created objects
* created views
* logics

""",
	"data": [
		"security/groups.xml",
		"security/ir.model.access.csv",
		"view/menu.xml",
		"view/invoices_move.xml", #inherited
	],
	"installable": True,
	"auto_install": False,
	"application": True,
}