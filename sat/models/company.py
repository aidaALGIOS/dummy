# -*- coding: utf-8 -*-
# See README.rst file on addon root folder for license details

from openerp import models, fields

class Company(models.Model):
    _inherit = 'res.company'

    manage_equipments = fields.Boolean()
    manage_contracts = fields.Boolean()
    work_time_rounding = fields.Integer(default=5)
    invoice_time_rounding = fields.Integer(default=15)
    register_work_time = fields.Boolean()
    support_analytic_root_id = fields.Many2one('account.analytic.account')