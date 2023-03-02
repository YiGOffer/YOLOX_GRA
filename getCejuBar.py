# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import time
real_path = "E:\Graduate\Code\YOLOX_GRA\img\测距误差对比图/"
file_name = ""
num = 2

# 指定默认字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'
# 解决负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False
if num == 1:
    file_name =" 两实验纵向距离平均误差" + str(time.time())
    num_list = [8.261, 4.909]
    plt.title("纵向距离平均误差对比")#图标名字

elif num == 2:
    file_name =" 两实验横向距离平均误差" + str(time.time())
    num_list = [7.688, 5.487]
    plt.title("横向距离平均误差对比")#图标名字

elif num == 3:
    file_name =" 两实验垂直距离平均误差" + str(time.time())
    num_list = [9.728, 7.187]
    plt.title("垂直距离平均误差对比")#图标名字

    
save_path = real_path + file_name + ".png"
name_list = ["实验1","实验2"]


plt.bar(range(len(num_list)), num_list,color='#0080FF',tick_label=name_list)
plt.savefig(save_path)
plt.show()