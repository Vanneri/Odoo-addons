# -*- coding: utf-8 -*-
from odoo import http

# class OvPurchaseStatus(http.Controller):
#     @http.route('/ov_purchase_status/ov_purchase_status/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ov_purchase_status/ov_purchase_status/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ov_purchase_status.listing', {
#             'root': '/ov_purchase_status/ov_purchase_status',
#             'objects': http.request.env['ov_purchase_status.ov_purchase_status'].search([]),
#         })

#     @http.route('/ov_purchase_status/ov_purchase_status/objects/<model("ov_purchase_status.ov_purchase_status"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ov_purchase_status.object', {
#             'object': obj
#         })