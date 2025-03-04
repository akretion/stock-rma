# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html)

from odoo import _, api, exceptions, fields, models


class RmaOrderLine(models.Model):
    _inherit = "rma.order.line"

    responsible_id = fields.Many2one("rma.responsible", string="Responsible")
    cause_id = fields.Many2one(
        "rma.cause",
        compute="_compute_cause_id",
        store=True,
        readonly=False,
        string="Problem",
    )
    cause_id_domain = fields.Binary(compute="_compute_cause_id_domain")

    @api.depends("responsible_id")
    def _compute_cause_id(self):
        for rec in self:
            if not rec.responsible_id:
                rec.cause_id = False

    @api.depends("responsible_id")
    def _compute_cause_id_domain(self):
        for rec in self:
            allowed_causes = rec.responsible_id.cause_ids
            rec.cause_id_domain = [("id", "in", allowed_causes.ids)]

    def action_rma_approve(self):
        for rec in self:
            if rec.company_id.rma_mandatory_cause:
                if not rec.cause_id or not rec.responsible_id:
                    raise exceptions.UserError(
                        _(
                            "You have to set a responsible and a cause to the RMA "
                            "before beeing able to validate it."
                        )
                    )
        return super().action_rma_approve()
