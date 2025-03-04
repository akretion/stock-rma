# Copyright (C) 2017-20 ForgeFlow S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html)

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    rma_mandatory_cause = fields.Boolean(
        related="company_id.rma_mandatory_cause",
        readonly=False,
        help="It won't be possible to approve RMA with no causes and responsibles set",
    )
