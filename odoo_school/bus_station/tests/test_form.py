from odoo.addons.bus_station.tests.common import TestCommon
from odoo.tests.common import Form
from odoo.tests import tagged


@tagged('post_install', '-at_install', 'bus_station')
class TestBusStationForm(TestCommon):

    def test_create_bus_station(self):
        """Test creating a new bus station"""

        bus_station = Form(self.bus_station_demo)
        self.assertEqual(bus_station.name, 'Test Station')
        self.assertEqual(bus_station.city, 'Test City')
