from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    kh_invoice_default_logo = fields.Binary(
        string="Default Invoice Logo",
        help="Used on the Khmer Tax/Commercial Invoice reports whenever "
             "this company's Contact record has no logo set. "
             "Configure this in Accounting/General Settings.",
    )