import http.client
import urllib
import os
from dotenv import load_dotenv

load_dotenv()

APP_TOKEN = os.getenv("APP_TOKEN")


def push_message(message: str, user_token) -> None:
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
                 urllib.parse.urlencode({
                     "token": APP_TOKEN,
                     "user": user_token,
                     "message": message,
                 }), {"Content-type": "application/x-www-form-urlencoded"})
    return conn.getresponse().status


print(push_message("message", 'u6by429m334zkap63ixfvett2as3sv'))
