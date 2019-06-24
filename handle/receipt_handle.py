#coding=utf-8
from log.user_log import UserLog
from time import sleep
from page.receipt_page import Receipt_page

class Receipt_handle(object):
    def __init__(self, driver):
        self.driver = driver
        self.receipt_p = Receipt_page(self.driver)
        get_user_log = UserLog()
        self.loger = get_user_log.get_log()

    #点击生成付款码并关闭
    def click_receiptByCode(self):
        self.receipt_p.get_receiptByCode_elment().click()
        sleep(1)
        self.receipt_p.get_queryReceipt_element().click()
        sleep(1)
        self.receipt_p.get_deliveryClose_element().click()
