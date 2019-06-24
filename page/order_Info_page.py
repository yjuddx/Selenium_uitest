#coding=utf-8
from base.find_element import FindElement

class Order_info_page(object):
    def __init__(self, driver):
        self.fd = FindElement(driver, "Order_Info")

    #获取用户手机号
    def get_phoneNo_element(self):
        return self.fd.get_element("phoneNo")

    #点击查询按钮
    def get_queryMobile_element(self):
        return self.fd.get_element("queryMobile")

    #获取身份证
    def get_idNumber_element(self):
        return self.fd.get_element("idNumber")

    #获取产品线选择
    def get_chanpinxian_element(self):
        return self.fd.get_element("chanpinxian")

    #获取新车
    def get_xinche_element(self):
        return self.fd.get_element("xinche")

    #获取二手车
    def get_ershouche_element(self):
        return self.fd.get_element("ershouche")

    #获取二手车查询按钮
    def get_queryVin_element(self):
        return self.fd.get_element("queryVin")

    #获取车架号
    def get_vin_element(self):
        return self.fd.get_element("vin")

    #获取排量
    def get_baseDisplacement_element(self):
        return self.fd.get_element("baseDisplacement")

    #获取座位数
    def get_baseSeating_element(self):
        return self.fd.get_element("baseSeating")


    #获取车辆采购金额
    def get_purchaseAmount_element(self):
        return self.fd.get_element("purchaseAmount")

    #获取品牌列表
    def get_pinpai_element(self):
        return self.fd.get_element("pinpai")

    #获取品牌
    def get_richan_element(self):
        return self.fd.get_element("richan")

    #获取车系列表
    def get_chexi_element(self):
        return self.fd.get_element("chexi")

    #获取车系
    def get_tianlai_element(self):
        return self.fd.get_element("tianlai")

    #获取车型列表
    def get_chexinglist_element(self):
        return self.fd.get_element("chexinglist")

    #获取车型
    def get_chexing_element(self):
        return self.fd.get_element("chexing")

    #获取颜色列表
    def get_colorlist_element(self):
        return self.fd.get_element("colorlist")

    #获取颜色
    def get_color_element(self):
        return self.fd.get_element("color")

    #获取指导价
    def get_guidePrice_element(self):
        return self.fd.get_element("guidePrice")

    #获取售价
    def get_salePrice_element(self):
        return self.fd.get_element("salePrice")

    #获取定金档位
    def get_earnestGear_element(self):
        return self.fd.get_element("earnestGear")

    #获取上牌省列表
    def get_preLicenseProvince_element(self):
        return self.fd.get_element("preLicenseProvince")

    #获取上牌省
    def get_bj_sheng_element(self):
        return self.fd.get_element("bj_sheng")

    #获取上牌市列表
    def get_preLicenseCity_elment(self):
        return self.fd.get_element("preLicenseCity")

    #获取上牌市
    def get_bj_shi_element(self):
        return self.fd.get_element("bj_shi")

    #获取上牌门店列表
    def get_preLicenseSotre_element(self):
        return self.fd.get_element("preLicenseSotre")

    #获取上牌门店
    def get_bj_mendian_element(self):
        return self.fd.get_element("bj_mendian")

    #获取易鑫工行
    def get_channelTypeGH_element(self):
        return self.fd.get_element("channelTypeGH")

    #获取易鑫其他
    def get_channelTypeQT_element(self):
        return self.fd.get_element("channelTypeQT")

    #获取汇通信诚
    def get_channelTypeHT_element(self):
        return self.fd.get_element("channelTypeHT")

    #获取长安新生
    def get_channelTypeCA_element(self):
        return self.fd.get_element("channelTypeCA")

    #获取首年交强险
    def get_firstYearSali_element(self):
        return self.fd.get_element("firstYearSali")

    #获取首年车船税
    def get_firstYearVehicleAndVesselTax_element(self):
        return self.fd.get_element("firstYearVehicleAndVesselTax")

    #获取首年商业险
    def get_firstCommercialTheft_element(self):
        return self.fd.get_element("firstCommercialTheft")

    #获取垫付保费金额
    def get_advancePremiumAmt_element(self):
        return self.fd.get_element("advancePremiumAmt")

    #获取实名制-是
    def get_realNameSystemYNull_element(self):
        return self.fd.get_element("realNameSystemYNull")

    #获取实名制-否
    def get_realNameSystemNNull_element(self):
        return self.fd.get_element("realNameSystemNNull")

    #获取店保-是
    def get_shopInsuranceYNull_element(self):
        return self.fd.get_element("shopInsuranceYNull")

    #获取店保-否
    def get_shopInsuranceNNull_element(self):
        return self.fd.get_element("shopInsuranceNNull")

    #获取期数
    def get_termCount_element(self):
        return self.fd.get_element("termCount")

    #获取月供
    def get_monthlyRent_element(self):
        return self.fd.get_element("monthlyRent")

    #获取客户利率
    def get_cusInterestRates_element(self):
        return self.fd.get_element("cusInterestRates")

    #获取购置税
    def get_purchaseTax_element(self):
        return self.fd.get_element("purchaseTax")

    #获取GPS费用
    def get_gpsFee_element(self):
        return self.fd.get_element("financing.gpsFee")

    #获取账号管理费
    def get_accountMaintenanceFee_element(self):
        return self.fd.get_element("accountMaintenanceFee")

    #获取首付金额--合作方
    def get_yxDownPaymentAmt_element(self):
        return self.fd.get_element("yxDownPaymentAmt")

    #获取风险融资额/申请贷款金额
    def get_yxRiskFinancingAmt_element(self):
        return self.fd.get_element("yxRiskFinancingAmt")


    #获取风控融资额
    def get_yxRiskControlFinancingAmt_element(self):
        return self.fd.get_element("yxRiskControlFinancingAmt")

    #获取经销商服务费
    def get_dealerServiceFeeId_element(self):
        return self.fd.get_element("dealerServiceFeeId")

    #获取档案服务费
    def get_fileManagementFeeId_element(self):
        return self.fd.get_element("fileManagementFeeId")

    #获取其他费用
    def get_otherExpenses_element(self):
        return self.fd.get_element("otherExpenses")


    #金融信息花生---------------------------
    #购车服务费
    def get_hsServiceFee_element(self):
        return self.fd.get_element("hsServiceFee")

    #上牌费
    def get_licenseFee_element(self):
        return self.fd.get_element("licenseFee")

    #抵押费
    def get_mortgageFee_element(self):
        return self.fd.get_element("mortgageFee")

    #其他费用
    def get_totalDownPaymentOtherAmt_element(self):
        return self.fd.get_element("totalDownPaymentOtherAmt")

    #备注
    def get_remarkId_element(self):
        return self.fd.get_element("remarkId")

    #获取产品类型列表
    def get_chanpinlist_element(self):
        return self.fd.get_element("chanpinlist")

    #获取常规产品
    def get_chanpinCG_element(self):
        return self.fd.get_element("chanpinCG")

    #获取产品A
    def get_chanpinA_element(self):
        return self.fd.get_element("chanpinA")

    #获取产品B
    def get_chanpinB_element(self):
        return self.fd.get_element("chanpinB")

    #获取产品C
    def get_chanpinC_element(self):
        return self.fd.get_element("chanpinC")

    #获取易鑫订单编号
    def get_yxOrderNo_element(self):
        return self.fd.get_element("yxOrderNo")

    #机构上传截图
    def get_jigoujietu_element(self):
        return self.fd.get_element("jigoushangchuan")

    #选择文件
    def get_checkfile_element(self):
        return self.fd.get_element("yx-upload-check")

    #确认上传
    def get_querenshangchuan_element(self):
        return self.fd.get_element("yx-upload-sub")

    #上传截图关闭按钮
    def get_jietuguanbi_element(self):
        return self.fd.get_element("jietuguanbi")

    #身份证上传按钮
    def get_shenfenzheng_element(self):
        return self.fd.get_element("shenfenzheng")

    #暂存
    def get_basicTempSave_element(self):
        return self.fd.get_element("basicTempSave")

    #暂存后确定
    def get_basicModalBtnNegative_element(self):
        return self.fd.get_element("basicModalBtnNegative")

    #提交
    def get_basicSubmit_element(self):
        return self.fd.get_element("basicSubmit")

    #获取返回
    def get_orderClose_element(self):
        return self.fd.get_element("orderClose")



