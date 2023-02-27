# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import time
real_path = "E:\Graduate\Code\YOLOX_GRA\img\测距误差对比图/"
file_name = ""
num = 1

if num == 1:
    file_name =" 两实验纵向距离平均误差" + str(time.time())
    num_list = [8.261, 4.909]
elif num == 2:
    file_name =" 两实验横向距离平均误差" + str(time.time())
    num_list = [7.688, 5.487]
elif num == 3:
    file_name =" 两实验垂直距离平均误差" + str(time.time())
    num_list = [9.728, 7.187]
    
save_path = real_path + file_name
name_list = ['实验1','实验2']

plt.bar(range(len(num_list)), num_list,color='rgb',tick_label=name_list)
plt.show()