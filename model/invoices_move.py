#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class invoices_move(models.Model):

    _name = "account.move"
    _description = "account.move"

    _inherit = "account.move"
    docs_status = fields.Selection(selection=[("belum","Belum Dikirim"),("terkirim","Terkirim")],  string="Docs status",  help="")
    recieve_date = fields.Date( string="Recieve Date",  help="")
    recieve_by = fields.Char( string="Recieve by",  help="")
    photo = fields.Binary( string="Photo",  help="")


