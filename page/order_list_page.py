#coding=utf-8
from base.find_element import FindElement

class Order_list():
    def __init__(self, driver):
        self.fd = FindElement(driver, "Order_list")


    #新增按钮
    def get_xinzeng_element(self):
        return self.fd.get_element("xinzeng")

    #查询框输入手机号
    def get_phoneNo_element(self):
        return self.fd.get_element("phoneNo")

    #查询按钮
    def get_serch_element(self):
        return self.fd.get_element("btnSearch")

    #查询后选择回租订单
    def get_btSelectItem_element(self):
        return self.fd.get_element("btSelectItem")

    #点击审核订单
    def get_btn_shenhedingdan_element(self):
        return self.fd.get_element("btn_shenhedingdan")

    #点击销售结算
    def get_btn_xiaoshoujiesuan_element(self):
        return self.fd.get_element("btn_xiaoshoujiesuan")

    #获取订单编号
    def get_order_no_element(self):
        return self.fd.get_element("order_no")

    #获取生成合同
    def get_btn_shengchenghetong_element(self):
        return self.fd.get_element("btn_shengchenghetong")

    #花生合同---签约主体
    def get_hsSignBody_element(self):
        return self.fd.get_element("hsSignBody")

    #选择签约主体
    def get_hsSignBody_1_element(self):
        return self.fd.get_element("hsSignBody_1")

    #生成合同
    def get_makeContract_element(self):
        return self.fd.get_element("makeContract")

    #返回按钮
    def get_deliveryClose_element(self):
        return self.fd.get_element("deliveryClose")

    #上传合同按钮
    def get_btn_shangchuanhetong_element(self):
        return self.fd.get_element("btn_shangchuanhetong")

    #购车协议上传按钮
    def get_gouchexieyi_element(self):
        return self.fd.get_element("gouchexieyi")

    #代收协议上传按钮
    def get_daishouxieyi_element(self):
        return self.fd.get_element("daishouxieyi")

    #选择文件
    def get_check_element(self):
        return self.fd.get_element("check")

    #确认上传
    def get_sub_element(self):
        return self.fd.get_element("sub")

    #关闭按钮
    def get_guanbi_element(self):
        return self.fd.get_element("guanbi")

    #提交按钮
    def get_yxHsContractApply_element(self):
        return self.fd.get_element("yxHsContractApply")












