from odoo import api, models


class SaleOrderReport(models.Model):
    _inherit = 'sale.order'

    @api.model
    def get_report_values(self, docids):
        docs = self.env['sale.order'].browse(docids)
        gbp_currency = self.env['res.currency'].search([('name', '=', 'GBP')], limit=1)
        return {
            'docs': docs,
            'gbp_currency_id': gbp_currency.id,
        }

