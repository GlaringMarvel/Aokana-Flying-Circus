import time
from python_imagesearch.imagesearch import imagesearcharea  # 引入识图函数
import re

# def cooData(x,y):
#     counter = 1   # 循环计数器
#     while counter <= 5:
#         Num = 0   # 获取图片个数
#         pos = imagesearcharea("image/HangarMenu/Setting.png", x, y, x+192, y+128, precision=0.5)
#         if pos[0] != -1:
#             Num += 1
#         else:
#             print("'Setting' image not found")
#
#         pos = imagesearcharea("image/HangarMenu/Battle.png", x+400, y, x+800, y+300, precision=0.5)
#         if pos[0] != -1:
#             Num += 1
#         else:
#             print("'Battle' image not found")
#
#         pos = imagesearcharea("image/HangarMenu/Help.png", x + 1000, y, x + 1500, y + 128, precision=0.5)
#         if pos[0] != -1:
#             Num += 1
#         else:
#             print("'Help' image not found")
#
#         if Num == 3:
#             return 1  # 返回值1，识别成功
#         else:
#             print("图像识别失败，请查看游戏界面是否被遮挡")
#             print("第" + str(counter)+"次识别失败")
#             counter += 1
#             time.sleep(3)
#     print("界面识别失败，请检查界面或等待")
#     return 0  # 返回值0，识别失败

def cooData(x,y):
    # counter = 1   # 循环计数器
    # while counter <= 5:
    #     Num = 0   # 获取图片个数
    #     pos = imagesearcharea("image/HangarMenu/Setting.png", x, y, x+192, y+128, precision=0.5)
    #     if pos[0] != -1:
    #         Num += 1
    #     else:
    #         print("'Setting' image not found")

    pos = imagesearcharea("image/HangarMenu/Battle.png", x+400, y, x+800, y+300, precision=0.5)
    if pos[0] != -1:
        return 1  # 返回值1，识别成功
    else:
        print("'Battle' image not found")
        print("图像识别失败，请查看游戏界面是否被遮挡")
        # print("第" + str(counter) + "次识别失败")
        # counter += 1
        time.sleep(3)
        # pos = imagesearcharea("image/HangarMenu/Help.png", x + 1000, y, x + 1500, y + 128, precision=0.5)
        # if pos[0] != -1:
        #     Num += 1
        # else:
        #     print("'Help' image not found")
        #
        # if Num == 3:
        #     return 1  # 返回值1，识别成功
        # else:

    # print("界面识别失败，请检查界面或等待")
    return 0  # 返回值0，识别失败

def IAS():

    # 读取文件
    file = open('data.txt', 'r')
    content = file.read()
    file.close()

    # 使用正则表达式提取数值
    pattern = r'speed=(\d+)'
    match = re.search(pattern, content)
    if match:
        value = match.group(1)
        speed = int(value)
        print(f"空速设置为超过{speed}")
        return speed
    else:
        speed = 900
        print("空速重置为默认值")
        return speed

def vtime():

    # 读取文件
    file = open('data.txt', 'r')
    content = file.read()
    file.close()

    # 使用正则表达式提取数值
    pattern = r'time=(\d+)'
    match = re.search(pattern, content)
    if match:
        value = match.group(1)
        t = int(value)
        print(f"自动抛洒热诱时间为开始{t}秒后")
        return t
    else:
        t = 180
        print("自动抛洒热诱时间重置为默认值")
        return t

# 我懒得写重复调用函数了，等参数多了再说
def upH():

    # 读取文件
    file = open('data.txt', 'r')
    content = file.read()
    file.close()

    # 使用正则表达式提取数值
    pattern = r'up=(\d+)'
    match = re.search(pattern, content)
    if match:
        value = match.group(1)
        up = int(value)
        print(f"扔完炸弹后自动爬升{up}m")
        return up
    else:
        up = 3000
        print("自动爬升重置为默认值")
        return up