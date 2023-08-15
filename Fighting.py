from python_imagesearch.imagesearch import imagesearcharea  # 引入识图函数
import pygetwindow
import cv2
import numpy as np
import pyautogui

def getWin():
    x = 0
    y = 0
    window = pygetwindow.getWindowsWithTitle('War Thunder')[0]  # 寻找游戏窗口
    x = window.left  # 窗口的左边界坐标
    y = window.top  # 窗口的顶部边界坐标

    window_width, window_height = window.size

    center_x = window.left + (window_width // 2)

    return x, y, center_x

def imgSearch(imgData, sx, sy, ex, ey):
    pos = imagesearcharea(imgData, sx, sy, ex, ey)
    if pos[0] != -1:
        bollen = 1
        return bollen
    else:
        bollen = 0
        return bollen

def back(x,y):
    sx = x + 600
    sy = y + 500
    ex = x + 1200
    ey = y + 800
    imgData = "image/Fight/Back.png"
    bollen = imgSearch(imgData, sx, sy, ex, ey)
    if bollen == 1:
        print("返回基地\n")
        return bollen
    else:
        bollen = 0
        return bollen

#CCRP3
def ccrpFind(x, y):
    # 定义要查找的图像路径
    image_path = "image/Fight/CCRP3.png"

    # 加载目标图像
    target_image = cv2.imread(image_path)

    # 转换颜色空间为HSV
    target_hsv = cv2.cvtColor(target_image, cv2.COLOR_BGR2HSV)

    # 计算目标图像的双通道直方图
    target_hist = cv2.calcHist([target_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

    # 获取屏幕截图
    screenshot = pyautogui.screenshot()

    # 将屏幕截图转换为OpenCV图像
    screenshot_image = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # 在指定范围内查找图像
    for dx in range(x, x + 1280):
        for dy in range(y + 200, y + 500):
            # 截取屏幕截图中的区域
            region = screenshot_image[dy:dy+target_image.shape[0], dx:dx+target_image.shape[1]]

            # 转换颜色空间为HSV
            region_hsv = cv2.cvtColor(region, cv2.COLOR_BGR2HSV)

            # 计算区域图像的双通道直方图
            region_hist = cv2.calcHist([region_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

            # 计算直方图的差异
            diff = cv2.compareHist(target_hist, region_hist, cv2.HISTCMP_CORREL)

            # 设置阈值，判断是否匹配成功
            threshold = 0.8
            if diff > threshold:
                print("找到图像，坐标：({}, {})".format(dx, dy))
                dx = dx + 4
                return dx

    # 未找到图像
    return None


# def ccrpSearch(imgData, sx, sy, ex, ey, pre):
#     pos = imagesearcharea(imgData, sx, sy, ex, ey, precision=pre)
#     if pos[0] != -1:
#         return pos
#     else:
#         return None

# # CCPR红线位置寻找
# def ccrp1(x, y):
#     sx = x
#     sy = y + 200
#     ex = x + 1280
#     ey = y + 600
#     pre = 0.8
#     imgData = "image/Fight/CCRP1.png"
#     result = ccrpSearch(imgData, sx, sy, ex, ey, pre)
#     if result is not None:
#         ix, iy = result
#         ix = ix + x
#         print("CCRP坐标已发现，位置：", ix, iy)
#         return ix
#     else:
#         return None

# 准星位置寻找
# def ccrp2(x, y):
#     sx = x + 400
#     sy = y + 200
#     ex = x + 1000
#     ey = y + 600
#     pre = 0.5
#     imgData = "image/Fight/CCRP2.png"
#     result = ccrpSearch(imgData, sx, sy, ex, ey, pre)
#     if result is not None:
#         ix, iy = result
#         ix = ix + 422 + x
#         print("准星坐标已发现，位置：", ix, iy)
#         return ix
#     else:
#         return None

# 准星位置寻找
# def ccrp4(x, y):
#     sx = x + 400
#     sy = y + 200
#     ex = x + 1000
#     ey = y + 600
#     pre = 0.2
#     imgData = "image/Fight/CCRP4.png"
#     result = ccrpSearch(imgData, sx, sy, ex, ey, pre)
#     if result is not None:
#         ix, iy = result
#         ix = ix + 422 + x
#         print("准星坐标已发现，位置：", ix, iy)
#         return ix
#     else:
#         return None

# CCPR红线位置寻找
# def ccrp1(x, y):
#     sx = x
#     sy = y + 200
#     ex = x + 1280
#     ey = y + 600
#     pre = 0.7
#     imgData = "image/Fight/CCRP3.png"
#     result = ccrpSearch(imgData, sx, sy, ex, ey, pre)
#     if result is not None:
#         ix, iy = result
#         ix = ix + x + 4
#         print("CCRP坐标已发现，位置：", ix, iy)
#         return ix
#     else:
#         return None
#
# # CCPR红线位置寻找
# def ccrp5(x, y):
#     sx = x
#     sy = y + 200
#     ex = x + 1280
#     ey = y + 600
#     pre = 0.1
#     imgData = "image/Fight/CCRP5.png"
#     result = ccrpSearch(imgData, sx, sy, ex, ey, pre)
#     if result is not None:
#         ix, iy = result
#         ix = ix + x + 4
#         print("CCRP坐标已发现，位置：", ix, iy)
#         return ix
#     else:
#         return None