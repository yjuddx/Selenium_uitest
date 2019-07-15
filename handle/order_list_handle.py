#coding=utf-8
from log.user_log import UserLog
import time
from page.order_list_page import Order_list
from os.path import abspath, dirname
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Order_list_handle(object):
    def __init__(self, driver):
        self.driver = driver
        self.orderlist_p = Order_list(self.driver)
        get_user_log = UserLog()
        self.loger = get_user_log.get_log()
        base_dir = dirname(dirname(abspath(__file__)))
        base_dir = base_dir.replace('\\', '/')
        self.base_dir = base_dir + "/util/" + "shangchuan.exe"

    #新增
    def xinzeng_click(self):
        self.orderlist_p.get_xinzeng_element().click()

    #审核
    def shenhe_click(self):
        self.orderlist_p.get_btn_shenhedingdan_element().click()

    #输入手机号
    def send_phoneNo(self, phoneNo):
        self.orderlist_p.get_phoneNo_element().send_keys(phoneNo)

    #点击查询
    def serch_click(self):
        self.orderlist_p.get_serch_element().click()

    #选择查询结果
    def searchRuzlt_click(self):
        self.orderlist_p.get_btSelectItem_element().click()

    #点击销售结算
    def click_btn_xiaoshoujiesuan(self):
        self.orderlist_p.get_btn_xiaoshoujiesuan_element().click()

    #获取订单编号
    def get_order_no(self):
        self.orderlist_p.get_order_no_element().getText()

    #点击生成合同
    def click_btn_shengchenghetong(self):
        self.orderlist_p.get_btn_shengchenghetong_element().click()

    #选择签约主体
    def click_hsSignBody(self):
        self.orderlist_p.get_hsSignBody_element().click()
        self.orderlist_p.get_hsSignBody_1_element().click()
        self.orderlist_p.get_makeContract_element().click()
        self.orderlist_p.get_deliveryClose_element().click()

    #上传合同
    def click_btn_shangchuanhetong(self):
        self.orderlist_p.get_btn_shangchuanhetong_element().click()

    #购车协议上传
    def click_gouchexieyi(self):
        self.orderlist_p.get_gouchexieyi_element().click()
        time.sleep(1)
        self.orderlist_p.get_check_element().click()
        os.system(self.base_dir)
        time.sleep(1)
        self.orderlist_p.get_sub_element().click()
        self.orderlist_p.get_guanbi_element().click()

    #代收代付协议上传
    def click_daishouxieyi(self):
        self.orderlist_p.get_daishouxieyi_element().click()
        time.sleep(1)
        self.orderlist_p.get_check_element().click()
        os.system(self.base_dir)
        time.sleep(1)
        self.orderlist_p.get_sub_element().click()
        self.orderlist_p.get_guanbi_element().click()

    #提交按钮
    def button_yxHsContractApply(self):
        self.orderlist_p.get_yxHsContractApply_element().click()
        time.sleep(1)
        self.orderlist_p.get_basicModalBtnNegative_element().click()

    #审核合同
    def btn_shenhehetong(self):
        self.orderlist_p.get_btn_shenhehetong_element().click()

    #店保选择是提交
    def shopInsuranceY(self):
        #self.orderlist_p.get_shopInsuranceYNull_element().click()
        self.orderlist_p.get_shopInsuranceNNull_element().click()
        time.sleep(3)
        #self.orderlist_p.get_forceAmountFlag_element().click()
        #self.orderlist_p.get_businessAmountFlag_element().click()
        self.orderlist_p.get_yxHsContractApply_element().click()
        time.sleep(1)
        self.orderlist_p.get_basicModalBtnNegative_element().click()

    #点击预订车辆按钮
    def click_btn_yudingcheliang(self):

        self.orderlist_p.get_btn_yudingcheliang_element().click()












