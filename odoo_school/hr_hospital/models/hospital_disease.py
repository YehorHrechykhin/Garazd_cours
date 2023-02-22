from odoo import models, fields


class HospitalDisease(models.Model):
    _name = 'hospital.disease'
    _description = 'Hospital Diseases'

    name = fields.Char(
        string='Name of disease',
        required=True
    )
    description = fields.Text(string='Short description')
    symptoms = fields.Text(string='Main symptoms')
