import base64
import binascii
from datetime import datetime as dt
import os
import uuid

from api import app
from flask import jsonify
from flask import request
from flask import send_file

from config import IMAGE_DIR


def get_file_info(path, file_name):
    file_size = os.path.getsize(path)
    last_access_timestamp = os.path.getmtime(path)
    last_access_utc = dt.utcfromtimestamp(last_access_timestamp).strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    return dict(
        file_name=file_name,
        file_size=file_size,
        last_access=last_access_utc,
    )


@app.route('/images/<file_name>')
def get_image(file_name):
    if not file_name:
        return 'image name is not specified', 400

    try:
        path = os.path.join(IMAGE_DIR, file_name)
        return send_file(path, mimetype='image/jpg')
    except FileNotFoundError as e:
        return 'image not found', 404
    except Exception as e:
        return 'unexpected error', 500


@app.route('/image', methods=['GET'])
def get_images():
    try:
        image_list = []
        for file_name in os.listdir(IMAGE_DIR):
            path = os.path.join(IMAGE_DIR, file_name)
            if os.path.isdir(path):
                continue
            file_info_dict = get_file_info(path, file_name)
            image_list.append(file_info_dict)
        return jsonify(image_list)
    except Exception as e:
        return 'unexpected error', 500


@app.route('/image', methods=['DELETE'])
def delete_image():
    file_name = request.get_data(as_text=True)
    if not file_name:
        return 'image name is not specified', 400

    try:
        os.remove(os.path.join(IMAGE_DIR, file_name))
        return 'ok', 200
    except FileNotFoundError as e:
        return 'ok', 200
    except Exception as e:
        return 'unexpected error', 500


@app.route('/image', methods=['POST'])
def create_image():
    image_data = request.get_data()
    if not image_data:
        return 'image data not found', 400

    try:
        file_name = f'{str(uuid.uuid4())}.jpg'
        path = os.path.join(IMAGE_DIR, file_name)
        with open(path, "wb") as image_file:
            image_file.write(base64.b64decode(image_data, validate=True))
        file_info_dict = get_file_info(path, file_name)
        return jsonify(file_info_dict)
    except binascii.Error as e:
        return 'non-base64 digit found', 400
    except Exception as e:
        return 'unexpected error', 500
