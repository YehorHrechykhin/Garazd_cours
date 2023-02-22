from odoo import api, models, fields


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patients'

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
    doctor = fields.Many2one(
        comodel_name='hospital.doctor',
        string='Attending doctor',
        required=True
    )
    birthday = fields.Date(string='Birthday date')
    age = fields.Integer(
        string='Full years',
        compute='_compute_age',
        store=True
    )
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('non-binary', 'Non-binary')
    ],
        string='Sex'
    )
    phone_number = fields.Char(
        string='Phone number',
        size=10
    )

    @api.depends('first_name', 'last_name')
    def _compute_full_name(self):
        for record in self:
            record.full_name = f"{record.first_name} {record.last_name}"

    @api.depends('birthday')
    def _compute_age(self):
        for record in self:
            if record.birthday:
                age = (fields.Date.today() - record.birthday).days // 365
                record.age = age

    def name_get(self):
        result = []
        for rec in self:
            name = rec.full_name
            result.append((rec.id, name))
        return result
