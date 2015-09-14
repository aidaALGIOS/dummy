# b-*- encoding: utf-8 -*-

from openerp import models, fields

class Equipment(models.Model):
    _name = 'sat.equipment'

    name = fields.Char(string="Equipment Name", required=True)
    description = fields.Text(string="Equipment Description")