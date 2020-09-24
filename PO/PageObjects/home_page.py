from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PO.PageLocators.home_page_locs import HomePageLocs as locs

class HomePage:

    def __init__(self,driver:WebDriver):
        # 初始化driver
        self.driver = driver

    # 退出元素是否存的状态  如果存在则返回True,不存在返回False??
    def get_element_exists(self):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locs.exit_loc))
        except:
            return False
        else:
            return True

    # 点击第一个标投资
    def click_first_bid(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(locs.bid_button))
        self.driver.find_element(*locs.bid_button).click()