import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
#%matplotlib inline

log_path='E:/yunnan_research/log_visualization/train_log_iou.txt'
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
result['count']=result['count'].str.split(': ').str.get(1)


result['Region Avg IOU']=pd.to_numeric(result['Region Avg IOU'])

result['Class']=pd.to_numeric(result['Class'])
result['Obj']=pd.to_numeric(result['Obj'])
result['No Obj']=pd.to_numeric(result['No Obj'])
result['0.5 Recall']=pd.to_numeric(result['0.5 Recall'])
result['0.7 Recall']=pd.to_numeric(result['0.7 Recall'])
result['count']=pd.to_numeric(result['count'])

def curve_fit(X,y,name):

   # X = df[['LSTAT']].values
   # y = df['MEDV'].values
    regr = LinearRegression()
    # create quadratic features
    quadratic = PolynomialFeatures(degree=2)
    cubic = PolynomialFeatures(degree=3)
    X_quad = quadratic.fit_transform(X)
    X_cubic = cubic.fit_transform(X)
    # fit features
    X_fit = np.arange(X.min(), X.max(), 1)[:, np.newaxis]

    regr = regr.fit(X, y)   #X,y训练数据集建模；X_fit测试数据集预测；对训练数据集测试得分(因为有时根本不知道测试数据集对应的真实y值)
    y_lin_fit = regr.predict(X_fit)
    linear_r2 = r2_score(y, regr.predict(X))

    regr = regr.fit(X_quad, y)
    y_quad_fit = regr.predict(quadratic.fit_transform(X_fit))
    quadratic_r2 = r2_score(y, regr.predict(X_quad))

    regr = regr.fit(X_cubic, y)
    y_cubic_fit = regr.predict(cubic.fit_transform(X_fit))
    cubic_r2 = r2_score(y, regr.predict(X_cubic))

    # plot results
    plt.scatter(X, y, label='training points', color='lightgray')
    plt.plot(X_fit, y_lin_fit, label='linear (d=1), $R^2=%.2f$' % linear_r2, color='blue', lw=2, linestyle=':')
    plt.plot(X_fit, y_quad_fit, label='quadratic (d=2), $R^2=%.2f$' % quadratic_r2, color='red', lw=2, linestyle='-')
    plt.plot(X_fit, y_cubic_fit, label='cubic (d=3), $R^2=%.2f$' % cubic_r2, color='green', lw=2, linestyle='--')
    plt.xlabel('batches')
    plt.ylabel(name)
    plt.legend(loc='upper left')
    plt.tight_layout()
    path_front = 'E:/yunnan_research/log_visualization/pic_back/'
    path_all = path_front + name +'.png'
    plt.savefig(path_all)
    plt.show()

y_data1 = result['Region Avg IOU'][:70000].values
x_data1 = np.arange(0,len(y_data1),1)[:, np.newaxis]
#print(len(y_data),type(y_data),y_data.shape)
y_data2 = result['Class'][:70000].values
x_data2 = np.arange(0,len(y_data2),1)[:, np.newaxis]

y_data3 = result['Obj'][:70000].values
x_data3 = np.arange(0,len(y_data3),1)[:, np.newaxis]

y_data4 = result['No Obj'][:70000].values
x_data4 = np.arange(0,len(y_data4),1)[:, np.newaxis]

y_data5 = result['0.5 Recall'][:70000].values
x_data5 = np.arange(0,len(y_data5),1)[:, np.newaxis]

y_data6 = result['0.7 Recall'][:70000].values
x_data6 = np.arange(0,len(y_data6),1)[:, np.newaxis]

curve_fit(x_data1,y_data1,'fit_Region Avg IOU')
curve_fit(x_data2,y_data2,'fit_Class')
curve_fit(x_data3,y_data3,'fit_Obj')
curve_fit(x_data4,y_data4,'fit_No Obj')
curve_fit(x_data5,y_data5,'fit_0.5_Recall')
curve_fit(x_data6,y_data6,'fit_0.7_Recall')