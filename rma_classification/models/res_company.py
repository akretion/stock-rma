# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html)

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    rma_mandatory_cause = fields.Boolean()
