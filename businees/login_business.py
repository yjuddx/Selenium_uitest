#coding=utf-8
from handle.login_handle import Login_handle
from util.read_ini import ReadIni

class LoginBusiness(object):
    def __init__(self, driver):
        self.login_h = Login_handle(driver)
        read_init = ReadIni()
        self.username = read_init.get_value('Login_user', 'username')
        self.password = read_init.get_value('Login_user', 'password')


    def user_login(self):
        self.login_h.send_username(self.username)
        self.login_h.send_password(self.password)
        self.login_h.click_login_button()

    def to_yixinhuizu(self):
        self.login_h.click_yixinhuizu()
