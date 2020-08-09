import base64
import json
from pprint import pprint

import requests


def send_request(method, url, data):
    resp = requests.request(method, url, data=data, verify=False)
    return resp.status_code, resp.text, resp.headers


resp = send_request('GET', 'http://127.0.0.1:5000/image', '')
print(resp)
print(resp[0])
pprint(json.loads(resp[1]))

file_name = 'photo_2020-04-27_21-19-07.jpg'
resp = send_request('DELETE', 'http://127.0.0.1:5000/image', file_name)
print(resp[0])
pprint(resp[1])

file_name = '/var/projects/visionlabs/images/QRCODE_https___bitfinex.com__refcode=s-bG_88d.jpeg'
with open(file_name, "rb") as image_file:
    b = base64.standard_b64encode(image_file.read())
resp = send_request('POST', 'http://127.0.0.1:5000/image', b)
print(resp[0])
pprint(resp[1])
