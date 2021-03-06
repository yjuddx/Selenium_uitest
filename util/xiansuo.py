#codin=utf-8
from util import shenfenzheng
import requests
import random
import re

class Xiansuo(object):
    def __init__(self):
        self.address='http://test.hsr.huashenghaoche.com'
        self.data = {
            'loginId': 'ccadmin',
            'password': '123qwe'
        }
        name_random = random.randint(10000, 100000)
        self.lead_name = '测试' + str(name_random)
        phone_random = random.randint(10000000, 99999999)
        self.phone = '120' + str(phone_random)
        #print(self.phone)
        self.Idcard = shenfenzheng.main()
        #print(self.Idcard)

    def login(self):
        #登录
        login_path = '/hshcmdm/toLogin'
        login_url = self.address + login_path
        res = requests.post(url=login_url, data=self.data)
        cookies = res.cookies['hshc_sid_test']
        self.cookies = {'hshc_sid_test': cookies}



    def create_xiansuo(self):
        #提取门店code和门店名称
        self.leads_address = 'http://test-crm.huashenghaoche.com'
        toleads_path = '/hshccrm/newleads/toAddLeads'
        self.toleads_url = self.leads_address + toleads_path
        #print(self.toleads_url)
        res = requests.get(self.toleads_url, cookies=self.cookies)
        html = res.text
        saleDepIdObj = re.search('<input type="hidden" name="saleDepId" value="(.*?)" />', html)
        if saleDepIdObj:
            self.saleDepId = saleDepIdObj.group(1)
            #print(self.saleDepId)
        saleDepObj = re.search('<input type="hidden" name="saleDep" value="(.*?)" />', html)
        if saleDepObj:
            self.saleDep = saleDepObj.group(1)
            #print(self.saleDep)


        #创建线索
        json_data = {
            "customBaseRecord": {
                "customerName": self.lead_name,
                "customerMobile": self.phone,
                "wechatNo": "",
                "qqNo": "",
                "channel": "",
                "birthday": "",
                "email": "",
                "certificateNo": self.Idcard,
                "residenceAddress": "",
                "bindStatus": "",
                "customerType": "customerTypeStatusList_001",
                "sex": "1",
                "certificateType": "customerCertificatesList_001",
                "provinceId": "",
                "cityId": "",
                "districtId": "",
                "province": 'null',
                "city": 'null',
                "district": 'null'
            },
            "leadDetail": {
                "channel": "A01_001_001",
                "saleDepId": self.saleDepId,
                "saleDep": self.saleDep,
                "createType": "msgCreateList_001",
                "shopCity": "120100",
                "shopProvince": "120000",
                "shopId": self.saleDepId,
                "saleShop": self.saleDep,
                "consultType": "msgMsgTypeList_001",
                "businessLine": "1",
                "distributorCode": "",
                "macketActivity": "",
                "usedProvince": "",
                "usedCity": "",
                "distributor": 'null'
            },
            "bookCarIntention": {
                "carBudget": "",
                "downPaymentBudget": "",
                "mostBudget": "",
                "paymentType": "",
                "financialIntention": "",
                "carPurpose": "",
                "gearBox": "",
                "carPreference": "",
                "intentionCarVoList": [{
                    "intentionalBrand": "",
                    "intentionalSeries": "",
                    "intentionalCars": "",
                    "intentionalBrandName": "请选择",
                    "intentionalSeriesName": "请选择",
                    "intentionalCarsName": "请选择"
                }]
            },
            "leadVisitDetail": {
                "nextTime": "2018-08-28 15:59:21",
                "failureCause": "",
                "visitStatus": "msgCallList_callOut_contact_001",
                "communicationNote": "123123",
                "communicationMode": "msgCommunicateTypeList_001",
                "intentionLeavel": "msgIntentLevelList_001"
            }
        }
        add_lead_path = '/hshccrm/newleads/create/1/1'
        self.add_lead_url = self.leads_address + add_lead_path
        #print(self.add_lead_url)
        res = requests.post(url=self.add_lead_url, json=json_data, cookies=self.cookies).json()
        self.reszult = res
        #print(self.reszult)
#        self.assertEqual(self.reszult['re']['msg'], '可以新建')

    def get_xiansuo(self):
        username = self.lead_name
        phone = self.phone
        idcard = self.Idcard
        return username, phone, idcard


if __name__ == '__main__':
    a = Xiansuo()
    a.login()
    a.create_xiansuo()
    e, b, c = a.get_xiansuo()
    print(e)
    print(b)
    print(c)

