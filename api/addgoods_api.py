import requests
from config import HOST,HEADERS
from api.login_api import session

def addgood(goods_name,category_id):
    url = HOST + "/addgoods"
    data = {
        "goods_name": goods_name,
        "category_id": category_id,
        "main_image": "dfsfsfsafs",
        "price": "1680",
        "quantity": 999,
        "detail": "dffdsfsfsf",
        "status": 1
    }
    response = session.post(url, json=data, headers = HEADERS)
    return response