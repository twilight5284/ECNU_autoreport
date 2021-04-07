# -*- coding = utf-8 -*-
# @Time : 2021/4/2 14:55
# @Author : twili
# @File : ECNU.py
# @Software : PyCharm

import json
import requests
import time
import datetime
from requests.packages import urllib3
import random

urllib3.disable_warnings()

def push_message(message, token):
    sendUrl = f'http://sc.ftqq.com/{token}.send?text={message}'
    requests.get(sendUrl)

def get_MiniToken(N):
    url1 = "https://anti-epidemic.ecnu.edu.cn/clock/mini/wx"
    # 引号中填入四个iv值
    ivparams = [
        "p0kEInI2/lI+a9ae9XvqYA==",
        "9RUWS3cDvhElV8NhZ9AKKQ==",
        "ANYaBd8A0NaQ9guAHdZjrw==",
        "33g8BLhAQQC8qkaN+cBVLw=="
    ]
    # 引号中填入对应的四个data值
    datapraram = [
        "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"
    ]
    # 引号中填入对应的openkey值
    openkeys = [
        "606d720ee3c3f536e09644bd"
    ]
    # 随机选取iv和data
    n = random.randint(0, 3)
    params1 = {
        "open_key": openkeys,
        "iv": ivparams[n],
        "data": datapraram[n]
    }
    headers1 = {
        "Host": "anti-epidemic.ecnu.edu.cn",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "content-type": "application/json",
        "Referer": "https://servicewechat.com/wxfcaebbc17bdc154b/27/page-frame.html",
        "Accept-Encoding": "gzip, deflate, br"
    }
    # 获取MiniToken
    body1 = requests.get(url=url1,headers = headers1,params=params1,verify=False)
    r=body1.json()
    return(r)

def ECNU_autoreport():
    url2 = "https://anti-epidemic.ecnu.edu.cn/clock/mini/record"
    headers2 = {
        "Host": "anti-epidemic.ecnu.edu.cn",
        "Connection": "keep-alive",
        "Content-Length": "151",
        "MiniToken": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJudW1iZXIiOiI1MjE4MzkwNDAyNiIsImlzcyI6IkVDTlUiLCJuYW1lIjoi546L6buOIiwiZXhwIjoxNjE2Njg4MTg4fQ.f0A4p4TCeiC71pIhpd6uUGZaFUcg2gWtkm3Rdm9mfBw",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "content-type": "application/json",
        "Referer": "https://servicewechat.com/wxfcaebbc17bdc154b/27/page-frame.html",
        "Accept-Encoding": "gzip, deflate, br"
    }
    r = get_MiniToken(N)
    # 替换MiniToken
    headers2["MiniToken"]=r["message"]
    # 引号中填入学号
    studentnumber = [
        "51203904020"
    ]
    # 引号中填入token
    studenttoken = [
        ""
    ]
    # 获取13位时间戳并替换
    millis = int(round(time.time() * 1000))
    body2={"number":studentnumber,"location":"在学校","health":"健康，未超过37.3","recordTime":millis,"token":studenttoken}
    # 用put完成打卡
    body3 = requests.put(url=url2,headers = headers2,json=body2)
    # 获取返回的信息
    message = body3.json()["message"]
    if message in ['ok','Ok','OK']:
        result = '主人，打卡成功咯'
    elif message == '今日已打卡':
        result = '主人，已经打卡咯'
    else:
        result = '主人，自己打卡呗；\n我出糗啦：%s，快来救我' % (message)
    # 引号中填入sckey值
    ServerKey = [
        "SCU168445Ta8fc146d5c37693c90406ce8b4de3003606d9be55277c
"
    ]
    push_message(result, ServerKey)


if __name__ == "__main__":
        time.sleep(30)
        ECNU_autoreport()
