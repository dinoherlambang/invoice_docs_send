#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class invoices_move(models.Model):

    _name = "account.move"
    _description = "account.move"

    _inherit = "account.move"

    docs_status = fields.Selection(selection=[("sent","Sent"),("recieved","Recieved")],  string="Docs Status", tracking=True, tracking_visibility='always',  help="")    
    recieve_date = fields.Date( string="Date", tracking=True, tracking_visibility='always',  help="")
    recieve_by = fields.Char( string="Recieve by", tracking=True, tracking_visibility='always',  help="")
    photo = fields.Binary( string="Photo", tracking=True, tracking_visibility='always',  help="")
    note = fields.Text(string="Note", tracking=True, tracking_visibility='onchange',  help="")


    # @api.onchange('docs_status')
    # def check_status(self):
    #     if self.docs_status == 'recieved':
    #         if not self.recieve_by or not self.photo:
    #             raise UserError(_('Recieve By or Photo is still empty'))

    @api.model
    def write(self, vals):
        if 'docs_status' in vals and vals['docs_status'] == 'recieved':
            for record in self:
                if not record.recieve_by or not record.photo:
                    raise UserError(_('Recieve By and Photo must be filled to change status as Received.'))
        return super(invoices_move, self).write(vals)