from flask_restx import Namespace, Resource
from flask import render_template, redirect, url_for, make_response, request, session, flash
from controll.image_model import ImageTable


image = Namespace('image')


@ image.route('/')
class Register(Resource):
    def post(self):

        d = request.files['image']

        data = request.form['user_email']
        user_email = list(filter(lambda x: 'user_email' in x,
                                 data.split(';')))[0].split('=')[1]

        d.save('backend/static/' + d.filename)

        ImageTable.add_image(
            user_email, d.filename)
        result = ImageTable.get_image(user_email)[-1].image

        return result
