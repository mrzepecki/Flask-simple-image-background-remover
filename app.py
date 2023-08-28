import os
import tempfile
from flask import Flask, request, send_file
from rembg import remove
from PIL import Image

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/v1/remove-background", methods=['POST'])
def remove_background():
    file = request.files['file']
    if file and allowed_file(file.filename):
        input_image = Image.open(file)

        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_output_file:
            output_image = remove(input_image)
            output_image.save(temp_output_file, format="PNG")

            temp_output_file.seek(0)
            response = send_file(temp_output_file.name, mimetype='image/png')

        os.remove(temp_output_file.name)
        return response