from odoo import models, fields, api

class groups(models.Model):

 _inherit = 'university.student'

 field_1 = fields.Char(required=True,string="Field One")
 field_2 = fields.Boolean(default=True,string="Field Two")