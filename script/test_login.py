import requests,logging,unittest
from api.login_api import loginapi
from uitls import assertapi
from parameterized import parameterized
from uitls import read_data_login
import pymysql


class LogninTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass

    @parameterized.expand(read_data_login)
    def testlogin(self,case, username,password,msg,result,status):
        response = loginapi(username,password)
        assertapi(self,status, result, msg, response)
        logging.info("{0}：{1}".format(case,response.json()))