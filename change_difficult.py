'''
统一xml文件中的difficult和Difficult
'''
import xml.etree.ElementTree as ET
from PIL import Image
import xml.dom.minidom
import os
import os.path

path ="E:/qinxiedaoduan/VOCdevkit/VOC2007/Annotations"
files=os.listdir(path)  #得到文件夹下所有文件名称
k = 0
for xmlFile in files: #遍历文件夹
    if not os.path.isdir(xmlFile): #判断是否是文件夹,不是文件夹才打开
        print (xmlFile)
    #dom=xml.dom.minidom.parse(os.path.join(path,xmlFile))
    tree = ET.parse(os.path.join(path,xmlFile))
    root = tree.getroot()
    b=0
    for element in root.findall('object/Difficult'):
        element.tag = "difficult"
        b=1
    k=k+b
    tree.write(os.path.join(path,xmlFile))
print(k)  #k用来计数有多少个文件被修改，而不是有多少个difficult被修改