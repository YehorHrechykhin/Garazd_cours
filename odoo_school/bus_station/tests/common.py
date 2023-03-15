from odoo.tests.common import TransactionCase


class TestCommon(TransactionCase):

    def setUp(self):
        super(TestCommon, self).setUp()
        self.group_bus_station_user = self.env.ref(
            'bus_station.group_bus_station_user')
        self.group_bus_station_admin = self.env.ref(
            'bus_station.group_bus_station_admin')
        self.bus_station_user = self.env['res.users'].create({
            'name': 'Test User',
            'login': 'test_user',
            'groups_id': [(4, self.env.ref('base.group_user').id),
                          (4, self.group_bus_station_user.id)],
        })
        self.bus_station_admin = self.env['res.users'].create({
            'name': 'Test Admin',
            'login': 'test_admin',
            'groups_id': [(4, self.env.ref('base.group_user').id),
                          (4, self.group_bus_station_admin.id)],
        })
        self.bus_station_demo = self.env['bus.station.station'].create({
            'name': 'Test Station',
            'city': 'Test City'})
