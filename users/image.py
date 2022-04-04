from flask_restx import Namespace, Resource
from flask import render_template, redirect, url_for, make_response, request, session, flash
from controll.image_model import ImageTable
from PIL import Image
import io
import torch
import io
import argparse


image = Namespace('image')


@ image.route('/')
class Register(Resource):
    def post(self):

        parser = argparse.ArgumentParser(
            description="Flask app exposing yolov5 models")
        parser.add_argument("--port", default=5000,
                            type=int, help="port number")
        args = parser.parse_args()

        model = torch.hub.load(
            "web_project/yolov5_models/yolov5", "custom", path='web_project/yolov5_models/AFv1.pt', source='local', force_reload=True)
        # model.names =  ['쌀밥', '된장찌개', '족발', '돈가스', '배추김치']
        # force_reload = recache latest code

        model.eval()

        d = request.files['image']

        data = request.form['user_email']
        user_email = list(filter(lambda x: 'user_email' in x,
                                 data.split(';')))[0].split('=')[1]

        img_bytes = d.read()

        img = Image.open(io.BytesIO(img_bytes))
        results = model(img, size=640)
        results.render()  # updates results.imgs with boxes and labels
        for img in results.imgs:
            img_base64 = Image.fromarray(img)
            filename = d.filename.split('.jpg')
            img_base64.save(
                f"web_project/static/{filename[0]}.jpeg", format="JPEG")

        data = results.pandas().xyxy[0].to_json(orient="records")

        ImageTable.add_image(
            user_email, f'{filename[0]}.jpeg')
        result = ImageTable.get_image(user_email)[-1].image
        print('test')

        return result
