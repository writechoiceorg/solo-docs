import requests
import json
import base64
from dotenv import load_dotenv
import os

load_dotenv()


def encode_base64(input_string):
    input_bytes = input_string.encode("utf-8")
    encoded_bytes = base64.b64encode(input_bytes)
    encoded_string = encoded_bytes.decode("utf-8")

    return encoded_string


def get_categories():
    url = "https://dash.readme.com/api/v1/categories"
    key = os.getenv("README_API_KEY")
    encoded = encode_base64(key)

    headers = {
        "x-readme-version": "v1.0",
        "authorization": f"Basic {encoded}Og==",
    }

    return requests.get(url, headers=headers)


def json_formatter():
    json_object = json.loads(get_categories().text)

    return json.dumps(json_object, indent=2)


print(json_formatter())
