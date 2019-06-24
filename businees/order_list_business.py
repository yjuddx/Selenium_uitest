# coding=utf-8
from handle.order_list_handle import Order_list_handle
import time
from os.path import abspath, dirname
import os


class Orderlist_business(object):
    def __init__(self, driver):
        self.driver = driver
        self.orderlist_h = Order_list_handle(self.driver)
        self.driver.switch_to_frame("frame-15080100")
        base_dir = dirname(dirname(abspath(__file__)))
        base_dir = base_dir.replace('\\', '/')
        self.base_dir = base_dir + "/util/" + "shangchuan.exe"

    def to_xinzeng(self):
        self.orderlist_h.xinzeng_click()

    #获取表单中数据
    def get_dept_list(self):
        row = self.driver.find_elements_by_tag_name('tr')
        list = []
        for i in row:
            j = i.find_elements_by_tag_name('td')
            for item in j:
                text = item.text
                list.append(text)
        return list[1]

    #查询并选中订单
    def search_order(self, phoneNo):
        self.orderlist_h.send_phoneNo(phoneNo)
        self.orderlist_h.serch_click()
        time.sleep(1)
        self.orderlist_h.searchRuzlt_click()

    #审核订单
    def to_shenhe(self, phoneNo):
        self.search_order(phoneNo)
        self.orderlist_h.shenhe_click()

    #点击销售结算
    def to_btn_xiaoshoujiesuan(self,phoneNo):
        self.search_order(phoneNo)
        order_no = self.get_dept_list()
        self.orderlist_h.click_btn_xiaoshoujiesuan()
        return order_no

    def to_hetong(self,phoneNo):
        self.search_order(phoneNo)
        self.orderlist_h.click_btn_shengchenghetong()

    #生成合同
    def shengcheng_hetong(self):
        self.orderlist_h.click_hsSignBody()

    #点击合同上传
    def to_shangchuanhetong(self,phoneNo):
        self.search_order(phoneNo)
        self.orderlist_h.click_btn_shangchuanhetong()

    #上传购车和代收车协议
    def shangchuanxieyi(self):
        self.orderlist_h.click_gouchexieyi()
        time.sleep(1)
        self.orderlist_h.click_daishouxieyi()
        time.sleep(1)
        self.orderlist_h.button_yxHsContractApply()





