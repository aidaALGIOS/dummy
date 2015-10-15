# -*- coding: utf-8 -*-
# See README.rst file on addon root folder for license details

from openerp import models, fields, api

class Brand(models.Model):

    _name = 'sat.brand'
    _order = 'name'

    name = fields.Char(size=64, required=True)
    description = fields.Text(help="Feel free to explain the Brand")
    active = fields.Boolean(default=True, help="If the active field is set to False, it will allow you to hide the brand without removing it.")

    _sql_constraints = [('sat_brand_unique_name', 'UNIQUE(name)','The brand name must be unique!')]