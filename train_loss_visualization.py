import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

log_path='E:/log_ceshi/keras_kmeans_log/train_log_loss.txt'
# lines=len(open(log_path,'r').readlines())#读取文件行数。行数较少时使用该方法
#文件较大时采用下面方法
lines = 0
for index, line in enumerate(open(log_path,'r')):
    lines += 1

result = pd.read_csv(log_path,
                     error_bad_lines=False, names=['loss', 'avg', 'rate', 'seconds', 'images'])
                    #skiprows需要忽略或跳过的行号    names：用于结果的列名列表，如果数据文件中没有列标题行，就要执行header=None
                    #skiprows=[x for x in range(lines) if ((x%10!=9) |(x<1000))] ,

result['loss']=result['loss'].str.split(' ').str.get(1)
result['avg']=result['avg'].str.split(' ').str.get(1)#应为是以空格开头，所有get（0）是索引号
result['rate']=result['rate'].str.split(' ').str.get(1)
result['seconds']=result['seconds'].str.split(' ').str.get(1)
result['images']=result['images'].str.split(' ').str.get(1)

result['loss']=pd.to_numeric(result['loss'])    #pd.to_numeric将其他数据转为整数型(浮点型？）数据
result['avg']=pd.to_numeric(result['avg'])
result['rate']=pd.to_numeric(result['rate'])
result['seconds']=pd.to_numeric(result['seconds'])
result['images']=pd.to_numeric(result['images'])

plt.rcParams['font.sans-serif']=['Times New Roman']
fig = plt.figure(figsize=(8,5))#800*400
ax = fig.add_subplot(1, 1, 1)
y_data = result['avg'].values[:2000]
x_data = np.linspace(0,10000,len(y_data),endpoint=True)#range(len(y_data))
ax.scatter(x_data,y_data,marker = 'o', color = 'red', s = 1,label='avg_loss')
plt.tick_params(direction='in')
plt.xticks(fontsize=20)#,fontweight='bold') #默认字体大小为10
plt.yticks(fontsize=20)#,fontweight='bold')
#ax.legend(loc='best')
#ax.set_title('The avg_loss curves')
#ax.set_xlabel('batches')
fig.savefig('E:/log_ceshi/keras_kmeans_log/1The avg_loss curves.jpg',dpi=400,bbox_inches='tight')

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)#将画布分割成1行1列，图像画在从左到右从上到下的第1块
# ax.plot(result['avg'].values[:2000],label='avg_loss') # .value变成一个列表,label是图例
# ax.legend(loc='best')  #图例自适应
# ax.set_title('The avg_loss curves')
# ax.set_xlabel('batches')
# fig.savefig('E:/log_ceshi/gydq_paper/The avg_loss curves')
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(result['loss'].values[:2000],label='loss')
# ax.legend(loc='best')  #图例自适应
# ax.set_title('The loss curves')
# ax.set_xlabel('batches')
# fig.savefig('E:/log_ceshi/gydq_paper/The loss curves')
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(result['rate'].values[:2000],label='rate')
# ax.legend(loc='best')  #图例自适应
# ax.set_title('The rate curves')
# ax.set_xlabel('batches')
# fig.tight_layout()#调整整体空白,自动调整subplot间的参数
# fig.savefig('E:/log_ceshi/gydq_paper/The rate curves')
