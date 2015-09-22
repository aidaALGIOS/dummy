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
        help="This allows you to define special conditions to manage and invoice your S.A.T tasks."
    )

    @api.one
    def set_company_values(self):
        company = self.env.user.company_id
        company.manage_equipments = self.group_manage_equipments
        company.manage_contracts = self.group_manage_contracts