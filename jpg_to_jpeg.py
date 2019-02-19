import inspect
import os
import random
import sys

old_filepath = "E:/qinxiedaoduan/ceshi2/train.txt"
new_filepath = "E:/qinxiedaoduan/ceshi2/new_train.txt"
old_str = "jpg"
new_str = "jpeg"
k = 0
with open(old_filepath,"r") as f:
    with open(new_filepath,"w") as n:
        for line in f:
            if (k>=1824 and k<3310):
                line = line.replace(old_str,new_str)
            line = line.strip('\r')
            n.write(line)
            k=k+1
