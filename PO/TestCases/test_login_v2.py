import unittest
from selenium import webdriver
import ddt

from PO.PageObjects.login_page import LoginPage
from PO.PageObjects.home_page import HomePage

@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 访问登陆页面
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://120.78.128.25:8765/Index/login.html")
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def setUp(self) -> None:
        self.driver.refresh()

    def test_login_02_success(self):
        # 步骤 # 1、登陆页面 - 登陆操作    用户名/密码
        LoginPage(self.driver).login("18684720553","python")
        # 断言  # 2、首页 - 获取元素是否存在
        self.assertTrue(HomePage(self.driver).get_element_exists())

    cases = [
        {"user":"","passwd":"python","check":"请输入手机号"},
        {"user": "18684720553", "passwd": "", "check": "请输入密码"},
        {"user": "1868472055", "passwd": "python", "check": "请输入正确的手机号"}
    ]

    @ddt.data(*cases)
    def test_login_01_failed_wrong_format(self,case):
        # 步骤 # 1、登陆页面 - 登陆操作   用户名/密码/期望数据
        lp = LoginPage(self.driver)
        lp.login(case["user"], case["passwd"])
        # 断言  # 2、登陆页面  - 获取错误的提示信息
        self.assertEqual(lp.get_msg_from_login_form(),case["check"])

