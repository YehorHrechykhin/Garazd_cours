from odoo import _, models, fields
from odoo.exceptions import ValidationError


class BusStationBuyTicketWizard(models.TransientModel):
    _name = 'bus.station.buy.ticket.wizard'
    _description = 'Bus Station Buy Ticket Wizard'

    timetable_id = fields.Many2one(
        comodel_name='bus.station.timetable',
        required=True
    )
    seat_number = fields.Integer(
        required=True
    )

    def action_buy_ticket(self):
        """Function to buy ticket"""
        timetable_id = self.timetable_id
        seat_number = self.seat_number

        # Check if the seat is already taken
        existing_ticket = self.env['bus.station.ticket'].search([
            ('timetable_id', '=', timetable_id.id),
            ('seat_number', '=', seat_number)
        ])
        if existing_ticket:
            raise ValidationError(_('Seat already taken'))

        # Create new ticket record
        self.env['bus.station.ticket'].create({
            'timetable_id': timetable_id.id,
            'seat_number': seat_number
        })


