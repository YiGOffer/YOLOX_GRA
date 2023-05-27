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
font_size = 30
# plt.rcParams['font.size'] = 30
plt.rcParams['figure.figsize']=(8, 8.5)
# 解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False
xData = [10, 20, 30, 40, 50, 60]

# 纵向距离误差
oriYoloZData = [7.26,8.28,9.06,3.80,9.59,11.59]
oriYoloHData = [7.85,6.25,11.05,2.75,7.85,10.60]
# oriYoloCData = [13.483, 9.855, 7.522, 4.046, 9.245, 14.218]
gYoloZ = [2.88,3.62,6.13,5.80,5.59,5.43]
gYoloH = [4.35,3.35,6.25,5.30,6.35,7.30]
# gYoloC = [2.426,6.850,5.033,6.057,7.641,15.117]
# num = input("请输入想生成的图像：")

num = 1 
file_name = ""
if num == 1:
    # 纵向曲线对比
    plt.plot(xData, oriYoloZData, label = "实验1",marker='.')  # 第一个参数为横坐标 第二个为纵坐标 第三个为曲线名字
    plt.plot(xData, gYoloZ, label = "实验2",marker='.')  # 第一个参数为横坐标 第二个为纵坐标 第三个为曲线名字
    plt.title("纵向距离误差对比",size = font_size)#图标名字
    file_name =" 纵向距离误差对比_" + str(time.time())
elif num == 2:
    # 横向
    plt.plot(xData, oriYoloHData, label = "实验1", marker='.')  # 第一个参数为横坐标 第二个为纵坐标 第三个为曲线名字
    plt.plot(xData, gYoloH, label = "实验2", marker='.')  # 第一个参数为横坐标 第二个为纵坐标 第三个为曲线名字
    plt.title("横向距离误差对比",size = font_size)#图标名字
    file_name =" 横向距离误差对比_" + str(time.time())
# elif num == 3:
#     # 垂直曲线对比
#     plt.plot(xData, oriYoloCData, label = "实验1", marker='.')  # 第一个参数为横坐标 第二个为纵坐标 第三个为曲线名字
#     plt.plot(xData, gYoloC, label = "实验2",marker='.')  # 第一个参数为横坐标 第二个为纵坐标 第三个为曲线名字
#     plt.title("垂直距离误差对比")#图标名字
#     file_name =" 垂直距离误差对比_" + str(time.time())



        
real_path = "E:\Graduate\Code\YOLOX_GRA\img\cejubar/"
save_path = real_path + file_name + ".jpg"
# plt.plot(x, x ** 2, label="line2")
# plt.plot(x,x**3,label="line3")

plt.ylabel("平均误差（%）",size = font_size)  # x轴名字
plt.xlabel("实际距离（m）",size = font_size)#y轴名字
plt.yticks(fontproperties = 'Times New Roman',size = font_size)
plt.xticks(fontproperties = 'Times New Roman',size = font_size)

plt.legend(fontsize = font_size - 5)#显示图例
plt.savefig(save_path)
plt.show()#生成图表

# import random

# for i in range (1,24) :
#     print("n",random.uniform(2.00,1.81))
