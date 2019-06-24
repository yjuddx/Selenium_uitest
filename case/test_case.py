#coding=utf-8
from businees.login_business import LoginBusiness
from businees.order_list_business import Orderlist_business
from businees.order_info_business import Order_info_business
from businees.receipt_business import Receipt_business
import time
from selenium import webdriver
from util.xiansuo import Xiansuo

driver = webdriver.Chrome()
driver.get('http://test-hsr.huashenghaoche.com/hshcmdm/login')
driver.maximize_window()
login = LoginBusiness(driver)
login.user_login()
time.sleep(1)
xiansuo = Xiansuo()
username, phoneNo, idNumber = xiansuo.get_xiansuo()
login.to_yixinhuizu()
time.sleep(1)
order_list = Orderlist_business(driver)
order_list.to_xinzeng()
order_info = Order_info_business(driver)
order_info.user_info(phoneNo, idNumber)
time.sleep(1)
order_info.search_xinche()
vin = "LGBF5AE05JR004237"
#order_info.search_ershouche(vin)
order_info.purchaseAmount_info("50000")
order_info.car_info()
order_info.color_info()
#判断订金是否正确
earnestGear_rezult = order_info.car_price("40000")
order_info.shangpai_info()
order_info.channelTypeGH()
order_info.baoxian_YY()
order_info.baoxian_info("100", "100", "100")
order_info.dianfu_info("1000")
order_info.qs_yg_ll()
order_info.purchaseTax_base("100")
order_info.gps_fee("100")
order_info.accountMaintenanceFee("100")
order_info.zifang_shoufu("8000")
order_info.send_fengxian_fengkong("100", "100")
order_info.send_jinrongHS("100", "100", "100", "100")
order_info.send_remarkId("易鑫-工行主流程--保险YY----常规产品")
order_info.chanpinCG()
order_info.send_yxOrderNo()
order_info.shangchuanjietu()
time.sleep(1)
order_info.send_shenfenzheng()
time.sleep(1)
order_info.zancun_function()
order_info.tijiao_function()
order_list.to_shenhe(phoneNo)
time.sleep(1)
order_info.tijiao_function()
order_no = order_list.to_btn_xiaoshoujiesuan(phoneNo)
receipt = Receipt_business(driver)
receipt.receiptByCode()
receipt.dow_payment(order_no)
order_list.to_hetong(phoneNo)
# 18615650248
# order_list.to_hetong('18615650248')
order_list.shengcheng_hetong()
order_list.to_shangchuanhetong(phoneNo)
order_list.shangchuanxieyi()

time.sleep(2)
#driver.close()