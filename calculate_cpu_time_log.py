import os
import os.path

filename_back=['_bu.log','_cbs_neu.log','_cbs_ion.log','_ept.log','_opt.log','_pop.log']
filepath0 = 'H:/ion_cs/'
filename0 = os.listdir(filepath0)
for name0 in filename0:
    filepath1 = os.path.join(filepath0,name0)#H:\ion_cs\Cx
    filename1 = os.listdir(filepath1)
    for name1 in filename1:
        filepath2 = os.path.join(filepath1,name1)#H:\ion_cs\Cx\C
        a=[]
        day=[];hour=[];minute=[];second=[]
        for i in filename_back:
            filename_all = name1.lower()+i
            with open(os.path.join(filepath2,filename_all),'r') as f:
                for line in f:
                    if 'Job cpu time' in line:
                        a.append(line.strip().split( ))
                        day.append(float(line.strip().split( )[3]))
                        hour.append(float(line.strip().split( )[5]))
                        minute.append(float(line.strip().split( )[7]))
                        second.append(float(line.strip().split( )[9]))
        days=sum(day)
        hours=sum(hour)
        minutes=sum(minute)
        seconds=sum(second)
        print('cpu_time_of:',name1)
        print('days:',days,'hours:',hours,'min:',minutes,'sec:',seconds)
        print(a)

'''
a=[]
day=[];hour=[];minute=[];second=[]
filename = 'F:/c_cbs_ion.log'
with open(filename,'r') as f:
    for line in f:
        if 'Job cpu time' in line:
            a.append(line.strip().split( ))
            day.append(float(line.strip().split( )[3]))
            hour.append(float(line.strip().split( )[5]))
            minute.append(float(line.strip().split( )[7]))
            second.append(float(line.strip().split( )[9]))
days=sum(day)
hours=sum(hour)
minutes=sum(minute)
seconds=sum(second)
print(days,hours,minutes,seconds)
print(a)
'''