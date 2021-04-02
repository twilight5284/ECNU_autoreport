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
        "",
        "",
        "",
        ""
    ]
    # 引号中填入对应的四个data值
    datapraram = [
        "",
        "",
        "",
        ""
    ]
    # 引号中填入对应的openkey值
    openkeys = [
        ""
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
        ""
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
    if message == 'ok' :
        result = '主人，打卡成功咯'
    elif message == '今日已打卡':
        result = '主人，已经打卡咯'
    else:
        result = '主人，自己打卡呗；\n我出糗啦：%s，快来救我' % (message)
    # 引号中填入sckey值
    ServerKey = [
        ""
    ]
    push_message(result, ServerKey)


if __name__ == "__main__":
        i = random.randint(1, 4)
        time.sleep(i * 55)
        ECNU_autoreport()
