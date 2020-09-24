from selenium.webdriver.common.by import By

class HomePageLocs:
    # 退出元素定位
    exit_loc = (By.XPATH, '//a[text()="退出"]')
    # 关于我们
    about_us = (By.XPATH, '//a[text()="关于我们"]')
    # 用户昵称
    user_link = (By.XPATH, '//a[@href="/Member/index.html"]')
    # 抢投标按钮
    bid_button = (By.XPATH, '//a[@class="btn btn-special"]')