#coding=utf-8
from base.find_element import FindElement

class Receipt_page(object):
    def __init__(self, driver):
        self.fd = FindElement(driver, "Receipt_page")

    #获取生成付款吗
    def get_receiptByCode_elment(self):
        return self.fd.get_element("receiptByCode")

    #获取关闭按钮
    def get_queryReceipt_element(self):
        return self.fd.get_element("queryReceipt")

    #获取返回按钮
    def get_deliveryClose_element(self):
        return self.fd.get_element("deliveryClose")