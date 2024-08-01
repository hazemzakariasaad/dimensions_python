from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    dimension = fields.Char(string="Dimension", related='product_id.dimension', readonly=False, store=True)

