import numpy as np
import time
import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt

tar = "Mish"
file_name =tar + str(time.time())

real_path = "E:\Graduate\Code\YOLOX_GRA\img\激活函数/"
save_path = real_path + file_name + ".jpg"

x = np.arange(-5, 5, 0.1)
tensor = torch.from_numpy(x)
y = []
y1 = []
y2 = []

for t in tensor:
    if tar == "Silu" :
        y_1 = t * torch.sigmoid(t)# silu
        y.append(y_1)

        y_2 = t * torch.sigmoid(0.1* t)# silu
        y1.append(y_2)

        y_3 = t * torch.sigmoid(10* t)# silu
        y2.append(y_3)

    else:
        y_1 = t * torch.tanh(F.softplus(t))# mish
        y.append(y_1)

if tar == "Silu" :
    plt.plot(x, y, label=tar+" β=1")
    plt.plot(x, y1, label=tar+" β=0.1")
    plt.plot(x, y2, label=tar+" β=10")
    plt.ylim(-3, 5)

else:
    plt.plot(x, y, label=tar,color='orangered')
    plt.ylim(-1, 5)
    
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig(save_path)
plt.show()
