import json
import matplotlib.pyplot as plt
import matplotlib
import time
import os
file_name = str(time.time())
file_path = "./dataOutput/"
if not os.path.exists(file_path):  #判断是否存在文件夹如果不存在则创建为文件夹
    os.makedirs(file_path)
save_path = file_path  + "combine/" + file_name + ".jpg"
# 指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family'] = 'sans-serif'
# 解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False
file_list = []
file_list[0] = "dataOutput\istockphoto-1305469222-640_adpp_is.mp4.json" 
file_list[1] = "dataOutput\istockphoto-1305469222-640_adpp_is.mp4.json" 
file_list[2] = "dataOutput\istockphoto-1305469222-640_adpp_is.mp4.json" 


# 读取json文件 
i = 0
data = ""
while i < len(file_list) :
    with open(file_list[i],'r') as f :
        data[i] = f.read()
        data[i] = json.load(data[i])
        plt.plot(data[i][0], data[i][1], label = os.path.split(file_list[i])[1])  # 第一个参数为横坐标 第二个为纵坐标 第三个为曲线名字


# plt.plot(x, x ** 2, label="line2")
# plt.plot(x,x**3,label="line3")
plt.xlabel("x label")  # x轴名字
plt.ylabel("ylabel")#y轴名字
plt.title("不同分辨率比对图")#图标名字
plt.legend()#显示图例
plt.savefig(save_path)
plt.show()#生成图表

# import random

# for i in range (1,24) :
#     print("n",random.uniform(2.00,1.81))
