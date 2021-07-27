# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Inheritance(models.Model):
    _inherit='crm.lead'

    image=fields.Binary('Image ooo')
    esm=fields.Char('Esm')

