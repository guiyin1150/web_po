# from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PO.PageLocators.login_page_locs import LoginPageLocs as loc
from PO.Common.basepage import Basepage

class LoginPage(Basepage):

    # 登陆  - 元素操作 - 不知道用例在什么情况下会调用我？？
    def login(self,username,passwd):
        self.input_text(loc.user_input,username,"登陆页面_输入用户名")
        self.input_text(loc.passwd_input,passwd,"登陆页面_输入密码")
        self.click_element(loc.login_button,"登陆页面_点击登陆按钮")

    # 获取登陆区域的提示信息
    def get_msg_from_login_form(self):
        self.wait_ele_visible(loc.msg_from_login_form,"登陆页面_等待登陆表单的错误提示元素")
        eles =  self.get_elements(loc.msg_from_login_form,"登陆页面_获取登陆表单的错误提示元素们")
        if len(eles) == 1:
            return eles[0].text
        elif len(eles) > 1:
            text_list = []
            for el in eles:
                text_list.append(el.text)
            return text_list

