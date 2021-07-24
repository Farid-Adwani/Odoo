import  odoorpc

odoo=odoorpc.ODOO('localhost',port=8069)
print('la liste des bases de données est :')
print(odoo.db.list());
odoo.login('farid','faridadwani@insat.u-carthage.tn','farid');
user=odoo.env.user;
print(user.name)
print(user.id)
print(user.create_date)
print(user.company_id.name)

user_data=odoo.execute('res.users','read',1)
for key in user_data[0]:
    print(key,' : ',user_data[0][key])

student_model=odoo.env['university.student']

student_ids=student_model.search([]);
for id in student_ids:
    print(id)
    print(odoo.execute('university.student','read',id))


# for student_id in student_model.search(['id','=',7]):
# students=student_model.browse(student_ids)
    # student=student_model.browse(id)
    # print(student['f_name'])

user.='faridadwani';



