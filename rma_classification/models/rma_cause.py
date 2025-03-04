# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html)

from odoo import fields, models


class RmaCause(models.Model):
    _name = "rma.cause"
    _description = "Cause of the RMA"
    _order = "name"

    active = fields.Boolean(
        default=True,
        help="The active field allows you to hide the category without removing it.",
    )
    name = fields.Char(
        required=True,
        copy=False,
        translate=True,
    )
    responsible_ids = fields.Many2many(
        "rma.responsible", "rma_responsible_rma_cause_rel"
    )

    _sql_constraints = [
        ("name_uniq", "unique (name)", "Cause name already exists !"),
    ]
