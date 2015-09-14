# b-*- encoding: utf-8 -*-

from openerp import models, fields

class Product(models.Model):
    _name = 'sat.product'

    name = fields.Char(string="Product Name", required=True)
    description = fields.Text(string="Product Description")