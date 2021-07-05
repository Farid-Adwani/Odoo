# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityProfessor(models.Model):
    _name = 'university.professor'
    _rec_name="f_name"

    f_name = fields.Char('Fist name')
    l_name = fields.Char('Last name')
    sexe = fields.Selection([('male','Male'), ('female','Female')])
    identity_card = fields.Char('Identity card')
    address = fields.Text('Address')
    birthday = fields.Date('Birthday')
    start_date = fields.Datetime('Start date')
    email = fields.Char()
    phone = fields.Char()
    subject_id=fields.Many2one(comodel_name='university.subject')
    depatment_id=fields.Many2one(comodel_name='university.depatment')
    classroom_ids = fields.Many2many(comodel_name='university.classroom',
                                     relation='professor_classroom',
                                     column1='f_name',
                                     column2='name')

    def name_get(self):
        result=[]
        for professor in self:
            alias="["+professor.depatment_id.name+"] "+professor.f_name+" "+professor.l_name
            result.append((professor.id,alias))
        return result

