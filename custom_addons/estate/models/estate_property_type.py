from odoo import models, fields,api

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Estate Property Type'
    _order = 'sequence ,name'

    name = fields.Char(required=True)
    property_ids = fields.One2many('estate.property', 'type_id',)
    sequence = fields.Integer('Sequence', default=1)
    offer_ids = fields.One2many('estate.property.offer','property_type_id')
    offer_count = fields.Integer(compute="_compute_offer_count")
    
    _sql_constraints = [
        ('check_unique_name', 'UNIQUE(name)',
        'Nama harus unik')
    ]

    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
