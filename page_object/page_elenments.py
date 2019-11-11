from appium.webdriver.common.mobileby import By
from time import sleep
from datetime import datetime

from page_object import base
from data_config import test_data

class AllElement(base.Base):


    def __init__(self,driver):
        base.Base.__init__(self,driver)
        self.random_time = datetime.now().strftime('%m%d%H%M%S')

    def skip_new_user(self):

        self.click((By.ID, 'btn_close'))

    def my_home(self):

        self.click((By.NAME, '我的'))

    def login(self):

        self.click((By.NAME, '登录/注册'))

    def select_login(self):

        self.click((By.ID, 'tv_account_login'))

    def account(self):

        self.input_text((By.ID, 'et_acount'), test_data.username)

    def password(self):

        self.input_text((By.ID, 'et_password'), test_data.password)

    def login_to(self):

        self.click((By.ID, 'btn_login'))
        sleep(3)

    def ll_search(self):
        self.click((By.ID, 'll_search'))

    def search_city(self):
        self.input_text((By.ID, 'et_search'), '2')


    def goto_search(self):
        self.click((By.ID, 'search'))
