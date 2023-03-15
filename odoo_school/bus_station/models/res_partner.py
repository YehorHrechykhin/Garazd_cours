from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Bus Station Employees'

    is_driver = fields.Boolean()
    driver_license = fields.Char()
    route_id = fields.Many2one(comodel_name='bus.station.route')
