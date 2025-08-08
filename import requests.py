import requests

API_KEY = "AIzaSyB_PIvlcsx9HT9dRKFkjYp1HrOdVqJXvEc"
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent?key=" + API_KEY

headers = {
    "Content-Type": "application/json"
}

data = {
    "contents": [
        {
            "parts": [
                {"text": "Write a short story about a robot who learns to paint."}
            ]
        }
    ]
}

response = requests.post(url, headers=headers, json=data)

print(response.json())