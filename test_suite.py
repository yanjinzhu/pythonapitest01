import unittest
from script.test_login import LogninTest
from tools.HTMLTestRunner import HTMLTestRunner
import time
from script.test_addgoods import AddGood
from config import HEADERS


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(LogninTest))
suite.addTest(unittest.makeSuite(AddGood))
report_file = "./report/test-{}.html".format(time.strftime("%Y%m%d %H%M%S"))

with open(report_file,"wb") as f:
    runner = HTMLTestRunner(f, title="宇泽购物流程－测试报告",description="v0.1")
    runner.run(suite)

print(HEADERS)