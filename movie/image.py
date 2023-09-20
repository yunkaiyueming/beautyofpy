from PIL import ImageFont,Image,ImageDraw
import os

##给图片加文字
def create_png_with_txt():
    ###os.chdir(r'C:\Users\hp\Desktop\gif示例')

    #设置字体和字号大小
    ###font = ImageFont.truetype('simhei.ttf',200)
    font =ImageFont.truetype("hwfs.ttf",26)

    for idx in range(10):
        im1=Image.open('./seed.png')

        #在图片上添加文字
        draw = ImageDraw.Draw(im1)
        draw.text((200,150),str(idx),(0,0,0),font)

        draw = ImageDraw.Draw(im1)

        #保存图片
        im1.save('./'+str(idx)+".png")

##裁剪图片
def cropImg(dir):
    for x in range(20):
        img = Image.open("./baidu/"+dir+"/"+str(x)+".jpg")
        print(img.size)
        cropped = img.crop((0, 0, 500, 500))  # (left, upper, right, lower) kuan ,gao 
        cropped.save("./baidu/"+dir+"/"+str(x)+"_1.jpg")
        os.remove("./baidu/"+dir+"/"+str(x)+".jpg")

