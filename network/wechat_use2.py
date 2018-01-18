#coding=utf8
#自动微信管理

# 导入模块
from wxpy import *
import urllib2
import json
import time

def start():
        msg = get_all_weather_infos()
        print(msg)
        wx_send_group(msg)

def wx_send_group(msg):
        # 初始化机器人，扫码登陆
        bot = Bot(True)

        # 搜索名称含有 "游否" 的男性深圳好友
        #my_friend = bot.friends().search(u"小白菜", sex=FEMALE)[0]
        my_friend = bot.groups().search(u"家人相亲相爱")[0]
        print(my_friend)

        # 发送文本给好友
        #my_friend.send(msg)
        embed()

def get_weather_info(url):
        response = urllib2.urlopen(url)
        decode_data = json.loads(response.read(),encoding="utf8")
        decode_data = decode_data["weatherinfo"]
        format_str = decode_data["city"]+":"+decode_data["temp1"]+"~"+decode_data["temp2"]+","+decode_data["weather"]
        #print(format_str)
        return format_str

def get_all_weather_infos():
        url1 = "http://www.weather.com.cn/data/cityinfo/101010100.html" #北京
        url2 = "http://www.weather.com.cn/data/cityinfo/101230101.html" #福州
        url3 ="http://www.weather.com.cn/data/cityinfo/101201101.html"  #十堰
        msg1 = get_weather_info(url1)+";\n"
        msg2 = get_weather_info(url2)+";\n"
        msg3 = get_weather_info(url3)

        datetime_msg = get_datetime_info()
        return datetime_msg+msg1+msg2+msg3

def get_datetime_info():
        date_time =  time.strftime("%Y-%m-%d %H:%M:%S ")
        week_num =time.strftime("%w", time.localtime())
        week_names =  [u"星期日",u"星期一" ,u"星期二",u"星期三",u"星期四",u"星期五",u"星期六"]

        datetime_msg= date_time+week_names[int(week_num)]+"\n"
        return datetime_msg

if __name__ == '__main__':
        start()
