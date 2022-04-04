from flask_restx import Namespace, Resource
from flask import render_template, redirect, url_for, make_response, request, session, flash
from controll.cal_model import Calorie_model
from controll.user_info_model import user_info_table


mainpage = Namespace('mainpage')


@mainpage.route('/')
class Mainpage(Resource):
    def get(self):
        if 'token' in session:
            try:
                user_data = request.cookies.get('user_email').split('%40')
                user_email = user_data[0] + '@' + user_data[1]
                user = user_info_table.search(user_email)
                sex = user[-1].sex
                age = user[-1].age
                result = Calorie_model.get(sex, age)
            except:
                result = [0] * 20
            print(result)

            print(session)

            return make_response(render_template('mainpage.html', cal_data=result))
        else:
            return make_response(render_template('login.html'))


@mainpage.route('/login')
class Login(Resource):
    def get(self):
        if 'token' in session:
            return make_response(redirect(url_for('mainpage_mainpage')))
        else:
            return make_response(render_template('login.html'))


@ mainpage.route('/register')
class Register(Resource):
    def get(self):
        return make_response(render_template('register.html'))


@ mainpage.route('/logout')
class Register(Resource):
    def get(self):
        if 'token' in session:
            session.pop('token')
            return make_response(redirect(url_for('mainpage_login')))
        else:
            return make_response(redirect(url_for('mainpage_login')))


@ mainpage.route('/info')
class Register(Resource):
    def get(self):
        return make_response(render_template('info.html'))


@ mainpage.route('/fig')
class Register(Resource):
    def get(self):
        return make_response(render_template('login.html'))


@ mainpage.route('/tlqkf')
class Register(Resource):
    def get(self):
        return make_response(render_template('upload.html'))


@ mainpage.route('/uploader')
class Register(Resource):
    def post(self):

        f = request.files['file']
        print('hi')

        f.save('../static/' + f.filename)

        return 'file uploaded successfully'


@ mainpage.route('/test')
class Register(Resource):
    def get(self):
        data = request.cookies.get('token')
        session['token'] = data
        return make_response(redirect(url_for('mainpage_mainpage')))
