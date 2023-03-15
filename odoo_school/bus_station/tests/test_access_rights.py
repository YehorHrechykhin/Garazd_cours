from odoo.addons.bus_station.tests.common import TestCommon
from odoo.tests import tagged


@tagged('post_install', '-at_install', 'bus_station', 'access')
class TestAccessRights(TestCommon):

    def test_01_bus_station_user_access_rights(self):
        self.env = self.env(user=self.bus_station_user.id)

        # Check that user can read stations
        stations = self.env['bus.station.station'].search([])
        self.assertTrue(stations)

    def test_02_bus_station_admin_access_rights(self):
        self.env = self.env(user=self.bus_station_admin.id)

        # Check that admin can read, create, and edit stations
        stations = self.env['bus.station.station'].search([])
        self.assertTrue(stations)
        new_station = self.env['bus.station.station'].create({
            'name': 'New Station',
            'city': 'New City'})
        new_station.write({'name': 'Updated Station'})
