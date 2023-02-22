from odoo import models, fields


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointments'

    patient_id = fields.Many2one(
        comodel_name='hospital.patient',
        string='Patient name',
        required=True
    )
    doctor_id = fields.Many2one(
        comodel_name='hospital.doctor',
        string='Doctor name',
        required=True
    )
    date = fields.Date(
        string='Date of appointment',
        required=True
    )
    reason = fields.Text(
        string='Reason for visit',
        required=True
    )
    diagnosis = fields.Text(string='Final diagnosis')
