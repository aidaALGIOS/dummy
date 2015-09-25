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

from openerp import models, fields

class Company(models.Model):
    _inherit = 'res.company'

    manage_equipments = fields.Boolean()
    manage_contracts = fields.Boolean()
    work_time_rounding = fields.Integer(default=5)
    invoice_time_rounding = fields.Integer(default=15)
    register_work_time = fields.Boolean()