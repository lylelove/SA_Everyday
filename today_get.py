import json
import time
import requests
sa_block = ['深a', '创业板', '沪a', '科创版']
code_name = []
date = time.strftime("%Y-%m-%d", time.localtime())
date_name = time.strftime("%Y_%m_%d", time.localtime())
hd = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/99.0.4844.82 Safari/537.36'}
url1 = 'http://36.push2.eastmoney.com/api/qt/clist/get?pn=1&pz=3000&po=0&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f12&fs=m:0+t:6,m:0+t:80&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f100,f102,f128,f136,f115,f152'
url2 = 'https://36.push2.eastmoney.com/api/qt/clist/get?pn=1&pz=3000&po=0&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f12&fs=m:0+t:80&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f100,f102,f128,f136,f115,f152'
url3 = 'http://36.push2.eastmoney.com/api/qt/clist/get?pn=1&pz=3000&po=0&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f12&fs=m:1+t:2,m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f100,f102,f128,f136,f115,f152'
url4 = 'http://36.push2.eastmoney.com/api/qt/clist/get?pn=1&pz=3000&po=0&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f12&fs=m:1+t:23&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f100,f102,f128,f136,f115,f152'
url = [url1, url2, url3, url4]
for i in range(len(url)):
    response = requests.get(url[i], headers=hd)
    info = response.text
    info = json.loads(info)
    try:
        temp = info['data']['diff']
    except:
        continue
    data_all = []
    with open('data/json/' + str(sa_block[i])+str(date_name) + '.json', 'w') as f:
        for item in temp:
            data_all.append([item['f12'], item['f14'],
                             [date, item['f2'], item['f3'], item['f4'], item['f5'], item['f6'], item['f7'], item['f15'],
                              item['f16'], item['f17'], item['f8'], item['f100'], item['f102'], item['f9'],
                              item['f23']]])
        json.dump(data_all, f)
    print(str(i) + 'ok')
