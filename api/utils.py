from django.conf import settings
import requests


def make_api_call(title):
    API_KEY = getattr(settings, 'API_KEY', '')
    url = "http://www.omdbapi.com/?t={}&apikey={}".format(title, API_KEY)
    return {k.lower(): v for k, v in requests.get(url).json().items()}
