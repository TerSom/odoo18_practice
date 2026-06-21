from odoo import models, fields, api
from datetime import timedelta

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estater Property Offer'

    price = fields.Float()
    status = fields.Selection([('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    property_id = fields.Many2one('estate.property', string='Property', required=True)
    validity = fields.Integer(string='Validity (days)', default=7)
    date_deadline = fields.Date(compute='_compute_date_deadline', inverse='_inverse_date_deadline')

    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for record in self:

            create_date = (
                record.create_date.date()
                if record.create_date
                else fields.Date.today()
            )

            record.date_deadline = (
                create_date +
                timedelta(days=record.validity)
            )
    
    def _inverse_date_deadline(self):
        for record in self:

            create_date = (
                record.create_date.date()
                if record.create_date
                else fields.Date.today()
            )

            record.validity = (
                record.date_deadline -
                create_date
            ).days