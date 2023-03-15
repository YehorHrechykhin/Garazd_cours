from datetime import timedelta
from odoo import api, models, fields


class BusStationBus(models.Model):
    _name = 'bus.station.bus'
    _description = 'Bus Fleet'

    model = fields.Char(required=True)
    bus_number = fields.Char(required=True)
    capacity = fields.Integer(
        string='Numbers of seats',
        required=True
    )
    last_technical_inspection_date = fields.Date(required=True)
    next_technical_inspection_date = fields.Date(compute='_compute_next_technical_inspection_date')

    @api.depends('last_technical_inspection_date')
    def _compute_next_technical_inspection_date(self):
        """Show next technical inspection date"""
        for bus in self:
            if bus.last_technical_inspection_date:
                duration = timedelta(days=365)  # technical inspection every year
                next_date = bus.last_technical_inspection_date + duration
                bus.next_technical_inspection_date = next_date

    def name_get(self):
        """ Display 'bus model and number' """
        res = []
        for bus in self:
            name = bus.model + ', ' + bus.bus_number
            res.append((bus.id, name))
        return res
