# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError
from odoo.tools import pycompat
from odoo.tools.float_utils import float_round


class Product(models.Model):
    _inherit = "product.product"

    @api.multi
    def _compute_purchase_total(self):
        domain = [
            ('state', 'in', ['purchase', 'done']),
            ('product_id', 'in', self.mapped('id'))
        ]
        order_lines = self.env['purchase.order.line'].read_group(domain, ['product_id', 'product_qty'],
                                                                 ['product_id'])
        purchase_data = dict([(data['product_id'][0], data['product_qty']) for data in order_lines])
        for product in self:
            product.purchases_count = float_round(purchase_data.get(product.id, 0),
                                                  precision_rounding=product.uom_id.rounding)

    purchases_count = fields.Integer(string='purchase', compute='_compute_purchase_total')

    @api.multi
    def action_view_purchases(self):
        self.ensure_one()
        action = self.env.ref('ov_purchase_status.action_purchase_order_line_status').read()[0]
        action['domain'] = [('product_id', '=', self.id),('state','in',('purchase', 'done'))]
        return action


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.multi
    def _compute_purchase_total(self):
        for template in self:
            template.purchases_count = float_round(
                sum([p.purchases_count for p in template.product_variant_ids]),
                precision_rounding=template.uom_id.rounding)

    purchases_count = fields.Integer(string='purchase', compute='_compute_purchase_total')

    @api.multi
    def action_view_purchases(self):
        self.ensure_one()
        action = self.env.ref('ov_purchase_status.action_purchase_order_line_status').read()[0]
        action['domain'] = [('product_id.product_tmpl_id', 'in', self.ids),('state','in',('purchase', 'done'))]
        return action
