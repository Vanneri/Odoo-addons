from odoo import api, fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    @api.depends('stock_valuation_layer_ids')
    def _compute_value_svl(self):
        """Compute `value_svl` for getting stock move value"""
        company_id = self.env.context.get('force_company', self.env.company.id)
        domain = [
            ('stock_move_id', 'in', self.ids),
            ('company_id', '=', company_id),
        ]
        groups = self.env['stock.valuation.layer'].read_group(domain, ['value:sum','unit_cost:sum'], ['stock_move_id'])
        products = self.browse()
        for group in groups:
            move = self.browse(group['stock_move_id'][0])
            move.value_svl = self.env.company.currency_id.round(group['value'])
            move.value_price = self.env.company.currency_id.round(group['unit_cost'])
            move |= move

    value_svl = fields.Float(compute='_compute_value_svl',string='Value')
    value_price = fields.Float(compute='_compute_value_svl',string='Price')

class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    value_svl = fields.Float(related='move_id.value_svl', string='Value')
    value_price = fields.Float(related='move_id.value_price', string='Price')