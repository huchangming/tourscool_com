from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import unittest
import time
import os
from functools import wraps

from page_object import page_elenments
from reuse_method import now_time
from tourscool_log import base_log


# 错误时打印错误日志及截图给报告,装饰器函数，报错截图，不报错正常执行。
def getImage(function):
    @wraps(function)       # 装饰器自身不会修改被装饰的__name__属性
    def inner(self,*args, **kwargs):
        try:
            function(self,*args, **kwargs)    # 正常每次都会返回被装饰的case去执行,当遇到错误case失败时,执行异常模块
        except Exception as e:
            time_str_map = now_time.get_times()
            self.driver.get_screenshot_as_file('../tourscool_report/images/%s.png' % time_str_map)
            print('screenshot:', time_str_map, '.png')
            self.my_log.error(" %s 用例不通过:=====%s" % (function.__name__, str(e)))   # 日志尽量输出详细原始日志
            raise Exception(" %s 测试不通过" % function.__name__)

        else:            #未抛出异常时，才会执行
            self.my_log.info (" %s 测试通过" % function.__name__)
    return inner

class ToursCoolCase(unittest.TestCase):

    my_log = base_log.Logger('ToursCool').getlog()  # 放到init当中，每次重新调用，都会初始化一次。
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = 'nox'    # 必须要有，但是appium暂时用不到该参数。
        # desired_caps['newCommandTimeout'] = 7200             # appium连接超时时长
        # desired_caps['noReset'] = True          # 不会每次清楚缓存数据，不会反复登录
        desired_caps['appPackage'] = 'com.zmcs.tourscool'      # 包名
        desired_caps['appActivity'] = 'com.zmcs.tourscool.activity.SplashActivity'     # 包的活动页
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)       # 连接driver,4723跟脚本交互
        self.driver.implicitly_wait(5)
        self.case = page_elenments.AllElement(self.driver)
        #设置显性等待，lambda函数返回bool类型数据，15S内每2秒检查一次bool数据，当满足true时，执行下一步。超时进入异常。
        try:
            WebDriverWait(self.driver, 25,2).until(lambda x: x.find_element_by_id('btn_close'))
            self.my_log.info('跳过红包领取')
            self.case.skip_new_user()
        except Exception as e:
            self.driver.get_screenshot_as_file('../error_image/%s.png' % (self._testMethodName + now_time.get_times()))

    def tearDown(self):
        self.driver.quit()   # 请使用quit

    # 写法等价于 test_login = getImage(test_login)
    @getImage
    def test_login(self):
        ele = self.case
        self.my_log.info('个人中心')
        ele.my_home()
        self.my_log.info('准备登陆')
        ele.login()
        self.my_log.info('选择账号密码登陆')
        ele.select_login()
        self.my_log.info('输入账号')
        ele.account()
        self.my_log.info('输入密码')
        ele.password()
        self.my_log.info('登入')
        ele.login_to()
        # 截图
        # time_str_map = now_time.get_times()
        # self.driver.get_screenshot_as_file('../tourscool_report/images/%s.png' % time_str_map)
        # 修改报告模块HTMLtestrunner.py中的插入图片，以下打印会转换成检索图片关键字及名字并展示在报告中
        # print('screenshot:', time_str_map, '.png')
        # 断言
        self.assertTrue(bool(WebDriverWait(self.driver,8,2).until_not(lambda x: x.find_element_by_id('btn_login'))))
    @getImage
    def test_ll_search(self):
        ele = self.case
        self.my_log.info('点击首页搜索')
        ele.ll_search()
        self.my_log.info('输入搜索城市')
        ele.search_city()
        self.my_log.info('开始搜索')
        ele.goto_search()
        time.sleep(2)
        if self.driver.find_element_by_id('message'):
            raise Exception('搜索闪退')
    @getImage
    def test_create_order(self):
        self.driver.swipe(400,1400,400,200)
        time.sleep(1)
        self.driver.find_elements_by_class_name('android.widget.RelativeLayout')[0].click()
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()