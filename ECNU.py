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
        "Me5WT5nHnocki4Ca/9Fa1A==",
        "R6pteZZlsnCq4UzgeX/3jg==",
        "GrhLdZNN0xqFsmo9P+v1Qw==",
        "/s2LlXGlMwkxJIJLY9sGXA=="
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
        "d70de0e1d95494683d7625279a4765d9"
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
        "SCU168445Ta8fc146d5c37693c90406ce8b4de3003606d9be55277c"
    ]
    push_message(result, ServerKey)


if __name__ == "__main__":
        time.sleep(30)
        ECNU_autoreport()
