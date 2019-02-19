'''
Created on 2018.12.10
@author:王甲鱼
'''
from PIL import Image
import cv2
import numpy as np
import operator

class Image_combine(object):
    def __init__(self,front_imagepath,back_imagepath,coordinate):
        self.front_imagepath = front_imagepath
        self.back_imagepath = back_imagepath
        self.coordinate = coordinate

    def white_front_add(self):
        back_img = Image.open(self.back_imagepath)#获得原图大小
        white_img = np.zeros((back_img.size[1],back_img.size[0],3), np.uint8)
        white_img.fill(255)#生成空白画布
        cv2.imwrite("E:/combine_ceshi/white_img.jpg",white_img)
        white_img = Image.open("E:/combine_ceshi/white_img.jpg")
        #white_img = white_img.convert('RGBA')
        front_img = Image.open(self.front_imagepath)
        #front_img = front_img.convert('RGBA')
        front_img_h,front_img_w = front_img.size
        box = (self.coordinate[0],self.coordinate[1],
               self.coordinate[0]+front_img_h,self.coordinate[1]+front_img_w)
        white_img.paste(front_img,box)
        white_img.save("E:/combine_ceshi/add_img.jpg")
        #return add_img

    def combine(self):
        self.white_front_add()
        back_img = Image.open(self.back_imagepath)
        #back_img = back_img.convert('RGBA')
        add_img = Image.open("E:/combine_ceshi/add_img.jpg")
        #add_img = add_img.convert('RGBA')
        for w in range(add_img.size[1]):
            for h in range(add_img.size[0]):
                #print(type(add_img[1,1]))
                dot = (h,w)
                if (add_img.getpixel(dot)[0]<255 or add_img.getpixel(dot)[1]<255 or add_img.getpixel(dot)[2]<255):
                #if list(add_img[h,w])[0]<245 and list(add_img[h,w])[1]<245 and list(add_img[h,w])[2]<245:
                #if operator.eq(list(add_img[h,w]),[255,255,255]) == False:
                    #back_img[h,w] = add_img[h,w]
                    back_img.putpixel(dot,add_img.getpixel(dot))
        return back_img

if __name__ == "__main__":
    front_imagepath = "E:/combine_ceshi/temp8.jpg"
    back_imagepath = "E:/combine_ceshi/ganta.jpg"
    coordinate = [50,50]
    Combine = Image_combine(front_imagepath,back_imagepath,coordinate)
    combine_image = Combine.combine()
    combine_image.save("E:/combine_ceshi/combine_image.jpg")


