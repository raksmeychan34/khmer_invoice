from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    kh_invoice_default_logo = fields.Binary(
        related='company_id.kh_invoice_default_logo',
        string="Default Invoice Logo",
        readonly=False,
    )