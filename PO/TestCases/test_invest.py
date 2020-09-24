import unittest
from selenium import webdriver
import ddt

from PO.PageObjects.login_page import LoginPage
from PO.PageObjects.home_page import HomePage
from PO.PageObjects.bid_page import BidPage
from PO.PageObjects.user_page import UserPage

from PO.TestDatas import Global_Datas as GD
from PO.TestDatas import login_datas as lds


class TestInvest(unittest.TestCase):

    def setUp(self) -> None:
        # 访问登陆页面
        self.driver = webdriver.Chrome()
        self.driver.get(GD.login_url)
        self.driver.maximize_window()
        # 登陆 - 使用公共投资人帐号
        LoginPage(self.driver).login(*GD.user_invest)

    def tearDown(self) -> None:
        self.driver.quit()

    # 正向场景  - 投资成功 - 投资2000块 - 用户余额/标余额是否发生变化
    def test_invest_success(self):
        """
        :return:
        """
        # 1、首页 - 选第一个标
        HomePage(self.driver).click_first_bid()
        bp = BidPage(self.driver)
        # 11、标页面 - 获取用户余额
        user_money_before_invest = bp.get_user_money()
        # 111、标页面 - 获取标的余额
        bid_money_before_invest = bp.get_bid_money()
        # 2、标页面 - 输入金额2000，点投标
        bp.invest(2000)
        # 3、标页面 - 在投标成功的弹出框里，点击查看并激活按钮
        bp.click_active_button_in_success_popup()

        # 1、钱有没有少2000 - 灵活可用
        # 4）个人页面 - 获取用户余额
        user_money_after_invest = UserPage(self.driver).get_user_money()
        # 断言：投前额 - 投后额 == 2000   # int(float(user_money_before_invest) - float(user_money_after_invest)) == 2000
        self.assertEqual(int(float(user_money_before_invest) - float(user_money_after_invest)),2000)
        #
        # 2、标的可投余额少2000
        # 5）个人页面 - 回退到上一页；刷新
        self.driver.back()
        self.driver.refresh()
        # 6）标页面 - 获取标的余额
        bid_money_after_invest = bp.get_bid_money()
        # 断言：(投前标额 - 投后标额) * 10000 == 2000
        # int(float(bid_money_before_invest) - float(bid_money_after_invest))*10000 == 2000
        self.assertEqual(int(float(bid_money_before_invest) - float(bid_money_after_invest)),2000)


# 投资失败：金额输入框的格式 不正确/数据不符合要求
# 投资失败：投资的钱 比你自己余额  还要高  你想投10000，但是你只有2000块。 --- 你的钱不够
#             额外 准备一个帐号，10000块钱。20000块。
#          你要投50000块，但是标只有20000可以投 -    ---- 标的钱不够
#          有一个帐户：>50000块    准备一个标，只有20000块钱余额

#   你有100万，标可投100万，你要投500万？？ 先判断标的余额不够，还是你的余额不够？

