# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityStudent(models.Model):
    _name = 'university.student'
    _inherit = 'mail.thread'

    f_name = fields.Char(string='Fist name',required=True,help='This is the First name ',index=True)
    l_name = fields.Char('Last name')
    sexe = fields.Selection([('male', 'Male'), ('female', 'Female')])
    identity_card = fields.Char('Identity card')
    address = fields.Text('Address')
    birthday = fields.Date('Birthday')
    registration_date = fields.Datetime('Registration Date')
    email = fields.Char()
    phone = fields.Char()
    lucky_number=fields.Float(string='Lucky number',compute='lucky_func')
    classmates=fields.One2many(related='classroom_id.student_ids')
    state = fields.Selection([('s1','mpi'),('s2','2eme'),('s3','3eme'),('s4','4eme'),('s5','5eme')])
    depatment_id=fields.Many2one(comodel_name='university.depatment')
    classroom_id=fields.Many2one(comodel_name='university.classroom')
    subject_ids = fields.Many2many(comodel_name='university.subject',
                                   relation='student_subject',
                                   column1='f_name',
                                   column2='name')

    def lucky_func(self):
        self.lucky_number=len(self.subject_ids)*len(self.f_name)*(self.l_name.count(self.f_name[0])+0.5)

    def name_get(self):
        result = []
        for student in self:
            alias = "[" + student.classroom_id.name + "] " + student.f_name + " " + student.l_name
            result.append((student.id,alias))
        return result


    def next_state(self):
        if self.state=='s1':
            return self.write({'state':'s2'})
        elif self.state=='s2':
            return self.write({'state':'s3'})
        elif self.state=='s3':
            return self.write({'state':'s4'})
        elif self.state=='s4':
            return self.write({'state':'s5'})
        else:
            return {'warning': {'title': 'Warning',
                                'message': 'Where are you going , you finished your study...'}}

    @api.onchange('subject_ids')
    def subject_max(self):
        if len(self.subject_ids) >= 3:
            return {'warning': {'title': 'Warning',
                                'message': 'You shouldn\'t add more than 2 Subjects'}}

    # @api.constrains('registration_date','birthday')
    # def date_error(self):
    #     if(self.registration_date <= self.birthday):
    #         raise ValueError('Registration date can not be before Birthday!!!')
