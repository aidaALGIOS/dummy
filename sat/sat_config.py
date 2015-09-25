# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Business Applications
#    Copyright (c) 2015 Algios <http://algios.com/>
#                       Javi Melendez <javi.melendez@algios.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api, _
from openerp.exceptions import ValidationError

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

    work_time_rounding = fields.Integer(
        string="Working time rounding",
        default=5,
        help="Minimum working time unit (minutes). Every worktime will be rounded before saving. " \
             "If you change it, every registered worktime lines will remain unchanged."
    )

    invoice_time_rounding = fields.Integer(
        string="Invoicing time rounding",
        default=15,
        help="Minimum invoicing time unit (minutes). Every invoiceable duration will be rounded before invoicing. " \
             "If you change it, every registered invoice lines will remain unchanged. You can change the value in any contracts."
    )

    register_work_time = fields.Boolean(
        string="Register working time in time slots",
        help="Check if you want to know exactly when every action begins and ends. Uncheck if you only want to know the duration."
    )

    @api.one
    @api.constrains('work_time_rounding', 'invoice_time_rounding')
    def _check_positive_rounding(self):
        if self.work_time_rounding < 1:
            raise ValidationError(_("Working time rounding must be greater than 0"))
        if self.invoice_time_rounding < 1:
            raise ValidationError(_("Invoicing time rounding must be greater than 0"))

    @api.model
    def get_default_company_values(self, fields):
        """Recuperar la configuración de la compañía"""
        company = self.env.user.company_id
        return {
            'work_time_rounding': company.work_time_rounding,
            'invoice_time_rounding': company.invoice_time_rounding,
            'register_work_time': company.register_work_time
        }

    @api.one
    def set_company_values(self):
        """Guardar la configuración en la compañía"""
        company = self.env.user.company_id
        company.write({
            'manage_equipments': self.group_manage_equipments,
            'manage_contracts': self.group_manage_contracts,
            'work_time_rounding': self.work_time_rounding,
            'invoice_time_rounding': self.invoice_time_rounding,
            'register_work_time': self.register_work_time
        })