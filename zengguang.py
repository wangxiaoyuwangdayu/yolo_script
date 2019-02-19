import matplotlib.pyplot as plt
from PIL import Image
from keras.preprocessing import image
import glob
# path为要增广的数据路径，目录下必须有子文件夹
# 设置生成器参数
#featurewise_center=True,featurewise_std_normalization=True 去中心化、除以标准差：标准化处理，变暗
#zca_whitening=True  降维操作，保留最重要特征 ？？？不用
#rotation_range=30    在0到30随机旋转
#width_shift_range=0.5,height_shift_range=0.5   水平、上下位置平移【0，最大平移距离】随机，最大平移=长*宽*参数
#shear_range=0.5   x不变y平移或交换
#zoom_range=0.5 或list【2,2】   在长或宽方向进行放缩  小于1是放大
#channel_shift_range=10   改变图片颜色  值越大，颜色越深
#horizontal_flip=True    随机水平翻转  vertical_flip=True用不到
#fill_mode=“reflect”、“wrap”、“nearest”、“constant” 不同填充

datagen = image.ImageDataGenerator(zoom_range=0.3,
                                   #horizontal_flip=True,
                                   rotation_range=15,
                                   width_shift_range=0.3,height_shift_range=0.3,
                                   channel_shift_range=10,
                                   fill_mode='constant')
path = 'E:/yunnan_research/zengguang'
gen_data = datagen.flow_from_directory(path,
                                       batch_size=1,
                                       shuffle=False,
                                       save_format='jpeg',
                                       save_to_dir='E:/yunnan_research/zg_shilie',
                                       save_prefix='daoduan',
				      target_size=(1134,2016))

# 生成n张图
p=4
q=p*8
for i in range(q):
    gen_data.next()
