from datetime import date
from odoo.addons.bus_station.tests.common import TestCommon
from odoo.tests import tagged


@tagged('post_install', '-at_install', 'bus_station')
class TestBusTechInspection(TestCommon):

    def test_compute_next_technical_inspection_date(self):
        bus = self.bus_demo
        bus._compute_next_technical_inspection_date()
        self.assertEqual(bus.next_technical_inspection_date, date(2022, 1, 1))
