from odoo import models, fields


class Invoice(models.Model):
    _inherit = 'account.move.line'

    dimension = fields.Char(string="Dimension", default=0, readonly=True)