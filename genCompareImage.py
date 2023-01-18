import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time

file_name = str(time.time())
file_path = "./flowImageOutput/"
save_path = file_path  + file_name + ".jpg"
# 指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family'] = 'sans-serif'
# 解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False

# 读取文件 
with open()

plt.plot(x, x, label="line1")  # 第一个参数为横坐标 第二个为纵坐标 第三个为曲线名字
plt.plot(x, x ** 2, label="line2")
plt.plot(x,x**3,label="line3")
plt.xlabel("x label")  # x轴名字
plt.ylabel("ylabel")#y轴名字
plt.title("折线图")#图标名字
plt.legend()#显示图例
plt.savefig(save_path)
plt.show()#生成图表

# import random

# for i in range (1,24) :
#     print("n",random.uniform(2.00,1.81))