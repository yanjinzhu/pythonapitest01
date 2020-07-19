import unittest
import logging
import json
from config import InitLog

def assertapi(self,status, result, msg, response):
    self.assertEqual(status, response.status_code)
    self.assertEqual(result, response.json().get("result"))
    self.assertIn(msg, response.json().get("msg"))


def read_data_login():
    jsonfile = "./data/logindata.json"
    with open(jsonfile,encoding="utf-8") as f:
        listdata = json.load(f)
        data_list = []
        for jsondata in listdata:
            case = jsondata.get("case")
            username = jsondata.get("username")
            password = jsondata.get("password")
            msg = jsondata.get("msg")
            result = jsondata.get("result")
            status = jsondata.get("status")

            data_list.append((case,username,password,msg,result,status))
    return data_list

def read_data_addgoods():
    jsonfile = "./data/addgooddata.json"
    with open(jsonfile,encoding="utf-8") as f:
        listdata = json.load(f)
        data_list = []
        for jsondata in listdata:
            case = jsondata.get("case")
            goods_name = jsondata.get("goods_name")
            category_id = jsondata.get("category_id")
            status = jsondata.get("status")
            result = jsondata.get("result")
            msg = jsondata.get("msg")
            data_list.append((case,goods_name,category_id,status,result,msg))
    return data_list
if __name__ == '__main__':
    a = read_data_addgoods()
    logging.info("组装后的数据：{}".format(a))