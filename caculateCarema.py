import cv2
import numpy as np
import glob

# 读取标定图像
# image_files = ["E:\Graduate\Code\YOLOX_GRA\img\\biaoding\\ori_biaoding\\2a.jpg", "E:\Graduate\Code\YOLOX_GRA\img\\biaoding\\1a.jpg"]
images = glob.glob('E:\Graduate\Code\YOLOX_GRA\img\\biaoding\\res1\\*.jpg')
# images = [cv2.imread(file) for file in image_files]
# print(images)
# 定义标定板的尺寸和格子数
board_size = (9, 6)
square_size = 1.0

# 提取标定板角点
obj_points = []
img_points = []
index=0
for img in images:
    index = index + 1
    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, board_size, None)
    if ret:
        objp = np.zeros((board_size[0] * board_size[1], 3), np.float32)
        objp[:,:2] = np.mgrid[0:board_size[0], 0:board_size[1]].T.reshape(-1, 2)
        objp *= square_size
        obj_points.append(objp)
        img_points.append(corners)
                # 将角点在图像上显示
        cv2.drawChessboardCorners(img, (9,6), corners, ret)
        cv2.imshow('findCorners',img)
        # cv2.imwrite('E:\Graduate\Code\YOLOX_GRA\img\\biaoding\\res\\findCorners' + str(index)+".png",img)
        cv2.waitKey(1)
cv2.destroyAllWindows()

# 进行相机标定
ret, K, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, gray.shape[::-1], None, None)

# 输出相机内参
print('相机内参：')
print('fx =', K[0, 0])
print('fy =', K[1, 1])
print('Uc =', K[0, 2])
print('Vc =', K[1, 2])
