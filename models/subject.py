# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversitySubject(models.Model):
    _name = 'university.subject'

    name = fields.Char()
    code = fields.Char()
    statut = fields.Selection([('one','1'),('Two','2'),('Three','3')])
    depatment_id=fields.Many2one(comodel_name='university.depatment')
    student_ids=fields.Many2many(comodel_name='university.student',
                                 relation='subject_student',
                                 column1='name',
                                 column2='f_name')
    professor_ids=fields.One2many(comodel_name='university.professor', inverse_name='subject_id')
