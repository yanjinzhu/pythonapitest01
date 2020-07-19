import requests
from config import HOST,HEADERS

session = requests.session()

def loginapi(username,password):
    url = HOST + "/login"
    data = {"username":username,"password":password}

    response = session.post(url, json = data, headers = HEADERS)

    # cookie = response.headers.get("set-cookie")
    # HEADERS["cookie"] = cookie
    return response
