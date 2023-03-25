import cv2
import numpy as np

# 读取标定图像
image_files = ["E:\Graduate\Code\YOLOX_GRA\标定2.png", "E:\Graduate\Code\YOLOX_GRA\标定1.png"]
images = [cv2.imread(file) for file in image_files]
print(images)
# 定义标定板的尺寸和格子数
board_size = (9, 6)
square_size = 1.0

# 提取标定板角点
obj_points = []
img_points = []
for img in images:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, board_size, None)
    if ret:
        objp = np.zeros((board_size[0] * board_size[1], 3), np.float32)
        objp[:,:2] = np.mgrid[0:board_size[0], 0:board_size[1]].T.reshape(-1, 2)
        objp *= square_size
        obj_points.append(objp)
        img_points.append(corners)

# 进行相机标定
ret, K, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, gray.shape[::-1], None, None)

# 输出相机内参
print('相机内参：')
print('fx =', K[0, 0])
print('fy =', K[1, 1])
print('Uc =', K[0, 2])
print('Vc =', K[1, 2])
