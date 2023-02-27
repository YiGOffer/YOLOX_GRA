import json
import matplotlib.pyplot as plt
import random
import matplotlib
import time
import os
import sys

file_name =" 纵向距离误差对比_" + str(time.time())

real_path = "E:\Graduate\Code\YOLOX_GRA\img\测距误差对比图/"
save_path = real_path + file_name + ".jpg"

# 指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family'] = 'sans-serif'
# 解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False
xData = [10, 20, 30, 40, 50, 60]

# 纵向距离误差
oriYoloZData = [7.256, 8.278, 9.059, 3.798, 9.591, 11.589]


plt.plot(xData, oriYoloZData, label = "实验1")  # 第一个参数为横坐标 第二个为纵坐标 第三个为曲线名字

# plt.plot(x, x ** 2, label="line2")
# plt.plot(x,x**3,label="line3")
plt.ylabel("平均误差（%）")  # x轴名字
plt.xlabel("实际距离（m）")#y轴名字
plt.title("纵向距离误差对比")#图标名字
plt.legend()#显示图例
plt.savefig(save_path)
plt.show()#生成图表

# import random

# for i in range (1,24) :
#     print("n",random.uniform(2.00,1.81))
