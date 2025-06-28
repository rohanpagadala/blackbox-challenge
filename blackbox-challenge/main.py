import requests
import json

BASE_URL = "https://blackbox-interface.vercel.app"

def post_data(data):
    url = f"{BASE_URL}/data"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=json.dumps({"data": data}))
    try:
        return response.json()
    except json.JSONDecodeError:
        return response.text

def get_time():
    url = f"{BASE_URL}/time"
    response = requests.get(url)
    try:
        return response.json()
    except json.JSONDecodeError:
        return response.text

def post_fizzbuzz(number):
    url = f"{BASE_URL}/fizzbuzz"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=json.dumps({"number": number}))
    try:
        return response.json()
    except json.JSONDecodeError:
        return response.text

def post_zap(input_data):
    url = f"{BASE_URL}/zap"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=json.dumps({"input": input_data}))
    try:
        return response.json()
    except json.JSONDecodeError:
        return response.text

def post_alpha(text):
    url = f"{BASE_URL}/alpha"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=json.dumps({"text": text}))
    try:
        return response.json()
    except json.JSONDecodeError:
        return response.text

def post_glitch(payload):
    url = f"{BASE_URL}/glitch"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    try:
        return response.json()
    except json.JSONDecodeError:
        return response.text

if __name__ == "__main__":
    print("Testing POST /data with 'hello'")
    print(post_data("hello"))

    print("\nTesting GET /time")
    print(get_time())

    print("\nTesting POST /fizzbuzz with 15")
    print(post_fizzbuzz(15))

    print("\nTesting POST /zap with 'test' ")
    print(post_zap("test"))

    print("\nTesting POST /alpha with 'abc' ")
    print(post_alpha("abc"))

    print("\nTesting POST /glitch with {'key': 'value'} ")
    print(post_glitch({"key": "value"}))

