#coding=utf-8
from log.user_log import UserLog
import time
from page.order_Info_page import Order_info_page
import datetime

class Order_info_handle(object):
    def __init__(self, driver):
        self.driver = driver
        self.orderinfo_p = Order_info_page(self.driver)
        get_user_log = UserLog()
        self.loger = get_user_log.get_log()

    #输入线索信息
    def send_userinfo(self, phoneNo, idNumber):
        self.loger.info("输入的手机号：" + phoneNo)
        self.orderinfo_p.get_phoneNo_element().send_keys(phoneNo)
        self.orderinfo_p.get_queryMobile_element().click()
        time.sleep(1)
        # self.loger.info("输入的身份证号：" + idNumber)
        # self.orderinfo_p.get_idNumber_element().send_keys(idNumber)
        self.orderinfo_p.get_xiansuolaiyuanlist_element().click()
        self.orderinfo_p.get_laiyuanqudao_element().click()

    #选择新车
    def search_xinche(self):
        self.orderinfo_p.get_chanpinxian_element().click()
        self.orderinfo_p.get_xinche_element().click()

    #选择二手车
    def search_ershouche(self, vin):
        self.orderinfo_p.get_chanpinxian_element().click()
        self.orderinfo_p.get_ershouche_element().click()
        self.orderinfo_p.get_vin_element().send_keys(vin)
        self.orderinfo_p.get_queryVin_element().click()
        self.orderinfo_p.get_baseDisplacement_element().send_keys("1.5L")
        self.orderinfo_p.get_baseSeating_element().send_keys("5")


    #输入车辆采购金额
    def send_purchaseAmount(self, purchaseAmount):
        self.orderinfo_p.get_purchaseAmount_element().send_keys(purchaseAmount)

    #选车
    def select_car_info(self):
        self.orderinfo_p.get_pinpai_element().click()
        self.orderinfo_p.get_richan_element().click()
        self.orderinfo_p.get_chexi_element().click()
        self.orderinfo_p.get_tianlai_element().click()
        self.orderinfo_p.get_chexinglist_element().click()
        self.orderinfo_p.get_chexing_element().click()

    #选择颜色
    def select_color_info(self):
        self.orderinfo_p.get_colorlist_element().click()
        self.orderinfo_p.get_color_element().click()

    #获取厂商
    def send_factoryName(self):
        self.orderinfo_p.get_factoryName_element().send_keys("东风日产")

    #输入指导价和售价
    def send_price(self, guidePrice, salePrice):
        self.orderinfo_p.get_guidePrice_element().clear()
        self.orderinfo_p.get_guidePrice_element().send_keys(guidePrice)
        self.orderinfo_p.get_salePrice_element().send_keys(salePrice)



    #选择上牌门店
    def select_shangpai_info(self):
        self.orderinfo_p.get_preLicenseProvince_element().click()
        self.orderinfo_p.get_bj_sheng_element().click()
        self.orderinfo_p.get_preLicenseCity_elment().click()
        self.orderinfo_p.get_bj_shi_element().click()
        self.orderinfo_p.get_preLicenseSotre_element().click()
        self.orderinfo_p.get_bj_mendian_element().click()
        self.orderinfo_p.get_queryEmissionStandardName_element().click()

    #选择易鑫工行
    def select_channelTypeGH(self):
        self.orderinfo_p.get_channelTypeGH_element().click()

    #选择易鑫其他
    def select_channelTypeQT(self):
        self.orderinfo_p.get_channelTypeQT_element().click()

    #选择汇通信诚
    def select_channelTypeHT(self):
        self.orderinfo_p.get_channelTypeHT_element().click()

    #选择长安新生
    def select_channelTypeCA(self):
        self.orderinfo_p.get_channelTypeCA_element().click()

    #选择奇瑞软银
    def select_channelTypeQR(self):
        self.orderinfo_p.get_channelTypeQR_element().click()

    #判断易鑫工行是否选中
    def channelTypeGH_is_selected(self):
        GH_rezult = self.orderinfo_p.get_channelTypeGH_element().is_selected()
        return GH_rezult

    #输入保险信息
    def send_baoxian_info(self, jiaoqiang, chechuan, shangye):
        self.orderinfo_p.get_firstYearVehicleAndVesselTax_element().send_keys(chechuan)
        self.orderinfo_p.get_firstYearSali_element().send_keys(jiaoqiang)
        self.orderinfo_p.get_firstCommercialTheft_element().send_keys(shangye)

    #输入垫付保险金额
    def send_dianfu(self, dianfu):
        self.orderinfo_p.get_advancePremiumAmt_element().send_keys(dianfu)

    #点击实名制-是
    def click_realNameSystemY(self):
        self.orderinfo_p.get_realNameSystemYNull_element().click()

    #点击实名制-否
    def click_realNameSystemN(self):
        self.orderinfo_p.get_realNameSystemNNull_element().click()

    #点击店保-是
    def click_shopInsuranceY(self):
        self.orderinfo_p.get_shopInsuranceYNull_element().click()

    #点击店保-否
    def click_shopInsuranceN(self):
        self.orderinfo_p.get_shopInsuranceNNull_element().click()

    #金融信息------------------------------合作方
    #输入期数-月供-利率
    def send_qs_yg_ll(self):
        self.orderinfo_p.get_termCount_element().send_keys("24")
        self.orderinfo_p.get_monthlyRent_element().send_keys("1000")
        self.orderinfo_p.get_cusInterestRates_element().send_keys("20")

    #输入购置税
    def send_gzs(self,purchaseTax):
        self.orderinfo_p.get_purchaseTax_element().send_keys(purchaseTax)

    #输入GPS费用
    def send_gps_fee(self, gps_fee):
        self.orderinfo_p.get_gpsFee_element().send_keys(gps_fee)

    #输入账户管理费
    def send_accountMaintenanceFee(self, accountMaintenanceFee):
        self.orderinfo_p.get_accountMaintenanceFee_element().send_keys(accountMaintenanceFee)

    #输入首付金额---合作方
    def send_yxDownPaymentAmt(self, yxDownPaymentAmt):
        self.orderinfo_p.get_yxDownPaymentAmt_element().send_keys(yxDownPaymentAmt)

    #输入风险融资额/申请贷款金额
    def send_yxRiskFinancingAmt(self, yxRiskFinancingAmt):
        self.orderinfo_p.get_yxRiskFinancingAmt_element().send_keys(yxRiskFinancingAmt)

    #输入风控融资额
    def send_yxRiskControlFinancingAmt(self, yxRiskControlFinancingAmt):
        self.orderinfo_p.get_yxRiskControlFinancingAmt_element().send_keys(yxRiskControlFinancingAmt)


    #金融信息---------------------花生
    #购车服务费
    def send_hsServiceFee(self, hsServiceFee):
        self.orderinfo_p.get_hsServiceFee_element().send_keys(hsServiceFee)

    #上牌费
    def send_licenseFee(self, licenseFee):
        self.orderinfo_p.get_licenseFee_element().send_keys(licenseFee)

    #抵押费
    def send_mortgageFee(self, mortgageFee):
        self.orderinfo_p.get_mortgageFee_element().send_keys(mortgageFee)

    #其他费用
    def send_totalDownPaymentOtherAmt(self, totalDownPaymentOtherAmt):
        self.orderinfo_p.get_totalDownPaymentOtherAmt_element().send_keys(totalDownPaymentOtherAmt)

    #备注
    def send_remarkId(self,remarkId):
        self.orderinfo_p.get_remarkId_element().send_keys(remarkId)

    #选择常规产品
    def select_changguiType(self):
        self.orderinfo_p.get_chanpinlist_element().click()
        self.orderinfo_p.get_chanpinCG_element().click()

    #选择产品A
    def select_chanpinA(self):
        self.orderinfo_p.get_chanpinlist_element().click()
        self.orderinfo_p.get_chanpinA_element().click()

    #选择产品B
    def select_chanpinB(self):
        self.orderinfo_p.get_chanpinlist_element().click()
        self.orderinfo_p.get_chanpinB_element().click()

    #选择产品C
    def select_chanpinC(self):
        self.orderinfo_p.get_chanpinlist_element().click()
        self.orderinfo_p.get_chanpinC_element().click()

    #输入易鑫编号
    def send_yxOrderNo(self):
        yxOrderNo = "YX" + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S%f"))
        self.orderinfo_p.get_yxOrderNo_element().send_keys(yxOrderNo)

    #机构上传截图
    def shangchuanjietu(self):
        self.orderinfo_p.get_jigoujietu_element().click()
        time.sleep(1)

    #身份证上传
    def send_shenfenzheng(self):
        self.orderinfo_p.get_shenfenzheng_element().click()
        time.sleep(1)

    def xuanzewenjian(self):
        self.orderinfo_p.get_checkfile_element().click()

    def querenguanbi(self):
        self.orderinfo_p.get_querenshangchuan_element().click()
        self.orderinfo_p.get_jietuguanbi_element().click()

    def click_zancun(self):
        self.orderinfo_p.get_basicTempSave_element().click()

    def click_basicModalBtnNegative(self):
        self.orderinfo_p.get_basicModalBtnNegative_element().click()

    #订单新增和审核公用提交
    def click_tijiao(self):
        self.orderinfo_p.get_basicSubmit_element().click()


    #点击返回
    def click_orderClose(self):
        self.orderinfo_p.get_orderClose_element().click()


















