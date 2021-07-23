from odoo import http

class UniversityController(http.Controller):
    @http.route('/university/controller/', auth='user')
    def index(self, **kw):
        students=http.request.env['university.student'].search(['|',('f_name','=','farid'),('f_name','=','Siwar')])
        returnsentence='<h1>Les etudiants sont : </h1>\n<ol>'
        for s in students:
            returnsentence+='<li>'+s['f_name']+'  '+s['l_name'] + ' de class '+s['classroom_id']['name']+'</li>'
        returnsentence += '</ol>'
        print(returnsentence)
        return returnsentence

#     @http.route('/university/university/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('university.listing', {
#             'root': '/university/university',
#             'objects': http.request.env['university.university'].search([]),
#         })

#     @http.route('/university/university/objects/<model("university.university"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('university.object', {
#             'object': obj
#         })


class fils(UniversityController):
    @http.route('/fils',auth='public')
    def filshandler(self, **kw):
        print('Hi from fils');
        return super(fils, self).index();