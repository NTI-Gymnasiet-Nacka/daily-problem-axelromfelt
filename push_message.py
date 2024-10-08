import http.client
import urllib
import os
from dotenv import load_dotenv

load_dotenv()
os.path.dirname(os.path.abspath(__file__))

APP_TOKEN = os.environ.get("APP_TOKEN")
USER_KEY = os.environ.get("USER_KEY")


def push_message(message: str) -> None:
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
                 urllib.parse.urlencode({
                     "token": APP_TOKEN,
                     "user": USER_KEY,
                     "message": message,
                 }), {"Content-type": "application/x-www-form-urlencoded"})
    return conn.getresponse().status


def main() -> None:
    while True:
        print(push_message(input()))


if __name__ == "__main__":
    main()
