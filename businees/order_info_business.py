#coding=utf-8
from handle.order_info_handle import Order_info_handle
from log.user_log import UserLog
from os.path import abspath, dirname
import os
import time


class Order_info_business(object):
    def __init__(self, driver):
        self.driver = driver
        self.orderinfo_h = Order_info_handle(self.driver)
        self.zifangType = 0
        self.chanpinType = 0
        get_user_log = UserLog()
        self.loger = get_user_log.get_log()
        base_dir = dirname(dirname(abspath(__file__)))
        base_dir = base_dir.replace('\\', '/')
        self.base_dir = base_dir + "/util/" + "shangchuan.exe"

    #客户信息模块
    def user_info(self, phoneNo, idNumber):
        self.orderinfo_h.send_userinfo(phoneNo, idNumber)

    #车辆信息模块

    #选择新车
    def search_xinche(self):
        self.orderinfo_h.search_xinche()

    #选择二手车
    def search_ershouche(self, vin):
        self.orderinfo_h.search_ershouche(vin)

    #车辆采购价
    def purchaseAmount_info(self,purchaseAmount):
        self.orderinfo_h.send_purchaseAmount(purchaseAmount)

    def car_info(self):
        self.orderinfo_h.select_car_info()

    def color_info(self):
        self.orderinfo_h.select_color_info()

    #车辆销售价小于等于5W的，定金金额等于3500
    #车辆销售价大于5W小于等于10W，定金金额等于4500
    #车辆销售价大于10W小于等于15W，定金金额等于5000
    #车辆销售价大于15W，定金金额等于10000
    def car_price(self,salePrice):
        self.orderinfo_h.send_price("60000", salePrice)
        salePrice = int(salePrice)
        earnestGear = int(self.get_earnestGear())
        if salePrice <= 50000 and earnestGear == 3500:
            self.loger.info("定金金额：" + str(earnestGear))
            return True
        elif salePrice > 50000 and salePrice <= 10000 and earnestGear == 4500:
            self.loger.info("定金金额：" + str(earnestGear))
            return True
        elif salePrice > 100000 and salePrice <= 150000 and earnestGear == 5000:
            self.loger.info("定金金额：" + str(earnestGear))
            return True
        elif salePrice > 150000 and earnestGear == 10000:
            self.loger.info("定金金额：" + str(earnestGear))
            return True
        else:
            self.loger.info("获取失败定金金额：" + str(earnestGear))
            return False

    # 执行JS获取定金
    def get_earnestGear(self):
        get_earnestGear = """
                        var value = document.getElementById("earnestGear").value
                        return value
                        """
        earnestGear = self.driver.execute_script(get_earnestGear)
        return earnestGear

    def shangpai_info(self):
        self.orderinfo_h.select_shangpai_info()

    #金融信息---资方
    #选择易鑫-工行
    def channelTypeGH(self):
        self.orderinfo_h.select_channelTypeGH()
        self.zifangType = 1

    #选择易鑫-其他
    def channelTypeQT(self):
        self.orderinfo_h.select_channelTypeQT()
        self.zifangType = 2

    #选择汇通信诚
    def channelTypeHT(self):
        self.orderinfo_h.select_channelTypeHT()
        self.zifangType = 3

    #选择长安新生
    def channelTypeCA(self):
        self.orderinfo_h.select_channelTypeCA()
        self.zifangType = 4

    #返回选择的资方
    def get_zifangType(self):
        zifangType = self.zifangType
        return zifangType

    #判断易鑫工行是否选中
    def GH_is_selected(self):
        gh_rezult = self.orderinfo_h.channelTypeGH_is_selected()
        return gh_rezult

    #选择是否实名制：是 是否店保：是 ---可填写垫付保费
    #选择是否实名制：否 是否店保：否 ---不可填写垫付保费  计算保险差额时从保险系统获取
    #一个否 一个是--- 可填写垫付保费
    def baoxian_YY(self):
        self.orderinfo_h.click_realNameSystemY()
        self.orderinfo_h.click_shopInsuranceY()

    def baoxian_YN(self):
        self.orderinfo_h.click_realNameSystemY()
        self.orderinfo_h.click_shopInsuranceN()

    def baoxian_NN(self):
        self.orderinfo_h.click_realNameSystemN()
        self.orderinfo_h.click_shopInsuranceN()

    def baoxian_info(self, jiaoqiang, chechuan, shangye):
        self.jiaoqiang = jiaoqiang
        self.chechuang = chechuan
        self.shangye = shangye
        self.orderinfo_h.send_baoxian_info(jiaoqiang, chechuan, shangye)

    def get_baoxian(self):
        jiaoqiang = self.jiaoqiang
        chechuan = self.chechuang
        shangye = self.shangye
        return jiaoqiang, chechuan, shangye

    def dianfu_info(self, dianfu):
        self.dianfu = dianfu
        self.orderinfo_h.send_dianfu(dianfu)

    def get_dianfu(self):
        dianfu = self.dianfu
        return dianfu

    #期数-月供-利率
    def qs_yg_ll(self):
        self.orderinfo_h.send_qs_yg_ll()

    #输入购置税
    def purchaseTax_base(self,purchaseTax):
        self.purchaseTax = purchaseTax
        self.orderinfo_h.send_gzs(purchaseTax)

    def get_purchaseTax(self):
        purchaseTax = self.purchaseTax
        return purchaseTax

    def gps_fee(self,gps_fee):
        self.gps_fee = gps_fee
        self.orderinfo_h.send_gps_fee(gps_fee)

    #获取GPS费用
    def get_gps_fee(self):
        gps_fee = self.gps_fee()
        return gps_fee

    def accountMaintenanceFee(self,accountMaintenanceFee):
        self.accountMaintenanceFee = accountMaintenanceFee
        self.orderinfo_h.send_accountMaintenanceFee(accountMaintenanceFee)

    #获取账户管理
    def get_accountMaintenanceFee(self):
        accountMaintenanceFee = self.accountMaintenanceFee
        return accountMaintenanceFee

    #首付金额---合作方
    def zifang_shoufu(self, zf_shoufu):
        self.zf_shoufu = zf_shoufu
        self.orderinfo_h.send_yxDownPaymentAmt(zf_shoufu)

    #获取资方首付
    def get_zfshoufu(self):
        zf_shoufu = self.zf_shoufu
        return zf_shoufu

    #输入风险融资额/申请贷款金额，风控融资额
    def send_fengxian_fengkong(self, yxRiskFinancingAmt,yxRiskControlFinancingAmt):
        self.orderinfo_h.send_yxRiskFinancingAmt(yxRiskFinancingAmt)
        self.orderinfo_h.send_yxRiskControlFinancingAmt(yxRiskControlFinancingAmt)

    #金融信息-------------花生
    #输入购车服务费，上牌费，抵押费，其他费用
    def send_jinrongHS(self,hsServiceFee, licenseFee, mortgageFee,totalDownPaymentOtherAmt):
        self.orderinfo_h.send_hsServiceFee(hsServiceFee)
        self.orderinfo_h.send_licenseFee(licenseFee)
        self.orderinfo_h.send_mortgageFee(mortgageFee)
        self.orderinfo_h.send_totalDownPaymentOtherAmt(totalDownPaymentOtherAmt)

    #输入备注信息
    def send_remarkId(self, remarkId):
        self.orderinfo_h.send_remarkId(remarkId)

    #选择常规产品
    def chanpinCG(self):
        self.orderinfo_h.select_changguiType()
        self.chanpinType = 1

    #选择产品A
    def chanpinA(self):
        self.orderinfo_h.select_chanpinA()
        self.chanpinType = 2

    #选择产品B
    def chanpinB(self):
        self.orderinfo_h.select_chanpinB()
        self.chanpinType = 3

    #选择产品C
    def chanpinC(self):
        self.orderinfo_h.select_chanpinC()
        self.chanpinType = 4

    def get_chanpinType(self):
        chanpinType = self.chanpinType
        return chanpinType

    # 执行JS获取花生首付金额
    def get_hsDownPaymentAmt(self):
        get_hsDownPaymentAmt = """
                        var value = document.getElementById("hsDownPaymentAmt").value
                        return value
                        """
        hsDownPaymentAmt = self.driver.execute_script(get_hsDownPaymentAmt)
        return hsDownPaymentAmt

    # 执行JS获取花生首付比例
    def get_hsDownPaymentRatio(self):
        hsDownPaymentRatio = """
                        var value = document.getElementById("hsDownPaymentRatio").value
                        return value
                        """
        hsDownPaymentAmt = self.driver.execute_script(hsDownPaymentRatio)
        return hsDownPaymentRatio




    #常规产品花生首付金额计算逻辑
    # 首付金额默认等于零
    # 首付比例默认等于零
    # 首付合计 = 首付金额_金融信息合作方 + 上牌费 + 抵押登记费 + 购车服务费 + 其他收费项目
    #产品类型A花生首付计算逻辑
    # 首付金额 = 首付金额_金融信息合作方 - 购置税融资额 - 首年交强险 - 首年车船税 - 首年商业险
    # 首付比例 = 首付金额 / 车辆销售价，计算结果按照四舍五入保留两位小数
    # 首付合计 = 首付金额_金融信息花生 + 上牌费 + 抵押登记费 + 购车服务费 + 其他收费项目
    #产品类型B花生首付计算逻辑-易鑫工行和易鑫其他
    # 首付金额_金融信息花生 = 首付金额_金融信息合作机构 - 首年商业险 = 首年交强险 - 首年车船税 - 购置税 - GPS费用 - 账户管理费
    # 首付比例_金融信息花生 = 首付金额_金融信息花生 / 销售，计算结果四舍五入保留两位小数
    # 销售结算中的首付合计金额 = GPS费用 + 上牌费 + 抵押费 + 购车服务费 + 账户管理费 + 首付金额（首付金额为金融信息_花生）+其他收费项目
    #产品类型B花生首付计算逻辑-汇通信诚
    # 首付金额 = 首付金额_金融信息合作方 - 购置税融资额 - 首年交强险 - 首年车船税 - 首年商业险 - 经销商服务费 - 档案管理费
    # 首付比例 = 首付金额 / 车辆销售价，计算结果按照四舍五入保留两位小数
    # 首付合计 = 首付金额_金额信息花生 + 上牌费 + 抵押登记费 + 购车服务费 + 经销商服务费 + 档案管理费 + 其他收费项
    #产品类型B花生首付计算逻辑-长安新生
    # 首付金额 = 首付金额_金融信息合作方 - 购置税融资额 - 首年交强险 - 首年车船税 - 首年商业险 - 其他费用
    # 首付比例 = 首付金额 / 车辆销售价，计算结果按照四舍五入保留两位小数
    # 首付合计 = 首付金额_金额信息花生 + 上牌费 + 抵押登记费 + 购车服务费 + 其他费用 + 其他收费项

    #判断首付金额是否正确
    # def hs_shoufu(self):
    #     chanpinType = self.chanpinType
    #     zifangType = self.zifangType
    #     hs_shoufu = int(self.get_hsDownPaymentAmt())
    #     hs_shoufubili =int(self.get_hsDownPaymentRatio())
    #     if chanpinType == 1:
    #         if hs_shoufu == 0 and hs_shoufubili == 0:
    #             return True
    #     elif chanpinType == 2:
    #







    #输入易鑫编号
    def send_yxOrderNo(self):
        self.orderinfo_h.send_yxOrderNo()

    #机构上传截图
    def shangchuanjietu(self):
        self.orderinfo_h.shangchuanjietu()
        self.orderinfo_h.xuanzewenjian()
        os.system(self.base_dir)
        self.orderinfo_h.querenguanbi()


    #身份证上传截图
    def send_shenfenzheng(self):
        self.orderinfo_h.send_shenfenzheng()
        self.orderinfo_h.xuanzewenjian()
        os.system(self.base_dir)
        time.sleep(1)
        self.orderinfo_h.xuanzewenjian()
        os.system(self.base_dir)
        self.orderinfo_h.querenguanbi()

    #订单新增暂存
    def zancun_function(self):
        self.orderinfo_h.click_zancun()
        time.sleep(1)
        self.orderinfo_h.click_basicModalBtnNegative()
        time.sleep(1)

    #订单新增和审核提交
    def tijiao_function(self):
        self.orderinfo_h.click_tijiao()
        time.sleep(1)
        self.orderinfo_h.click_basicModalBtnNegative()

    def orderClose(self):
        self.orderinfo_h.click_orderClose()




















