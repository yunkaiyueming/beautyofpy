#coding=utf8

import tushare as ts
import warnings

def use_ts():
        print ts.__version__
        data = ts.get_sz50s()
        print data
       # print help(data)
        #print dir(data)
        #print ts.get_hs300s()

if __name__ == '__main__':
        warnings.filterwarnings("ignore") #忽略warning

        use_ts()


