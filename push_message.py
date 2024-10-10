import http.client
import urllib
import os
from dotenv import load_dotenv

load_dotenv()

APP_TOKEN = os.getenv("APP_TOKEN")


def push_message(message: str, user_key) -> None:
    """sends a notification to a mobile phone using pushover and returns if it succeeded

    Args:
        message (str): the message that is getting pushed
        user_key (_type_): user key is what identifies which user should get the message

    Returns:
        int: if the messaged succeeded in sending or not 
    """
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
                 urllib.parse.urlencode({
                     "token": APP_TOKEN,
                     "user": user_key,
                     "message": message,
                 }), {"Content-type": "application/x-www-form-urlencoded"})
    return conn.getresponse().status
