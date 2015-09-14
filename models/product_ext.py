# b-*- encoding: utf-8 -*-

from openerp import models, fields
 
class product_template(models.Model):
    _name = 'product.template' 
    _inherit = 'product.template' 

    uniqueness = fields.Boolean(string="Uniqueness", required=True)
    maintainable = fields.Boolean(string="Maintainable", required=True)
