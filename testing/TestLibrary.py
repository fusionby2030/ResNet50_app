import requests
import re

class TestLibrary(object):
    """
    Test Library for testing NN logic

    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    def __init__(self, ip='http://127.0.0.1:5000'):
        self.ip_address = ip
        self.query = {}

    def send_img(self, image_path):
        url = '{}/predict'.format(self.ip_address)
        image = open(image_path, "rb").read()
        payload = {"image": image}
        r = requests.post(url, files=payload).json()
        return r["success"]
    def post_img(self, image_path):
        url = '{}/predict'.format(self.ip_address)
        image = open(image_path, "rb").read()
        payload = {"image": image}
        r = requests.post(url, files=payload).json()
        return r
    def image_analysis(self, image_path):
        url = '{}/predict'.format(self.ip_address)
        image = open(image_path, "rb").read()
        payload = {"image": image}
        r = requests.post(url, files=payload).json()
        best_guess = r['predictions'][0]
        name = best_guess['label']
        return name

#c.send_img('image')
