import unittest
from api.addgoods_api import addgood
import logging
from config import InitLog
from uitls import assertapi
from parameterized import parameterized
from uitls import read_data_addgoods

class AddGood(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass

    @parameterized.expand(read_data_addgoods)
    def testaddgood(self,case,goods_name,category_id,status,result,msg):
        response = addgood("goods_name",category_id)
        logging.info("{0}：{1}".format(case,response.json()))

        assertapi(self,status,result,msg,response)