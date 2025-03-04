# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html)

{
    "name": "RMA Classification",
    "version": "16.0.2.0.0",
    "license": "LGPL-3",
    "category": "RMA",
    "summary": "Add RMA sources and defects to classify RMAs",
    "author": "Akretion,ForgeFlow",
    "website": "https://github.com/ForgeFlow/stock-rma",
    "depends": ["rma"],
    "data": [
        "security/ir.model.access.csv",
        "views/rma_order_line.xml",
        "views/rma_order.xml",
        "views/rma_responsible.xml",
        "views/rma_cause.xml",
        "views/res_config_settings_views.xml",
    ],
    "installable": True,
}
