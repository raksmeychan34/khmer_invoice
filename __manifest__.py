{
    "name" : "Khmer Invoice",
    "summary": """
            This addon will add two new print options on Customer Invoices,
            following Cambodia's Tax Invoice and Commercial Invoice
        """,
    "version": "19.0.1.0.0",
    "author": "Raksmey",
    "license": "AGPL-3",
    "website": "",
    "category": "Accounting/Localizations",
    "depends": ["account"],
    "data": [
        "views/res_partner_views.xml",
        "views/report_paperformat_kh_invoice.xml",
        "views/report_kh_tax_invoice.xml",
        "views/report_kh_commercial_invoice.xml",
    ],
    "images": ["static/description/icon.png"],
    "installable": True,
    "application": False,
}