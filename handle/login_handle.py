#coding=utf-8
from page.login_page import LoginPage
from log.user_log import UserLog
import time

class Login_handle(object):
    def __init__(self, driver):
        self.driver = driver
        self.login_p = LoginPage(self.driver)
        get_user_log = UserLog()
        self.loger = get_user_log.get_log()

    def send_username(self, username):
        self.loger.info("输入用户名是：" + username)
        self.login_p.get_username_element().send_keys(username)

    def send_password(self, password):
        self.loger.info("输入密码是：" + password)
        self.login_p.get_password_element().send_keys(password)

    def click_login_button(self):
        self.login_p.get_loginSumit_element().click()

    def click_yixinhuizu(self):
        self.login_p.get_xiaoshouguanli_element().click()
        time.sleep(1)
        self.login_p.get_xiaoshouxitong_element().click()
        time.sleep(1)
        self.login_p.get_huizudingdanguanli_element().click()
        self.login_p.get_yixinhuizudingdan_element().click()


