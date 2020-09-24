"""
@File    : user_page_loc
@Time    : 2019/12/9
@Author  : liyuan
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""

from selenium.webdriver.common.by import By

class UserPageLocs:

    #可用余额
    user_leftMoney = (By.XPATH,'//li[@class="color_sub"]')