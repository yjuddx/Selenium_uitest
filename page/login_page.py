#coding=utf-8
from base.find_element import FindElement
class LoginPage(object):
    def __init__(self, driver):
        self.fd = FindElement(driver, "Login_page")

    #获取用户名元素
    def get_username_element(self):
        return self.fd.get_element("username")

    def get_password_element(self):
        return self.fd.get_element("password")

    def get_loginSumit_element(self):
        return self.fd.get_element("login-submit")

    def get_xiaoshouguanli_element(self):
        return self.fd.get_element("xiaoshouguanli")

    def get_xiaoshouxitong_element(self):
        return self.fd.get_element("xiaoshouxitong")

    def get_huizudingdanguanli_element(self):
        return self.fd.get_element("huizudingdanguanli")

    def get_yixinhuizudingdan_element(self):
        return self.fd.get_element("yixinhuizudingdan")



