import random

from odoo import http
from odoo.http import request
class studentController(http.Controller):
    @http.route('/university/student/',type='json',csrf=False, auth='none')
    def index(self,**kw):
        students=http.request.env['university.student'].search([])

        student_list=[]
        for rec in students:
            student=http.request.env['university.student'].browse(rec.id)
            student_data={
                "id":student.id,
                "f_name": student.f_name,
                "l_name": student.l_name,
                "classoom name": student.classroom_id.name,
                "field1": student.field_1,
            }
            student_list.append(student_data)
        data = {
            "head": "200",
            "message": "success",
            "len":len(students),
            "response": student_list,
        }
        return data

    @http.route('/university/add_student',type='json',auth='none',csrf=False)
    def add(self,f_name,l_name,field_1,message):
        classrooms = http.request.env['university.classroom'].search([])
        classroom_id=random.choice(classrooms).id
        new_rec=http.request.env['university.student'].create({'f_name':f_name,'l_name':l_name,'field_1':field_1,'classroom_id':classroom_id})
        output=message+str(new_rec.id)
        return output

    @http.route('/university/delete_student',type='json',auth='none')
    def delete(self):
        students=http.request.env['university.student'].search([])
        if (len(students)>0):
            id = students[len(students) - 1].id
            res = http.request.env['university.student'].browse(id).unlink()
            if (res == True):
                return {"message": 'Student with id ' + str(id) + ' is deleted with success',
                        "len": len(http.request.env['university.student'].search([]))}
            else:
                return {"message": 'Operation failed to felete student with id ' + str(id),
                        "len": len(http.request.env['university.student'].search([]))}
        else:
            return {"message":'No Student created yet',
                        "len": len(students)}


    @http.route('/university/update_student', type='json', auth='none', csrf=False)
    def add(self, f_name, l_name,data):
        student=http.request.env['university.student'].search([('f_name','=',f_name),('l_name','=',l_name)])
        print(student)
        if(len(student)>0):
            res = student.write(data)
            if res == True:
                return {"message": 'Student ' + f_name +' '+l_name+' is updated with success '}
            else:
                return {"message": 'updating Student '+ f_name +' '+l_name+' failed '}
        else:
            return {"message": 'no existing Student with name ' + f_name +' '+l_name}


