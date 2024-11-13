import requests
import execjs
import pandas as pd
import csv
import json
import os

all_items = []
num = 0
# 隧道域名:端口号
tunnel = "q518.kdltpspro.com:15818"

# 用户名密码方式
username = "t13132378424292"
password = "pl930bnu"
proxies = {
    "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
    "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
}

# 读取 CSV 文件
df = pd.read_csv('高校信息.csv')

# 提取 'school_id' 列的数据，并转换为列表
school_id_list = df['school_id'].tolist()

shengfen_list = [11, 12, 13, 14, 15, 21, 22, 23, 31, 32, 33, 34, 35, 36, 37, 41, 42, 43, 44, 45, 46, 50, 51, 52, 53, 54, 61, 62, 63, 64, 65, 81, 82]

shengfen_dict = {11: '北京', 33: '浙江', 31: '上海', 32: '江苏', 34: '安徽', 42: '湖北', 61: '陕西', 44: '广东', 51: '四川', 23: '黑龙江', 12: '天津', 37: '山东', 35: '福建', 43: '湖南', 22: '吉林', 21: '辽宁', 50: '重庆', 62: '甘肃', 41: '河南', 53: '云南', 36: '江西', 45: '广西', 52: '贵州', 14: '山西', 46: '海南', 13: '河北', 15: '内蒙古', 64: '宁夏', 65: '新疆', 63: '青海', 54: '西藏', 81: '香港', 82: '澳门'}
for i in school_id_list:
    for j in shengfen_list:

        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json',
            'Origin': 'https://www.gaokao.cn',
            'Referer': 'https://www.gaokao.cn/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        page = 1
        local_province_id = str(j)
        school_id = str(i)
        local_type_id = '2073'
        year = 2022


        url = f'https://api.zjzw.cn/web/api/?e_sort=zslx_rank,min&e_sorttype=desc,desc&local_province_id={local_province_id}&local_type_id={local_type_id}&page={page}&school_id={school_id}&size=10&uri=apidata/api/gk/score/province&year={year}&signsafe='

        signsafe = execjs.compile(open('./jiemi.js','r',encoding='utf-8').read()).call('main123',url)


        json_data = {
            'e_sort': 'zslx_rank,min',
            'e_sorttype': 'desc,desc',
            'local_province_id': local_province_id,
            'local_type_id': local_type_id,
            'page': page,
            'school_id': school_id,
            'signsafe': signsafe,
            'size': 10,
            'uri': 'apidata/api/gk/score/province',
            'year': year,
        }

        url = url + signsafe
        try:
            response = requests.post(url=url,headers=headers,proxies=proxies,json=json_data).json()
        except Exception as e:
            print(e)
            continue
        items = response['data']['item']

        all_items.extend(items)

        num+=1
        print(num)

        if num % 1000==0:
            df = pd.DataFrame(all_items)

            df.to_csv('高校分数数据2022.csv', index=False, mode='a',
                      header=not os.path.exists('高校分数数据2022.csv'))

            all_items.clear()




if all_items:
    df = pd.DataFrame(all_items)
    df.to_csv('高校分数数据2022.csv', index=False, mode='a', header=not os.path.exists('高校分数数据2022.csv'))

print('所有数据已保存！')