from flask import Flask, render_template
import requests


class Post:

    def __init__(self):
        self.url_Qs = 'https://api.npoint.io/57ad038392ed0f077f03'

    def get_q(self):
        response = requests.get(self.url_Qs)
        data = response.json()

        return data