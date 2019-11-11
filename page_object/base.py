from tourscool_log import base_log



class Base(object):

    # my_log = base_log.Logger('ToursCool').getlog()  # 放到init当中，每次重新调用，都会初始化一次。

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        # --------------------------------------------------------------

    # 单 寻找单个元素.返回元素对象
    def find_ele(self, *mode):
        return self.driver.find_element(*mode)

    # 复 寻找列表元素，返回元素对象
    def find_eles(self, index, *mode):
        return self.driver.find_elements(*mode)[index]
        # 与以下的方法无任何关联.
        # --------------------------------------------------------------

    # 单  输入数据
    def input_text(self, mode, text):
        self.driver.find_element(*mode).send_keys(text)

    # 复 输入数据
    def inputs_text(self, mode, index, text):
        self.driver.find_elements(*mode)[index].send_keys(text)

    # 单 点击事件
    def click(self, mode):
        self.driver.find_element(*mode).click()

    # 复 点击事件
    def clicks(self, mode, index):
        self.driver.find_elements(*mode)[index].click()

    # 单 获取文本
    def jiancha(self, mode):
        return self.driver.find_element(*mode).text

    # 复 获取文本
    def jianchaS(self, mode, index):
        return self.driver.find_elements(*mode)[index].text

    # 单 是否显示
    def displayed(self, mode):
        return self.driver.find_element(*mode).is_displayed()

    # 复 是否显示
    def displayeds(self, mode, index):
        return self.driver.find_elements(*mode)[index].is_displayed()

    def clear(self, mode):
        self.driver.find_element(*mode).clear()

    def page_data(self):
        return self.driver.page_source

    # 滑动
    def page_swipe(self,*ints):
        return self.driver.swipe(*ints)
