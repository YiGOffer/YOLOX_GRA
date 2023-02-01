import json
import matplotlib.pyplot as plt
import matplotlib
import time
import os
import sys

data = []
min_len = sys.maxsize
file_list = []
file_name = str(time.time())
file_path = "./dataOutput/"
if not os.path.exists(file_path):  #判断是否存在文件夹如果不存在则创建为文件夹
    os.makedirs(file_path)
res_path = file_path + "combine/"
if not os.path.exists(res_path):  #判断是否存在文件夹如果不存在则创建为文件夹
    os.makedirs(res_path)
save_path = res_path + file_name + ".jpg"

# 指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family'] = 'sans-serif'
# 解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False

file_list.append("dataOutput\\animal1080p.mp4.json" ) 
file_list.append("dataOutput\\animal720p.mp4.json" ) 
file_list.append("dataOutput\\animal480p.mp4.json" ) 

# 读取json文件 

for i in range(len(file_list)):
    with open(file_list[i],'r') as f :
        data.append(json.loads(f.read()))
        if len(data[i][0]) < min_len :
            min_len = len(data[i][0])
print(min_len)

for i in range(len(data)):
    for j in range(2):
        if len(data[i][j]) >= min_len :
            data[i][j] = data[i][j][:min_len - 1]
    file_ext_name = os.path.split(file_list[i])[1]
    label_name = file_ext_name.split('.')[0]
    plt.plot(data[0][0], data[i][1], label = label_name)  # 第一个参数为横坐标 第二个为纵坐标 第三个为曲线名字

# plt.plot(x, x ** 2, label="line2")
# plt.plot(x,x**3,label="line3")
plt.ylabel("FPS")  # x轴名字
plt.xlabel("时间（单位：min）")#y轴名字
plt.title("不同分辨率下FPS变化图")#图标名字
plt.legend()#显示图例
plt.savefig(save_path)
plt.show()#生成图表

# import random

# for i in range (1,24) :
#     print("n",random.uniform(2.00,1.81))
