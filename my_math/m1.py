import math

base16 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E","F"]

##根据16的x次方公式，每次获得尾部部分，知道整除完
##3*16^2 + 14*16^1 + 8*16^0
def Tenconvert16(num):
    base16str = ""
    round = 1
    while num>0:
        last= num % math.pow(16, round)  ##取的余数部分
        last = int(last / math.pow(16, round-1)) ##取余数下阶的整数部分
        print(round, last)
        convstr = str(base16[last])
        
        base16str = str(convstr) + str(base16str)
        num = num - last * math.pow(16, round-1) ##取得剩余值

        round = round+1

    return base16str

##循环除以16，直到整数部分为0，然后逆序取余数
def Ten2convert16(num):
    base16str=""
    while True:
        last= num % 16  ##循环除以16
        
        print(last)
        convstr = str(base16[last])
        base16str = str(convstr) + str(base16str)

        # if num<16:
        #     break
        num = int(num/16) ##取整数部分，知道整数部分为0
        if num==0:
            break

    return base16str

def Tenconvert2(num):
    base16str = ""
    round = 1
    while num>0:
        last= num % math.pow(2, round)
        last = int(last / math.pow(2, round-1))
        print(round, last)
        convstr = str(base16[last])
        
        base16str = str(convstr) + str(base16str)
        num = num - last * math.pow(2, round-1)

        round = round+1

    return base16str

def TenconvertY(num, y):
    base16str = ""
    round = 1
    while num>0:
        last= num % math.pow(y, round)
        last = int(last / math.pow(y, round-1))
        print(round, last)
        convstr = str(base16[last])
        
        base16str = str(convstr) + str(base16str)
        num = num - last * math.pow(y, round-1)

        round = round+1

    return base16str


def xConvert10(x, num):
    round = 0
    num = str(num)
    total = 0
    while num!="":
        last = num[len(num)-1]
        print(round, last)
        last = findInxInBase(last)
        last = int(last) * math.pow(x, int(round))
        total = total + last
        num = num[0:len(num)-1]
        round = round+1
    return int(total)

def findInxInBase(str):
    for i in range(len(base16)):
        if str == base16[i]:
            return i
    return -1

def XConvertY(x, num, y):
    if y==10:
        return xConvert10(x, num)
    else:
        return TenconvertY(xConvert10(x, num), y)

print(Tenconvert16(100)) ##64
print(Tenconvert16(1000)) ##3E8
print(Tenconvert16(10000)) ##2710

# print(Tenconvert2(100)) ##64

# print(xConvert10(16, 2710))
# print(xConvert10(16, "3E8"))

# print(XConvertY(12,'456789AB', 7))


# print(Ten2convert16(100)) ##64
# print(Ten2convert16(1000)) ##3E8
# print(Ten2convert16(10000)) ##2710
