from odoo import models, fields


class BusStationStation(models.Model):
    _name = 'bus.station.station'
    _description = 'Bus Station'

    name = fields.Char(required=True)
    city = fields.Char(required=True)

    def name_get(self):
        """ Display 'city + station name' """
        res = []
        for station in self:
            name = station.city + ', ' + station.name
            res.append((station.id, name))
        return res
