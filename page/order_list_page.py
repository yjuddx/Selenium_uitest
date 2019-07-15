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

    #通用提交按钮
    def get_yxHsContractApply_element(self):
        return self.fd.get_element("yxHsContractApply")

    #合同上传提交确定
    def get_basicModalBtnNegative_element(self):
        return self.fd.get_element("basicModalBtnNegative")

    #审核合同
    def get_btn_shenhehetong_element(self):
        return self.fd.get_element("btn_shenhehetong")

    #店保选择是
    def get_shopInsuranceYNull_element(self):
        return self.fd.get_element("shopInsuranceYNull")

    #店保选择否
    def get_shopInsuranceNNull_element(self):
        return self.fd.get_element("shopInsuranceNNull")

    #预订车辆
    def get_btn_yudingcheliang_element(self):
        return self.fd.get_element("btn_yudingcheliang")

    #花生合同交强险
    def get_forceAmountFlag_element(self):
        return self.fd.get_element("forceAmountFlag")

    #花生合同商业险
    def get_businessAmountFlag_element(self):
        return self.fd.get_element("businessAmountFlag")













