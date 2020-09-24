from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PO.PageLocators.bid_page_locs import BidPageLocs as locs
from PO.Common.basepage import Basepage

class BidPage(Basepage):

    # 11、标页面 - 获取用户余额
    def get_user_money(self):
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locs.money_input))
        return self.get_ele_attribute(locs.money_input,"data-amount","标页面 - 获取用户余额")

    # 111、标页面 - 获取标的余额
    def get_bid_money(self):
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locs.bid_money_text))
        return self.get_ele_text(locs.bid_money_text,"标页面 - 获取标的余额")

    # 2、标页面 - 输入金额2000，点投标
    def invest(self,invest_money):
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locs.money_input))
        self.input_text(locs.money_input,invest_money,"标页面 - 输入投资金额")
        self.click_element(locs.invest_button,"表页面-点击投资按钮")

    # 3、标页面 - 在投标成功的弹出框里，点击查看并激活按钮
    def click_active_button_in_success_popup(self):
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locs.active_button_on_successPop))
        self.click_element(locs.active_button_on_successPop,"标页面 - 在投标成功的弹出框里，点击查看并激活按钮")