from random import random
from time import sleep
import requests as req
import json

url = "https://auto.ru/-/ajax/desktop/listing/"

# 2001-2006 - 18529 предложений
# startYear = 2001
# finishYear = 2006
# 2007-2008 - 17768 предложений
# startYear = 2007
# finishYear = 2008
# 2009-2011 - 19761 предложений
# startYear = 2009
# finishYear = 2011
# 2012-2013 - 18885 предложений
# startYear = 2012
# finishYear = 2013
# 2014-2016 - 17761 предложений
# startYear = 2014
# finishYear = 2016
# 2017-2019 - 16194 предложений
# startYear = 2017
# startYear = 2019
# 2020 -2020 - 19946 предложений
# startYear = 2020
# finishYear = 2020

# секция параметров по годам
# 1990 - 1995 - 2557 предложения
# params = {
#     "year_from":1990,
#     "year_to":1995,
#     "section":"all",
#     "category":"cars",
#     "output_type":"list",
#     "geo_radius":200,"geo_id":[213]
# }
#
# # 1996 - 1998 - 3297 предложений
# params = {
#     "category":"cars",
#     "section":"all",
#     "output_type":"list",
#     "year_from":1996,
#     "year_to":1998,
#     "geo_radius":200,
#     "geo_id":[213]
# }
#
# # 1999 - 2000 - 2994 предложений
# params = {
#     "year_from":1999,
#     "year_to":2000,
#     "section":"all",
#     "category":"cars",
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
#
# # 2001 - 2001
# params = {
#     "year_from":2001,
#     "year_to":2001,
#     "section":"all",
#     "category":"cars",
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
#
# # 2002 - 2002
# params = {
#     "year_from":2002,
#     "year_to":2002,
#     "section":"all",
#     "category":"cars",
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
#
# # 2003 - 2003
# params = {
#     "year_from":2003,
#     "year_to":2003,
#     "section":"all",
#     "category":"cars",
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
#
# # 2004 - 2004
# params = {
#     "year_from":2004,
#     "year_to":2004,
#     "section":"all",
#     "category":"cars",
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
#
# # 2005 - 2005
# params = {
#     "year_from":2005,
#     "year_to":2005,
#     "section":"all",
#     "category":"cars",
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
#
#
# # 2006 - 2006
# # коробка - автомат
# params = {
#     "year_from":2006,
#     "year_to":2006,
#     "section":"all",
#     "category":"cars",
#     "transmission":["AUTO","AUTOMATIC","ROBOT","VARIATOR"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# #коробка механика
# params = {
#     "year_from":2006,
#     "year_to":2006,
#     "transmission":["MECHANICAL"],
#     "section":"all",
#     "category":"cars",
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
#
# # 2007 - 2007
# # коробка автомат
# params = {
#     "year_from":2007,
#     "year_to":2007,
#     "section":"all",
#     "category":"cars",
#     "transmission":["AUTOMATIC"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# # еще одна порция автоматов
# params = {
#     "year_from":2007,
#     "year_to":2007,
#     "section":"all",
#     "category":"cars",
#     "transmission":["ROBOT","VARIATOR"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# #механика
# params = {
#     "year_from":2007,
#     "year_to":2007,
#     "section":"all",
#     "category":"cars",
#     "transmission":["MECHANICAL"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
#
# # 2008 - 2008
# #механика, полный привод
# params = {
#     "year_from":2008,
#     "year_to":2008,
#     "transmission":["MECHANICAL"],
#     "section":"all",
#     "category":"cars",
#     "gear_type":["ALL_WHEEL_DRIVE"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# # механика,  передний  и задний приводы
# params = {
#     "year_from":2008,
#     "year_to":2008,
#     "transmission":["MECHANICAL"],
#     "section":"all",
#     "category":"cars",
#     "gear_type":["REAR_DRIVE","FORWARD_CONTROL"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# #  автомат полный привод
# params = {
#     "year_from":2008,
#     "year_to":2008,
#     "transmission":["AUTOMATIC","AUTO","ROBOT","VARIATOR"],
#     "gear_type":["ALL_WHEEL_DRIVE"],
#     "section":"all",
#     "category":"cars",
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# #автомат передний
# params = {
#     "year_from":2008,
#     "year_to":2008,
#     "transmission":["ROBOT","AUTOMATIC","VARIATOR","AUTO"],
#     "section":"all",
#     "category":"cars",
#     "gear_type":["FORWARD_CONTROL"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# #автомат задний привод
# params = {
#     "year_from":2008,
#     "year_to":2008,
#     "transmission":["ROBOT","AUTOMATIC","VARIATOR","AUTO"],
#     "section":"all",
#     "category":"cars",
#     "gear_type":["REAR_DRIVE"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
#
# # 2009 - 2009
# params = {
#     "year_from":2009,
#     "year_to":2009,
#     "section":"all",
#     "category":"cars",
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
#
#
# # 2010 - 2010
# #полный привод
# params = {
#     "year_from":2010,
#     "year_to":2010,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["ALL_WHEEL_DRIVE"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# #передний - несколько неполная выборка может быть
# params = {
#     "year_from":2010,
#     "year_to":2010,
#     "gear_type":["FORWARD_CONTROL"],
#     "section":"all",
#     "category":"cars",
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# #задний привод
# params = {
#     "year_from":2010,
#     "year_to":2010,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["REAR_DRIVE"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
#
#
# # 2011 - 2011
# # полный привод
# params = {
#     "year_from":2011,
#     "year_to":2011,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["ALL_WHEEL_DRIVE"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# # механика и передний привод
# params = {
#     "year_from":2011,
#     "year_to":2011,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["FORWARD_CONTROL"],
#     "transmission":["MECHANICAL"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# # автомат и передний привод
# params = {
#     "year_from":2011,
#     "year_to":2011,
#     "gear_type":["FORWARD_CONTROL"],
#     "section":"all",
#     "category":"cars",
#     "transmission":["AUTO","AUTOMATIC","ROBOT","VARIATOR"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# #задний привод
# params = {
#     "year_from":2011,
#     "year_to":2011,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["REAR_DRIVE"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
#
#
# # 2012 - 2012
# # полный привод
# params = {
#     "year_from":2012,
#     "year_to":2012,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["ALL_WHEEL_DRIVE"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# # механика и передний привод
# params = {
#     "year_from":2012,
#     "year_to":2012,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["FORWARD_CONTROL"],
#     "transmission":["MECHANICAL"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# # автомат и передний привод
# params = {
#     "year_from":2012,
#     "year_to":2012,
#     "gear_type":["FORWARD_CONTROL"],
#     "section":"all",
#     "category":"cars",
#     "transmission":["AUTO","AUTOMATIC","ROBOT","VARIATOR"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# #задний привод
# params = {
#     "year_from":2012,
#     "year_to":2012,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["REAR_DRIVE"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
#
#
# # 2013 - 2013
# # полный привод
# params = {
#     "year_from":2013,
#     "year_to":2013,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["ALL_WHEEL_DRIVE"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# # механика и передний привод
# params = {
#     "year_from":2013,
#     "year_to":2013,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["FORWARD_CONTROL"],
#     "transmission":["MECHANICAL"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# # автомат и передний привод
# params = {
#     "year_from":2013,
#     "year_to":2013,
#     "gear_type":["FORWARD_CONTROL"],
#     "section":"all",
#     "category":"cars",
#     "transmission":["AUTO","AUTOMATIC","ROBOT","VARIATOR"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# #задний привод
# params = {
#     "year_from":2013,
#     "year_to":2013,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["REAR_DRIVE"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
#
#
# # 2014 - 2014
# # полный привод
# params = {
#     "year_from":2014,
#     "year_to":2014,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["ALL_WHEEL_DRIVE"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# # механика и передний привод
# params = {
#     "year_from":2014,
#     "year_to":2014,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["FORWARD_CONTROL"],
#     "transmission":["MECHANICAL"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# # автомат и передний привод
# params = {
#     "year_from":2014,
#     "year_to":2014,
#     "gear_type":["FORWARD_CONTROL"],
#     "section":"all",
#     "category":"cars",
#     "transmission":["AUTO","AUTOMATIC","ROBOT","VARIATOR"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# #задний привод
# params = {
#     "year_from":2014,
#     "year_to":2014,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["REAR_DRIVE"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
#
#
# # 2015 - 2015
# # полный привод
# params = {
#     "year_from":2015,
#     "year_to":2015,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["ALL_WHEEL_DRIVE"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# # механика и передний привод
# params = {
#     "year_from":2015,
#     "year_to":2015,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["FORWARD_CONTROL"],
#     "transmission":["MECHANICAL"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# # автомат и передний привод
# params = {
#     "year_from":2015,
#     "year_to":2015,
#     "gear_type":["FORWARD_CONTROL"],
#     "section":"all",
#     "category":"cars",
#     "transmission":["AUTO","AUTOMATIC","ROBOT","VARIATOR"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# #задний привод
# params = {
#     "year_from":2015,
#     "year_to":2015,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["REAR_DRIVE"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
#
#
# # 2016 - 2016
# # полный привод
# params = {
#     "year_from":2016,
#     "year_to":2016,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["ALL_WHEEL_DRIVE"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# # механика и передний привод
# params = {
#     "year_from":2016,
#     "year_to":2016,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["FORWARD_CONTROL"],
#     "transmission":["MECHANICAL"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# # автомат и передний привод
# params = {
#     "year_from":2016,
#     "year_to":2016,
#     "gear_type":["FORWARD_CONTROL"],
#     "section":"all",
#     "category":"cars",
#     "transmission":["AUTO","AUTOMATIC","ROBOT","VARIATOR"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# #задний привод
# params = {
#     "year_from":2016,
#     "year_to":2016,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["REAR_DRIVE"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
#
#
# # 2017 - 2017
# # полный привод
# params = {
#     "year_from":2017,
#     "year_to":2017,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["ALL_WHEEL_DRIVE"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# # механика и передний привод
# params = {
#     "year_from":2017,
#     "year_to":2017,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["FORWARD_CONTROL"],
#     "transmission":["MECHANICAL"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# # автомат и передний привод
# params = {
#     "year_from":2017,
#     "year_to":2017,
#     "gear_type":["FORWARD_CONTROL"],
#     "section":"all",
#     "category":"cars",
#     "transmission":["AUTO","AUTOMATIC","ROBOT","VARIATOR"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# #задний привод
# params = {
#     "year_from":2017,
#     "year_to":2017,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["REAR_DRIVE"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
#
# # 2018 - 2018
# # полный привод
# params = {
#     "year_from":2018,
#     "year_to":2018,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["ALL_WHEEL_DRIVE"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# # механика и передний привод
# params = {
#     "year_from":2018,
#     "year_to":2018,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["FORWARD_CONTROL"],
#     "transmission":["MECHANICAL"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# # автомат и передний привод
# params = {
#     "year_from":2018,
#     "year_to":2018,
#     "gear_type":["FORWARD_CONTROL"],
#     "section":"all",
#     "category":"cars",
#     "transmission":["AUTO","AUTOMATIC","ROBOT","VARIATOR"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# #задний привод
# params = {
#     "year_from":2018,
#     "year_to":2018,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["REAR_DRIVE"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
#

# 2019 - 2019
# полный привод
params = {
    "year_from":2019,
    "year_to":2019,
    "section":"all",
    "category":"cars",
    "gear_type":["ALL_WHEEL_DRIVE"],
    "output_type":"list",
    "geo_radius":200,
    "geo_id":[213]
}
# # механика и передний привод
# params = {
#     "year_from":2019,
#     "year_to":2019,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["FORWARD_CONTROL"],
#     "transmission":["MECHANICAL"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# # автомат и передний привод
# params = {
#     "year_from":2019,
#     "year_to":2019,
#     "gear_type":["FORWARD_CONTROL"],
#     "section":"all",
#     "category":"cars",
#     "transmission":["AUTO","AUTOMATIC","ROBOT","VARIATOR"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
# #задний привод
# params = {
#     "year_from":2019,
#     "year_to":2019,
#     "section":"all",
#     "category":"cars",
#     "gear_type":["REAR_DRIVE"],
#     "output_type":"list",
#     "geo_radius":200,
#     "geo_id":[213]
# }
#


# 2020 - 2020





ref_params_key = "Referer"
ref_params_value = "https://auto.ru/moskva/cars/2019-year/all/drive-4x4_wheel/?output_type=list&page="


headers = '''
Host: auto.ru
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://auto.ru/moskva/cars/2019-year/all/drive-4x4_wheel/?output_type=list&page=2
x-client-app-version: 202007.06.152959
x-page-request-id: 717a2d59a603631ae1e3b4ddf1256395
x-client-date: 1594234168681
x-csrf-token: 6f20c6120dd716e4cbac376f1af1d7df03afcbe350078c7e
x-requested-with: fetch
content-type: application/json
Origin: https://auto.ru
Content-Length: 161
DNT: 1
Connection: keep-alive
Cookie: autoru_sid=a%3Ag5efae2552hqfqd8k2f04llqe50etfc4.f66280d6fdb90d3ab315fc505303657e%7C1594223350501.604800.PJ_g6EMi4051oUxrcmeh2A.VxZam4Pu5fdsOp4fWqQ4oyvQQrFVH1SpRoMgvqcbYiI; autoruuid=g5efae2552hqfqd8k2f04llqe50etfc4.f66280d6fdb90d3ab315fc505303657e; suid=1a4937a691982a7e936e75f3f227cd51.c0829dd6d4c3991b288d5e4fdc05509b; _ym_uid=1593500259362054855; _ym_d=1594234168; bltsr=1; crookie=MDPoQ6dY5f6plgEgtYQYhKELCUCbVJ9zJcT1emasjloDYpzY9pIFqA29FN2M/W9c/9KQfb21OCyNGxuLlCMi4Ldtfg0=; _csrf_token=6f20c6120dd716e4cbac376f1af1d7df03afcbe350078c7e; from_lifetime=1594234166714; from=direct; X-Vertis-DC=sas; cmtchd=MTU5NDIyODkxMDc4Nw==
Pragma: no-cache
Cache-Control: no-cache
'''.strip().split("\n")

print(headers)
dict_headers = {}
for header in headers:
    key, value = header.split(": ")
    dict_headers[key] = value
print(dict_headers)
offers = []
# цикл по страницам запускаем
for x in range(1,4):
    params['page'] = x
    dict_headers[ref_params_key] = ref_params_value + str(x)
    response = req.post(url, json=params, headers = dict_headers)

    print("page = {}".format(x), "status code = {}".format(response.status_code))
    data = response.json()
    offers.extend(data['offers'])
    sleep(8)

# with open('data.json') as f:
#    offers = json.load(f)

keys = ['badges', 'color_hex', 'documents', 'owner_expences', 'section', 'seller_type',
        'additional_info', 'price_info', 'price_history', 'saleId', 'state', 'tags', 'vehicle_info',
        'lk_summary', 'owner_expenses']
filtered_offers = []
for offer in offers:
    filtered_offer = {}
    for key in offer.keys():
        if key in keys:
            filtered_offer[key] = offer[key]
    filtered_offers.append(filtered_offer)


with open("data_parce.json", "w") as f:
    json.dump(filtered_offers, f)