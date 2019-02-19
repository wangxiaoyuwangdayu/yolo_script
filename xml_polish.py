from PIL import Image
import xml.dom.minidom
import os
import os.path

#该版本xml文件数和图片数一一对应
#标注生成xml文件时，图像的大小可能丢失，该脚本获得图片大小，补充进xml文件相应位置
#img_path为丢失信息的图像的路径
#path为丢失信息的xml文件的路径
#确保图像文件顺序和xml文件顺序一致
e0=[]
e1=[]
img_path = "E:/yunnan_research/pic_train/"
img_files = os.listdir(img_path)
for name in img_files:
    print(name)
    img = Image.open(os.path.join(img_path,name))
    d=img.size
    e0.append(d[0])
    e1.append(d[1])
path ="E:/yunnan_research/xml_file_shiyan/"
files=os.listdir(path)  #得到文件夹下所有文件名称
s=[]
k=0
for xmlFile in files: #遍历文件夹
    if not os.path.isdir(xmlFile): #判断是否是文件夹,不是文件夹才打开
        print (xmlFile)
	#将获取的xml文件名送入到dom解析
        dom=xml.dom.minidom.parse(os.path.join(path,xmlFile))  ###最核心的部分os.path.join(path,xmlFile),路径拼接,输入的是具体路径
        root=dom.documentElement
        #获取标签对name/pose之间的值
        name=root.getElementsByTagName('width')
        name0=name[0]
        print("wrong width:",name0.firstChild.data)
        name0.firstChild.data=e0[k]
        wang=root.getElementsByTagName('height')
        wang0=wang[0]
        print("wrong height:",wang0.firstChild.data)
        wang0.firstChild.data=e1[k]
        k=k+1
        #保存修改到xml文件中
        with open(os.path.join(path,xmlFile),'w') as fh:
            dom.writexml(fh)
            print('OK!')



