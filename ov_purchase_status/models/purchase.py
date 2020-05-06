# -*- coding: utf-8 -*-

from odoo import api, exceptions, fields, models, _
from odoo.tools import email_re, email_split, email_escape_char, float_is_zero, float_compare, \
    pycompat, date_utils

from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning

from odoo.addons import decimal_precision as dp
import logging

_logger = logging.getLogger(__name__)


class PurchaseOrder(models.Model):
    _name = 'purchase.order'
    _inherit = 'purchase.order'

    @api.multi
    @api.depends('order_line.qty_received')
    def _get_delivery_status(self):
        """ compute over all delivery status From line.
        """
        for order in self:
            deliver_quantity = sum(
                order.mapped('order_line').filtered(lambda r: r.product_id.type != 'service').mapped('qty_received'))
            order_quantity = sum(
                order.mapped('order_line').filtered(lambda r: r.product_id.type != 'service').mapped('product_uom_qty'))
            if order_quantity >= deliver_quantity > 0:
                order.delivery_status = 'partially delivered'
            elif order_quantity <= deliver_quantity:
                order.delivery_status = 'delivered'
            else:
                order.delivery_status = 'not delivered'

    delivery_status = fields.Selection([
        ('not delivered', 'Not Delivered'),
        ('partially delivered', 'Partially Delivered'),
        ('delivered', 'Fully Delivered')
    ], string='Delivery Status', compute="_get_delivery_status", store=True, readonly=True)


class PurchaseOrderLine(models.Model):
    _name = 'purchase.order.line'
    _inherit = 'purchase.order.line'

    @api.multi
    @api.depends('qty_received')
    def _get_delivery_status(self):
        """ compute delivery status based on Qty delivered.
        """
        for line in self:
            if line.product_qty >= line.qty_received > 0:
                line.delivery_status = 'partially delivered'
            elif line.product_qty <= line.qty_received:
                line.delivery_status = 'delivered'
            else:
                line.delivery_status = 'not delivered'

    @api.multi
    @api.depends('qty_invoiced')
    def _get_invoice_status(self):
        """ compute delivery status based on Qty delivered.
        """
        for line in self:
            if line.product_qty >= line.qty_invoiced > 0:
                line.invoice_status = 'partially invoiced'
            elif line.product_qty <= line.qty_invoiced:
                line.invoice_status = 'invoiced'
            else:
                line.invoice_status = 'not invoiced'

    delivery_status = fields.Selection([
        ('not delivered', 'Not Delivered'),
        ('partially delivered', 'Partially Delivered'),
        ('delivered', 'Fully Delivered')
    ], string='Delivery Status', compute="_get_delivery_status", store=True, readonly=True)

    invoice_status = fields.Selection([
        ('not invoiced', 'Not Invoiced'),
        ('partially invoiced', 'Partially Invoiced'),
        ('delivered', 'Fully Invoiced')
    ], string='Invoice Status', compute="_get_invoice_status", store=True, readonly=True)
