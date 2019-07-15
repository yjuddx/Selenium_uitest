#coding=utf-8
from handle.receipt_handle import Receipt_handle
from util.mysql_db import DB


class Receipt_business(object):
    def __init__(self, driver):
        self.driver = driver
        self.receipt_h = Receipt_handle(self.driver)

    #生成付款码
    def receiptByCode(self):
        self.receipt_h.click_receiptByCode()



    #执行SQL变成已收首付已付定金
    def dow_payment(self, order_no):
        db = DB('cforder')
        sql = "UPDATE t_yx_order_settlement SET state=3, deposit_state=1,down_actual_amt=11000,deposit_actual_amt=5000 WHERE order_no=" + "'" + order_no + "'"
        db.update(sql)
        db.close()