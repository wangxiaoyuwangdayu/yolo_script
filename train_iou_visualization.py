import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

log_path='E:/log_ceshi/keras_kmeans_log/train_log_iou.txt'
# lines=len(open(log_path,'r').readlines())#读取文件行数。行数较少时使用该方法
#文件较大时采用下面方法
lines = 0
for index, line in enumerate(open(log_path,'r')):
    lines += 1

result = pd.read_csv(log_path,
                     error_bad_lines=False, names=['Region Avg IOU', 'Class', 'Obj', 'No Obj', '0.5 Recall', '0.7 Recall','count'])
                    # skiprows=[x for x in range(lines) if (x%10==0 or x%10==9) ] ,

result['Region Avg IOU']=result['Region Avg IOU'].str.split(': ').str.get(1)
result['Class']=result['Class'].str.split(': ').str.get(1)
result['Obj']=result['Obj'].str.split(': ').str.get(1)
result['No Obj']=result['No Obj'].str.split(': ').str.get(1)
result['0.5 Recall']=result['0.5 Recall'].str.split(': ').str.get(1)
result['0.7 Recall']=result['0.7 Recall'].str.split(': ').str.get(1)
#result['count']=result['count'].str.split(': ').str.get(1)

result['Region Avg IOU']=pd.to_numeric(result['Region Avg IOU'])
result['Class']=pd.to_numeric(result['Class'])
result['Obj']=pd.to_numeric(result['Obj'])
result['No Obj']=pd.to_numeric(result['No Obj'])
result['0.5 Recall']=pd.to_numeric(result['0.5 Recall'])
result['0.7 Recall']=pd.to_numeric(result['0.7 Recall'])
#result['count']=pd.to_numeric(result['count'])

plt.rcParams['font.sans-serif']=['Times New Roman']
fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot(1, 1, 1)
y_data = result['0.5 Recall'].values[::50]   #iou,class:50 recll 200
x_data = np.linspace(0,10000,len(y_data),endpoint=True)#range(len(y_data))
ax.scatter(x_data,y_data,marker = 'o', color = 'red', s = 0.5,label='0.5 Recall')
# ax.legend(loc='best')
# ax.set_title('The Region Avg IOU curves')
# ax.set_xlabel('batches')
plt.tick_params(direction='in')
plt.xticks(fontsize=20)#,fontweight='bold') #默认字体大小为10
plt.yticks(fontsize=20)#,fontweight='bold')
fig.savefig('E:/log_ceshi/keras_kmeans_log/10.5 Recall.jpg',dpi=400,bbox_inches='tight')#,format='svg')

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(result['Region Avg IOU'].values,label='Region Avg IOU')
# ax.legend(loc='best')
# ax.set_title('The Region Avg IOU curves')
# ax.set_xlabel('batches')
# fig.savefig('E:/log_ceshi/gydq_paper/The Region Avg IOU curves')

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.scatter(range(len(result['Class'].values)),result['Class'].values,marker = 'o', color = 'grey', s = 0.5,label='Class')
# ax.legend(loc='best')
# ax.set_title('The Class curves')
# ax.set_xlabel('batches')
# fig.savefig('E:/log_ceshi/gydq_paper/The Class curves')

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(result['Obj'].values,label='Obj')
# ax.legend(loc='best')
# ax.set_title('The Obj curves')
# ax.set_xlabel('batches')
# fig.savefig('E:/log_ceshi/gydq_paper/The Obj curves')
#
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(result['No Obj'].values,label='No Obj')
# ax.legend(loc='best')
# ax.set_title('The No Obj curves')
# ax.set_xlabel('batches')
# fig.savefig('E:/log_ceshi/gydq_paper/The No Obj curves')
#
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(result['0.5 Recall'].values,label='0.5 Recall')
# ax.legend(loc='best')
# ax.set_title('The 0.5 Recall curves')
# ax.set_xlabel('batches')
# fig.savefig('E:/log_ceshi/gydq_paper/0.5_Recall curves.png')
#
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(result['0.7 Recall'].values,label='0.7 Recall')
# ax.legend(loc='best')
# ax.set_title('The 0.7 Recall curves')
# ax.set_xlabel('batches')
#
# #fig.tight_layout()
# fig.savefig('E:/log_ceshi/gydq_paper/0.7_Recall curves.png')
