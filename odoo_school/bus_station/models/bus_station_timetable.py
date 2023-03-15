from odoo import models, fields


class BusStationTimetable(models.Model):
    _name = 'bus.station.timetable'
    _description = 'Bus Station Timetable'

    route_id = fields.Many2one(
        comodel_name='bus.station.route',
        required=True
    )
    driver_id = fields.Many2one(
        comodel_name='res.partner',
        required=True,
        domain=[('is_driver', '=', True)]
    )
    bus_id = fields.Many2one(
        comodel_name='bus.station.bus',
        required=True
    )
    capacity = fields.Integer(
        string='Numbers of seats',
        related='bus_id.capacity'
    )
    departure_date = fields.Datetime(required=True)
    arrival_date = fields.Datetime(required=True)

    def name_get(self):
        """ Display 'route_id + departure_date' """
        res = []
        for timetable in self:
            name = timetable.route_id.name + ' ' \
                   + str(timetable.departure_date)
            res.append((timetable.id, name))
        return res
