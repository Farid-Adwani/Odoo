# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Universitydepatment(models.Model):
    _name = 'university.depatment'
    name = fields.Char()
    code = fields.Char()
    subject_ids=fields.One2many(comodel_name='university.subject', inverse_name='depatment_id')
    student_ids=fields.One2many(comodel_name='university.student', inverse_name='depatment_id')
    professor_ids=fields.One2many(comodel_name='university.professor', inverse_name='depatment_id')

