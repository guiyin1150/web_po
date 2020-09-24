"""
 1）日志？失败截图？
      什么样子的日志：记录用例的执行过程。
      失败截图：用例失败了，在失败的操作截取当前的页面。

      用例当中每一个步骤 === 调页面对象的行为 + 测试数据
                                ||
                              页面对象
                                ||
                        selenium webdriver API
                             日志/失败截图
                                ||
                            1、等待可见
                            2、查找元素
                            3、点击 - 必然的前提：等待和查找
                            4、输入 - 必然的前提：等待和查找
                            5、获取属性 - 必然的前提：等待和查找
                            6、获取文本 - 必然的前提：等待和查找
"""

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PO.Common import logger
import logging
import time
from PO.Common.dir_config import screenshot_dir
from selenium.webdriver.common.by import By


# 记录日志/失败截图+错误信息输出+抛出异常
class Basepage:

    def __init__(self, driver: WebDriver):
        # 初始化driver
        self.driver = driver

    # 1、等待可见
    def wait_ele_visible(self,loc,img_name,timeout=20,poll_fre=0.5):
        """
        :param loc:
        :param img_name:{页面名称_页面行为}
        :param timeout:
        :param poll_fre:
        :return:
        等待开始的时候，记录一下当前时间。等待结束的时候，记录一下当前时间。时间差就是等待时长。
        """
        logging.info("{} 等待 {} 元素可见。".format(img_name,loc))
        # 等待开始的时候，记录一下当前时间
        try:
            WebDriverWait(self.driver, timeout,poll_frequency=poll_fre).until(EC.visibility_of_element_located(loc))
        except:
            # 失败截图 - 写入日志
            self.save_page_shot(img_name)
            logging.exception("等待元素可见失败：")
            raise
        # else:
        #     # 等待结束的时候，记录一下当前时间。
        #     pass

    # # 元素存在
    # def wait_page_contains_element(self):
    #     pass

    # 2、查找元素
    def get_element(self,loc,img_name):
        """
        :param loc:
        :param img_name: {页面名称_页面行为}
        :return:
        """
        logging.info("在 {} 查找元素：{}.".format(img_name,loc))
        try:
            ele = self.driver.find_element(*loc)
        except:
            self.save_page_shot(img_name)
            logging.exception("查找元素失败！")
            raise
        else:
            return ele

    # 2、查找元素们
    def get_elements(self, loc, img_name):
        """
        :param loc:
        :param img_name: {页面名称_页面行为}
        :return:
        """
        logging.info("在 {} 查找所有匹配的元素：{}.".format(img_name, loc))
        try:
            eles = self.driver.find_elements(*loc)
        except:
            self.save_page_shot(img_name)
            logging.exception("查找元素失败！")
            raise
        else:
            return eles

    # 3、点击元素。
    def click_element(self,loc,img_name,timeout=20,poll_fre=0.5):
        """
        :param loc:
        :param img_name: {页面名称_页面行为}
        :param timeout:
        :param poll_fre:
        :return:
        """
        self.wait_ele_visible(loc,img_name,timeout,poll_fre)  # 必然的前提
        ele = self.get_element(loc,img_name)  # 必然的前提
        logging.info("在 {}  点击 {} 元素。".format(img_name, loc))
        try:
            ele.click()
        except:
            self.save_page_shot(img_name)
            logging.exception("点击元素失败！")
            raise

    # 元素的输入操作
    def input_text(self,loc,value,img_name,timeout=20,poll_fre=0.5):
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)  # 必然的前提
        ele = self.get_element(loc, img_name)  # 必然的前提
        logging.info("在 {} 往元素 {} 输入文本值：{}。".format(img_name, loc, value))
        try:
            ele.send_keys(value)
        except:
            self.save_page_shot(img_name)
            logging.exception("元素输入文本失败！")
            raise
    #获取属性值
    def get_ele_attribute(self,loc,attr_name,img_name,timeout=20,poll_fre=0.5):
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)  # 必然的前提
        ele = self.get_element(loc, img_name)  # 必然的前提
        logging.info("在 {} 获取元素 {} 的 {} 属性。".format(img_name, loc, attr_name))
        try:
            value = ele.get_attribute(attr_name)
        except:
            self.save_page_shot(img_name)
            logging.exception("获取元素的属性失败！")
            raise
        else:
            logging.info("属性值为：{}".format(value))
            return value

    # 获取元素的文本值
    def get_ele_text(self,loc,img_name,timeout=20,poll_fre=0.5):
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)  # 必然的前提
        ele = self.get_element(loc, img_name)  # 必然的前提
        logging.info("在 {} 获取元素 {} 的文本内容。".format(img_name, loc))
        try:
            text = ele.text
        except:
            self.save_page_shot(img_name)
            logging.exception("获取元素的文本失败！")
            raise
        else:
            logging.info("文本值为：{}".format(text))
            return text

    def save_page_shot(self,img_name):
        """
        :param img_name: {页面名称_页面行为}
        :return:
        """
        # 将图片存储到Outputs的screenshots下。唯一不同的是，图片命名
        # 命名规范：{页面名称_页面行为}_时间.png
        # 文件完整名称 = Outputs的screenshots + {页面名称_页面行为}_时间.png
        # file_name = "{}_{}.png".format(img_name,"当前时间")
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        screenshot_path = screenshot_dir + "/{}_{}.png".format(img_name, now)
        self.driver.save_screenshot(screenshot_path)
        logging.info("截取当前网页成功并存储在: {}".format(screenshot_path))



if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    # 调basepage类里面儿的页面操作行为。 实例化。
    bp = Basepage(driver)
    search_loc = ("id","kw")
    button_loc = ("id","su")
    bp.input_text(search_loc,"柠檬班","百度页面_搜索输入操作")
    bp.click_element(button_loc,"百度页面_点击百度一下")
    time.sleep(5)
    driver.quit()




