import http.client
import urllib
APP_TOKEN: str = "aszwjnjeffy3cdcisqb6anm9eusrhh"
USER_KEY: str = "uoghnwn4vgn6tgnqm5oo6m4ckjwppc"


def push_message(message: str) -> None:
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
                 urllib.parse.urlencode({
                     "token": APP_TOKEN,
                     "user": USER_KEY,
                     "message": message,
                 }), {"Content-type": "application/x-www-form-urlencoded"})
    return conn.getresponse().status


# def main() -> None:
#     while True:
#         print(push_message(input()))


# if __name__ == "__main__":
#     main()
