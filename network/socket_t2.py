#-*- coding:utf-8 -*-    --------------Ashare 股票行情数据双核心版( https://github.com/mpquant/Ashare ) 
import json,requests,datetime,time;      
import pandas as pd
import requests
import json

#腾讯日线
def get_price_day_tx(code, end_date='', count=10, frequency='1d'):     #日线获取  
    unit='week' if frequency in '1w' else 'month' if frequency in '1M' else 'day'     #判断日线，周线，月线
    if end_date:  end_date=end_date.strftime('%Y-%m-%d') if isinstance(end_date,datetime.date) else end_date.split(' ')[0]
    end_date='' if end_date==datetime.datetime.now().strftime('%Y-%m-%d') else end_date   #如果日期今天就变成空    
    URL=f'http://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param={code},{unit},,{end_date},{count},qfq'     
    st= json.loads(requests.get(URL).content);    ms='qfq'+unit;      stk=st['data'][code]   
    buf=stk[ms] if ms in stk else stk[unit]       #指数返回不是qfqday,是day
    df=pd.DataFrame(buf,columns=['time','open','close','high','low','volume'],dtype='float')     
    df.time=pd.to_datetime(df.time);    df.set_index(['time'], inplace=True);   df.index.name=''          #处理索引 
    return df

#腾讯分钟线
def get_price_min_tx(code, end_date=None, count=10, frequency='1d'):    #分钟线获取 
    ts=int(frequency[:-1]) if frequency[:-1].isdigit() else 1           #解析K线周期数
    if end_date: end_date=end_date.strftime('%Y-%m-%d') if isinstance(end_date,datetime.date) else end_date.split(' ')[0]        
    URL=f'http://ifzq.gtimg.cn/appstock/app/kline/mkline?param={code},m{ts},,{count}' 
    st= json.loads(requests.get(URL).content);       buf=st['data'][code]['m'+str(ts)] 
    df=pd.DataFrame(buf,columns=['time','open','close','high','low','volume','n1','n2'])   
    df=df[['time','open','close','high','low','volume']]    
    df[['open','close','high','low','volume']]=df[['open','close','high','low','volume']].astype('float')
    df.time=pd.to_datetime(df.time);   df.set_index(['time'], inplace=True);   df.index.name=''          #处理索引     
    df['close'][-1]=float(st['data'][code]['qt'][code][3])                #最新基金数据是3位的
    return df

#sina新浪全周期获取函数，分钟线 5m,15m,30m,60m  日线1d=240m   周线1w=1200m  1月=7200m
def get_price_sina(code, end_date='', count=10, frequency='60m'):    #新浪全周期获取函数    
    frequency=frequency.replace('1d','240m').replace('1w','1200m').replace('1M','7200m');   mcount=count
    ts=int(frequency[:-1]) if frequency[:-1].isdigit() else 1       #解析K线周期数
    if (end_date!='') & (frequency in ['240m','1200m','7200m']): 
        end_date=pd.to_datetime(end_date) if not isinstance(end_date,datetime.date) else end_date    #转换成datetime
        unit=4 if frequency=='1200m' else 29 if frequency=='7200m' else 1    #4,29多几个数据不影响速度
        count=count+(datetime.datetime.now()-end_date).days//unit            #结束时间到今天有多少天自然日(肯定 >交易日)        
        #print(code,end_date,count)    
    URL=f'http://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData?symbol={code}&scale={ts}&ma=5&datalen={count}' 
    dstr= json.loads(requests.get(URL).content);       
    #df=pd.DataFrame(dstr,columns=['day','open','high','low','close','volume'],dtype='float') 
    df= pd.DataFrame(dstr,columns=['day','open','high','low','close','volume'])
    df['open'] = df['open'].astype(float); df['high'] = df['high'].astype(float);                          #转换数据类型
    df['low'] = df['low'].astype(float);   df['close'] = df['close'].astype(float);  df['volume'] = df['volume'].astype(float)    
    df.day=pd.to_datetime(df.day);    df.set_index(['day'], inplace=True);     df.index.name=''            #处理索引                 
    if (end_date!='') & (frequency in ['240m','1200m','7200m']): return df[df.index<=end_date][-mcount:]   #日线带结束时间先返回              
    return df

def get_price(code, end_date='',count=10, frequency='1d', fields=[]):        #对外暴露只有唯一函数，这样对用户才是最友好的  
    xcode= code.replace('.XSHG','').replace('.XSHE','')                      #证券代码编码兼容处理 
    xcode='sh'+xcode if ('XSHG' in code)  else  'sz'+xcode  if ('XSHE' in code)  else code     

    if  frequency in ['1d','1w','1M']:   #1d日线  1w周线  1M月线
         try:    return get_price_sina( xcode, end_date=end_date,count=count,frequency=frequency)   #主力
         except: return get_price_day_tx(xcode,end_date=end_date,count=count,frequency=frequency)   #备用                    
    
    if  frequency in ['1m','5m','15m','30m','60m']:  #分钟线 ,1m只有腾讯接口  5分钟5m   60分钟60m
         if frequency in '1m': return get_price_min_tx(xcode,end_date=end_date,count=count,frequency=frequency)
         try:    return get_price_sina(  xcode,end_date=end_date,count=count,frequency=frequency)   #主力   
         except: return get_price_min_tx(xcode,end_date=end_date,count=count,frequency=frequency)   #备用

def get_zhangfu(today, yesterday):
    if int(yesterday)==0: return 'unknow'
    return str(round((today-yesterday)/yesterday*100,2)) + "%"

def send_monitor_msg(content):
    ## headers中添加上content-type这个参数，指定为json格式
    headers = {'Content-Type': 'application/json'}

    data = {
    "appToken":"AT_IkWT5MuswFoluyqe6gSLiutoAtv98GGH",
    "content":content,
    "summary":"今日大盘",#消息摘要，显示在微信聊天页面或者模版消息卡片上，限制长度100，可以不传，不传默认截取content前面的内容。
    "contentType":1,#内容类型 1表示文字  2表示html(只发送body标签内部的数据即可，不包括body标签) 3表示markdown 
    # "topicIds":[ #发送目标的topicId，是一个数组！！！，也就是群发，使用uids单发的时候， 可以不传。
    #     123
    # ],
    "uids":[#发送目标的UID，是一个数组。注意uids和topicIds可以同时填写，也可以只填写一个。
        "UID_3MMgxGOVOOw7cO35lb8WkyqIRpb5"
    ],
    "url":"https://baidu.com", #原文链接，可选参数
    "verifyPay":False #是否验证订阅时间，true表示只推送给付费订阅用户，false表示推送的时候，不验证付费，不验证用户订阅到期时间，用户订阅过期了，也能收到。
    }

    ## post的时候，将data字典形式的参数用json包转换成json格式。
    response = requests.post(url='https://wxpusher.zjiecode.com/api/send/message', headers=headers, data=json.dumps(data))

def get_can_yesterday(day, data):
    for x in range(6):
        yesterday = day - datetime.timedelta(days=x)
        yesterday_str = yesterday.strftime('%Y-%m-%d')
        # print('can_yesterday',yesterday_str)
        if yesterday_str in data:
            return yesterday_str
    return 0

def get_fromate_by_code(code):
    df=get_price(code,frequency='1d',count=6)      #支持'1d'日, '1w'周, '1M'月  
    # print('上证指数日线行情\n',df)
    
    data = {}
    for idx,item in df.iterrows():
        # print(idx.strftime('%Y-%m-%d'),type(idx))
        # print(item['close'])
        date = idx.strftime('%Y-%m-%d')

        date_info = {"close":item['close'], 'zf':0}
        data[date] = date_info

    # today = datetime.datetime.now().date()
    # print("当前日期：", current_date)

    formate_str = ""
    # print(data)
    for x in data:
        timeArr = time.strptime(x,'%Y-%m-%d')
        unixtime = time.mktime(timeArr)
        today = datetime.datetime.utcfromtimestamp(unixtime)
        # print('x', x, today)

        canyestday = get_can_yesterday(today, data)

        # print('x', x, canyestday)
        if canyestday!=0:
            data[x]['canyestday'] = canyestday
            data[x]['zf'] = get_zhangfu(data[x]['close'], data[canyestday]['close'])

            tmp_str = x + "     " + str(data[x]['close']) + "     " + data[x]['zf'] + "\n"
            formate_str = formate_str + tmp_str
        else:
            data[x]['canyestday'] = ''
            data[x]['zf'] = 'unknow'
        
    return formate_str

if __name__ == '__main__':
    codes = ['sh000001','sh600585','sh600009','sh601318','sz000651','sh600276']
    code_desc = {'sh000001':'上证指数' ,"sh600585":"海螺水泥", "sh600009":"上海机场", "sh601318":"中国平安", 'sz000651':'格力电器', 'sh600276':'恒瑞医药'}
    code_fromate_str = ""
    for x in codes:
        print(x)
        code_str = code_desc[x] +" 近5日股价："+ "\n" + get_fromate_by_code(x) + "\n\n"
        code_fromate_str = code_fromate_str + code_str
    
    send_monitor_msg(code_fromate_str)

    # df=get_price('000001.XSHG',frequency='15m',count=10)  #支持'1m','5m','15m','30m','60m'
    # print('上证指数分钟线\n',df)

# Ashare 股票行情数据( https://github.com/mpquant/Ashare ) 