# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.tools.float_utils import float_round

class Product(models.Model):
    _inherit = "product.product"

    def action_view_stock_move_lines_valuation(self):
        self.ensure_one()
        action = self.env.ref('stock_product_valuation.stock_move_line_action_valuation').read()[0]
        action['domain'] = [('product_id', '=', self.id)]
        return action

class ProductTemplate(models.Model):
    _inherit = 'product.template'


    @api.depends('product_variant_ids.value_svl')
    def _compute_value_svl(self):
        """Compute 'value_svl' for product template"""
        for product in self:
            product.value_svl = float_round(
                sum([p.value_svl for p in product.product_variant_ids]),
                precision_rounding=product.uom_id.rounding)

    value_svl = fields.Float(compute='_compute_value_svl')


    def action_view_stock_move_lines_valuation(self):
        self.ensure_one()
        action = self.env.ref('stock_product_valuation.stock_move_line_action_valuation').read()[0]
        action['domain'] = [('product_id.product_tmpl_id', 'in', self.ids)]
        return action
