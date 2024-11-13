import execjs
import requests
import pandas as pd
import json

all_items = []
for i in range(1,148):

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
    page = i
    url = f'https://api.zjzw.cn/web/api/?keyword=&page={page}&province_id=&ranktype=&request_type=1&size=20&type=&uri=apidata/api/gkv3/school/lists&signsafe='
    signsafe = execjs.compile(open('./jiemi.js','r',encoding='utf-8').read()).call('main123',url)
    json_data = {
        'keyword': '',
        'page': 2,
        'province_id': '',
        'ranktype': '',
        'request_type': 1,
        'signsafe': '772a7c5ff327171f300fb5bbd7b8afa4',
        'size': 20,
        'type': '',
        'uri': 'apidata/api/gkv3/school/lists',
    }
    url = url+signsafe
    response = requests.post(
        url = url,
        headers=headers,
        json=json_data,
    ).json()

    print(response)
    # 提取数据项（这里只有一个项，但通常可能是一个列表）
    items = response['data']['item']
    all_items.extend(items)

    print(1)


df = pd.DataFrame(all_items)

# df.to_csv('高校信息.csv', index=False)

print("所有数据已成功保存")