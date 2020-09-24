import unittest
from selenium import webdriver
import ddt

from PO.PageObjects.login_page import LoginPage
from PO.PageObjects.home_page import HomePage

from PO.TestDatas import Global_Datas as GD
from PO.TestDatas import login_datas as lds

@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        # 访问登陆页面
        # logging.info("******************用例前置：打开谷歌浏览器，并访问前程贷登陆页面*********************")
        self.driver = webdriver.Chrome()
        self.driver.get(GD.login_url)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()


    def test_login_success(self):
        # 步骤 # 1、登陆页面 - 登陆操作    用户名/密码
        # logging.info("******************登陆用例-正常场景-登陆成功*********************")
        LoginPage(self.driver).login(*lds.success)
        # 断言  # 2、首页 - 获取元素是否存在
        self.assertTrue(HomePage(self.driver).get_element_exists())


    @ddt.data(*lds.cases)
    def test_login_failed_wrong_format(self,case):
        # 步骤 # 1、登陆页面 - 登陆操作   用户名/密码/期望数据
        lp = LoginPage(self.driver)
        lp.login(case["user"], case["passwd"])
        # 断言  # 2、登陆页面  - 获取错误的提示信息
        self.assertEqual(lp.get_msg_from_login_form(),case["check"])

