import requests

def safe_post(url, payload):
    try:
        res = requests.post(url, json=payload)
        try:
            return res.json()
        except requests.exceptions.JSONDecodeError:
            return f"Non-JSON response:\n{res.text}"
    except Exception as e:
        return f"Request failed: {e}"

def safe_get(url):
    try:
        res = requests.get(url)
        try:
            return res.json()
        except requests.exceptions.JSONDecodeError:
            return f"Non-JSON response:\n{res.text}"
    except Exception as e:
        return f"Request failed: {e}"

BASE = "https://blackbox-interface.vercel.app/api"

# 1. /data
print("\nTesting POST /data")
for val in ["hello", "123", "racecar", "OpenAI"]:
    url = f"{BASE}/data"
    print(f"Input: {val} =>", safe_post(url, {"data": val}))

# 2. /time
print("\nTesting GET /time")
url = f"{BASE}/time"
print("Response:", safe_get(url))

# 3. /fizzbuzz
print("\nTesting POST /fizzbuzz")
for val in ["3", "5", "15", "7", "hello", ["Fizz", "Buzz"]]:
    url = f"{BASE}/fizzbuzz"
    print(f"Input: {val} =>", safe_post(url, {"data": val}))

# 4. /zap
print("\nTesting POST /zap")
for val in ["zap", "OpenAI", "boom123", "ZAPZAP"]:
    url = f"{BASE}/zap"
    print(f"Input: {val} =>", safe_post(url, {"data": val}))

# 5. /alpha
print("\nTesting POST /alpha")
for val in ["abc", "abc123", "123", "!@#OpenAI", "xyz"]:
    url = f"{BASE}/alpha"
    print(f"Input: {val} =>", safe_post(url, {"data": val}))

# 6. /glitch
print("\nTesting POST /glitch")
for val in ["glitch", "OpenAI", "123", "abcdef"]:
    url = f"{BASE}/glitch"
    print(f"Input: {val} =>", safe_post(url, {"data": val}))
