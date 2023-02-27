import json
import matplotlib.pyplot as plt
import random
import matplotlib
import time
import os
import sys


# 指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family'] = 'sans-serif'
# 解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False
xData = [10, 20, 30, 40, 50, 60]

# 纵向距离误差
oriYoloZData = [7.256, 8.278, 9.059, 3.798, 9.591, 11.589]
oriYoloHData = [7.505, 6.307, 11.030, 2.729, 7.985, 10.604]
oriYoloCData = [13.483, 9.855, 7.522, 4.046, 9.245, 14.218]
gYoloZ = [2.876,3.621,6.132,5.798,5.591,5.433]
gYoloH = [4.416,3.330,6.236,5.319,6.334,7.317]
gYoloC = [2.426,6.850,5.033,6.057,7.641,15.117]
num = input("请输入想生成的图像：")
if num == 1:
    # 纵向曲线对比
    plt.plot(xData, oriYoloZData, label = "实验1")  # 第一个参数为横坐标 第二个为纵坐标 第三个为曲线名字
    plt.plot(xData, gYoloZ, label = "实验2")  # 第一个参数为横坐标 第二个为纵坐标 第三个为曲线名字
    plt.title("纵向距离误差对比")#图标名字
    file_name =" 纵向距离误差对比_" + str(time.time())
elif num == 2:
    # 横向
    plt.plot(xData, oriYoloHData, label = "实验1")  # 第一个参数为横坐标 第二个为纵坐标 第三个为曲线名字
    plt.plot(xData, gYoloH, label = "实验2")  # 第一个参数为横坐标 第二个为纵坐标 第三个为曲线名字
    plt.title("横向距离误差对比")#图标名字
    file_name =" 横向距离误差对比_" + str(time.time())
elif num == 3:
    # 垂直曲线对比
    plt.plot(xData, oriYoloCData, label = "实验1")  # 第一个参数为横坐标 第二个为纵坐标 第三个为曲线名字
    plt.plot(xData, gYoloC, label = "实验2")  # 第一个参数为横坐标 第二个为纵坐标 第三个为曲线名字
    plt.title("垂直距离误差对比")#图标名字
    file_name =" 垂直距离误差对比_" + str(time.time())





real_path = "E:\Graduate\Code\YOLOX_GRA\img\测距误差对比图/"
save_path = real_path + file_name + ".jpg"
# plt.plot(x, x ** 2, label="line2")
# plt.plot(x,x**3,label="line3")
plt.ylabel("平均误差（%）")  # x轴名字
plt.xlabel("实际距离（m）")#y轴名字
plt.legend()#显示图例
plt.savefig(save_path)
plt.show()#生成图表

# import random

# for i in range (1,24) :
#     print("n",random.uniform(2.00,1.81))
