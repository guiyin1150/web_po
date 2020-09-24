from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PO.PageLocators.user_page_locs import UserPageLocs as locs


class UserPage:

    def __init__(self, driver: WebDriver):
        # 初始化driver
        self.driver = driver

    # 11、获取用户余额
    def get_user_money(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(locs.user_leftMoney))
        return self.driver.find_element(*locs.user_leftMoney).text.strip("元")