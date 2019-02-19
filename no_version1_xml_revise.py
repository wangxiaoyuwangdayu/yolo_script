import xml.etree.ElementTree as ET
import glob

path = 'E:/qinxiedaoduan/ceshi2/Annotations/'
#path = 'E:/qinxiedaoduan/ceshi2/xml/'
items = glob.glob(path+'*.xml')
n=0
for item in items:
    tree = ET.parse(item)
    root = tree.getroot()
# for child in root:
#     print(child.tag,child.attrib) 访问开头信息<  >里的内容
# for i in root.iter('folder'):  访问<folder  >里的内容
#     print(i.attrib)
    root[0].text = "VOC2007"#.text显示folder<>zhi<>的值，而attrib是<annotation verified="no">folder后面的一串字典
    #print(root[0].text)
    if len(root[1].text) == 5:
        root[1].text = root[1].text + '.jpg'
    tree.write(item)
    n=n+1
print(n,'ok')
