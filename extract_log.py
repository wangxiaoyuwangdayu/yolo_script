import inspect
import os
import random
import sys

def extract_log(log_file,new_log_file,key_word):
    with open(log_file, 'r') as f:
        with open(new_log_file, 'w') as train_log:
            for line in f:
                # 去除多gpu的同步log
                if 'Syncing' in line:
                    continue
                # 去除除零错误的log
                if 'nan' in line:
                    continue
                if key_word in line:
                    train_log.write(line)

extract_log('E:/log_ceshi/keras_kmeans_log/log.txt','E:/log_ceshi/keras_kmeans_log/train_log_loss.txt','images')
extract_log('E:/log_ceshi/keras_kmeans_log/log.txt','E:/log_ceshi/keras_kmeans_log/train_log_iou.txt','IOU')