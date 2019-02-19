import os
import operator as op
import shutil

#保证xml文件与图片文件一一对应，否则训练会有错误
#将多余的图片文件剪切到img_ret_path路径下

img_path = "E:/qinxiedaoduan/VOCdevkit/VOC2007/JPEGImages/"
xml_path = "E:/qinxiedaoduan/VOCdevkit/VOC2007/Annotations/"
img_ret_path = "E:/qinxiedaoduan/ret"
xmlfiles=os.listdir(xml_path)
imgfiles=os.listdir(img_path)
xmlname=[]
imgname=[]
for a in xmlfiles:
    xmlname.append(a[:5])
for b in imgfiles:
    imgname.append(b[:5])
ret = list(set(xmlname)^set(imgname))
print(len(ret))
for c in ret:
    fullname1=img_path+c+".jpg"
    fullname2=img_path+c+".jpeg"
    #shutil.move(os.path.join(img_path,fullname),img_ret_path)
    try:
        shutil.move(fullname1,img_ret_path)
    except:
        shutil.move(fullname2,img_ret_path)
    else:
        pass
