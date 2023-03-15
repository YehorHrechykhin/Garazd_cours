from odoo import models, fields


class BusStationTicket(models.Model):
    _name = 'bus.station.ticket'
    _description = 'Bus Ticket'

    timetable_id = fields.Many2one(
        comodel_name='bus.station.timetable',
        required=True
    )
    departure_date = fields.Datetime(related='timetable_id.departure_date')
    seat_number = fields.Integer(required=True)
