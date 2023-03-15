from odoo import api, models, fields


class BusStationRoute(models.Model):
    _name = 'bus.station.route'
    _description = 'Bus Route'

    name = fields.Char(required=True)
    station_from_id = fields.Many2one(
        comodel_name='bus.station.station',
        required=True
    )
    station_to_id = fields.Many2one(
        comodel_name='bus.station.station',
        required=True
    )

    @api.onchange('station_from_id', 'station_to_id')
    def _onchange_station(self):
        if self.station_from_id and self.station_to_id:
            self.name = self.station_from_id.city + ', ' \
                        + self.station_from_id.name + '-' \
                        + self.station_to_id.city + ', ' \
                        + self.station_to_id.name
