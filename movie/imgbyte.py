import io
import base64
from PIL import Image
import numpy as np

def image2byte(image_path):
    '''
    图片转byte
    image: 必须是PIL格式
    image_bytes: 二进制
    '''
    image = Image.open(image_path)
    # 创建一个字节流管道
    img_bytes = io.BytesIO()
    #把PNG格式转换成的四通道转成RGB的三通道，然后再保存成jpg格式
    image = image.convert("RGB")
    # 将图片数据存入字节流管道， format可以按照具体文件的格式填写
    image.save(img_bytes, format="JPEG")
    # 从字节流管道中获取二进制
    image_bytes = img_bytes.getvalue()
    return image_bytes

def byte2image(byte_data):
    '''
    byte转为图片
    byte_data: 二进制
    '''
    image = Image.open(io.BytesIO(byte_data))
    return image



def read2byte(path):
    '''
    图片转二进制
    path：图片路径
    byte_data：二进制数据
    '''
    with open(path,"rb") as f:
        byte_data = f.read()
    return byte_data


image_path = "unnamed.jpg"
# byte_data = image2byte(image_path) #把图片转换成二进制
# print('0x%d',byte_data)
# image2 = byte2image(byte_data) #把二进制转成图片

byte_data = read2byte(image_path)
print(byte_data)