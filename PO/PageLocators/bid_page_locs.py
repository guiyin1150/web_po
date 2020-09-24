"""
@File    : bid_page_loc
@Time    : 2019/12/9
@Author  : liyuan
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""

from selenium.webdriver.common.by import By

class BidPageLocs:

    #金额输入框
    money_input = (By.XPATH,"//input[contains(@class,'invest-unit-investinput')]")
    # 标的余额元素
    bid_money_text = (By.XPATH,'//div[contains(@class,"money_overplus")]//span[text()="剩余："]/following-sibling::span[1]')
    #投标按钮
    invest_button = (By.XPATH,'//button[text()="投标"]')
    #投资成功弹出框 - 查看并激活按钮
    active_button_on_successPop = (By.XPATH,'//div[@class="layui-layer-content"]//button[text()="查看并激活"]')
    # 投资失败 - 弹出框 - 提示信息
    invest_failed_popup = (By.XPATH, '//div[contains(@class,"layui-layer-dialog")]//div[@class="text-center"]')
    # 投资失败 - 弹出框 - 关闭弹出框
    invest_close_failed_popup_button = (By.XPATH, '//div[contains(@class,"layui-layer-dialog")]//a')