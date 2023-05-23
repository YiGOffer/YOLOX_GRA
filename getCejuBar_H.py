# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import time
real_path = "E:\Graduate\Code\YOLOX_GRA\img\Map/"
file_name = ""
total_num = 0
tar = [['mish', 'relu',  'silu'], ['cbam', 'sam', 'eca','mish']]

# 指定默认字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 30
plt.rcParams['figure.figsize']=(8, 7)
# 解决负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False
for num in tar[total_num]:        # 第二个实例
#1
    if num == "mish":
        file_name = num + str(time.time())
        num_list = [0.9124, 0.8723, 0.907]
        sum = 0
        for i in num_list:
            sum += i
        avg = round (sum / len(num_list) * 100,2)
        title_str = "mAP =" + str(avg) + "%"
        plt.title(title_str )#图标名字
    elif num == "relu":
        file_name = num + str(time.time())
        num_list = [0.872, 0.833, 0.904]
        sum = 0
        for i in num_list:
            sum += i
        avg = round (sum / len(num_list) * 100,2)
        title_str = "mAP =" + str(avg) + "%"
        plt.title(title_str )#图标名字
    elif num == "silu":
        file_name = num + str(time.time())
        num_list = [0.913, 0.8323, 0.91443]
        sum = 0
        for i in num_list:
            sum += i
        avg = round (sum / len(num_list) * 100,2)
        title_str = "mAP =" + str(avg) + "%"
        plt.title(title_str )#图标名字

#2
    elif num == "cbam":
        file_name = num + str(time.time())
        num_list = [0.90253, 0.78234, 0.8925]#"人","牛","马"
        sum = 0
        for i in num_list:
            sum += i
        avg = round (sum / len(num_list) * 100,2)
        title_str = "mAP =" + str(avg) + "%"
        plt.title(title_str )#图标名字
    elif num == "sam":
        file_name = num + str(time.time())
        num_list = [0.9132, 0.8532, 0.9012]#"人","牛","马"
        sum = 0
        for i in num_list:
            sum += i
        avg = round (sum / len(num_list) * 100,2)
        title_str = "mAP =" + str(avg) + "%"
        plt.title(title_str )#图标名字
    elif num == "eca":
        file_name = num + str(time.time())
        num_list = [0.9122, 0.8565, 0.9432]#"人","牛","马"
        sum = 0
        for i in num_list:
            sum += i
        avg = round (sum / len(num_list) * 100,2)
        title_str = "mAP =" + str(avg) + "%"
        plt.title(title_str )#图标名字       
#3
    save_path = real_path + file_name + ".png"
    name_list = ["人","牛","马"]
    plt.xlim((0,1))
    # plt.ylim((0,1))
    plt.barh(range(len(num_list)), num_list,color='#0080FF',tick_label=name_list)
    for i in range(1, len(num_list)+1):
        plt.text(num_list[i-1], i-1, round (num_list[i-1],2),fontsize=20)
    plt.savefig(save_path)
    plt.show()