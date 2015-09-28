# -*- coding: utf-8 -*-
# See README.rst file on addon root folder for license details

from openerp import models, fields, api

class SatConfiguration(models.TransientModel):
    _inherit = 'res.config.settings'
    _name = 'sat.config.settings'

    group_manage_equipments = fields.Boolean(
        string="Manage equipments",
        group='base.group_user',
        implied_group='sat.group_manage_equipments',
        help="This allows you to check which products are contained in your customer installations."
    )

    group_manage_contracts = fields.Boolean(
        string="Manage contracts",
        group='base.group_user',
        implied_group='sat.group_manage_contracts',
        help="This allows you to define special conditions to manage and invoice your SAT tasks."
    )

    @api.one
    def set_company_values(self):
        company = self.env.user.company_id
        company.write({
            'manage_equipments': self.group_manage_equipments,
            'manage_contracts': self.group_manage_contracts
        })