# -*- coding: utf-8 -*-
# from odoo import http


# class StockProductValuation(http.Controller):
#     @http.route('/stock_product_valuation/stock_product_valuation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_product_valuation/stock_product_valuation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_product_valuation.listing', {
#             'root': '/stock_product_valuation/stock_product_valuation',
#             'objects': http.request.env['stock_product_valuation.stock_product_valuation'].search([]),
#         })

#     @http.route('/stock_product_valuation/stock_product_valuation/objects/<model("stock_product_valuation.stock_product_valuation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_product_valuation.object', {
#             'object': obj
#         })
