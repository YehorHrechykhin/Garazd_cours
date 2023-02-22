from odoo import api, models, fields


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctors'

    first_name = fields.Char(
        string='Name',
        required=True
    )
    last_name = fields.Char(
        string='Surname',
        required=True
    )
    full_name = fields.Char(
        string='Name',
        compute='_compute_full_name'
    )
    specialty = fields.Char(
        string='Medical specialty',
        required=True
    )
    phone_number = fields.Char(
        string='Phone number',
        size=10
    )

    @api.depends('first_name', 'last_name')
    def _compute_full_name(self):
        for record in self:
            record.full_name = f"{record.first_name} {record.last_name}"

    def name_get(self):
        result = []
        for rec in self:
            name = rec.full_name
            result.append((rec.id, name))
        return result
