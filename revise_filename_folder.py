import xml.dom.minidom as xdm
import glob
import os
import os.path

path = 'E:/qinxiedaoduan/ceshi2/Annotations/'
#path = 'E:/qinxiedaoduan/ceshi2/xml/'

items = glob.glob(path+'*.xml')

#train_txt = 'train.txt'
'''
#path ="E:/qinxiedaoduan/VOCdevkit/VOC2007/Annotations"
files=os.listdir(path)  #得到文件夹下所有文件名称
for xmlFile in files:
    dom=xdm.parse(os.path.join(path,xmlFile))
    root = dom.documentElement

    # change folder name
    folder_dom = root.getElementsByTagName('folder')
    print(folder_dom[0].firstChild.data)
    folder_dom[0].firstChild.data = 'VOC2007'

    # change image name
    image_dom = root.getElementsByTagName('filename')
    print(image_dom[0].firstChild.data)
   # with open(train_txt, 'a+') as f:
   #     f.write(image_dom[0].firstChild.data)
   #     f.write('\n')
    if len(image_dom[0].firstChild.data)==5:
        image_dom[0].firstChild.data = image_dom[0].firstChild.data + '.jpg'
    #image_dom[0].firstChild.data = image_dom[0].firstChild.data + '.jpg'
    with open(os.path.join(path,xmlFile), 'w') as f:
        dom.writexml(f)#,encoding='utf-8')
'''

for item in items:
    dom = xdm.parse(item)
    root = dom.documentElement

    # change folder name
    folder_dom = root.getElementsByTagName('folder')
    print(folder_dom[0].firstChild.data)
    folder_dom[0].firstChild.data = 'VOC2007'

    # change image name
    image_dom = root.getElementsByTagName('filename')
    print(image_dom[0].firstChild.data)
   # with open(train_txt, 'a+') as f:
   #     f.write(image_dom[0].firstChild.data)
   #     f.write('\n')
    if len(image_dom[0].firstChild.data)==5:
        image_dom[0].firstChild.data = image_dom[0].firstChild.data + '.jpg'
    #image_dom[0].firstChild.data = image_dom[0].firstChild.data + '.jpg'
    with open(item, 'w') as f:
        dom.writexml(f)#,encoding='utf-8')
