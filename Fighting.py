from python_imagesearch.imagesearch import imagesearcharea  # 引入识图函数
import pygetwindow
import OpenFile
import port8111
import math
import numpy as np

# 读取文件设置
_, decelerate_distance, _, fox_two_distance, bombing_distance, _ = OpenFile.read_values()
print(f"减速距离设置为：{decelerate_distance}")
print(f"热诱抛洒距离设置为：{fox_two_distance}")
print(f"战区剩余距离判断设置为：{bombing_distance}")


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


def back(x, y):
    sx = x + 600
    sy = y + 500
    ex = x + 1200
    ey = y + 800
    imgData = "image/Fight/Back.png"
    bollen = imgSearch(imgData, sx, sy, ex, ey)
    if bollen == 1:
        return bollen
    else:
        bollen = 0
        return bollen


# 玩家是否处于机场
def compare_coordinates():
    # 初始化 coordinates 列表
    coordinates = [None, None, None]  # 初始化 coordinates 列表
    # 获取坐标值并解包赋值给 coordinates 列表
    coordinates[0], coordinates[1], coordinates[2] = port8111.get_coordinates()
    airfield_coordinates = coordinates[0]
    player_coordinates = coordinates[2]

    if player_coordinates == (-1, -1):
        return -1
    # 将坐标的小数点后两位保留，并转换为字符串进行比较
    airfield_str = "{:.2f}".format(airfield_coordinates[0]) + "{:.2f}".format(airfield_coordinates[1])
    player_str = "{:.2f}".format(player_coordinates[0]) + "{:.2f}".format(player_coordinates[1])

    # 比较坐标字符串是否相等
    if airfield_str == player_str:
        return 1
    else:
        return 0


# 飞行时飞控
def flight_controller(h1, h2, v1, v2, v3, Vy, Hm, throttle, IAS):
    if throttle == 0 and IAS < 100:  # 判断是否死亡
        print(f"节流阀：{throttle} 空速：{IAS} 可能死亡")
        flag = 0
        return flag
    elif IAS < 250:  # 判断是否具有起飞速度
        print(f"空速：{IAS} 空速过低")
        flag = 1
        return flag
    elif Hm < h1:  # 判断水平高度
        if Vy < v1:  # 判断爬升率
            flag = 88  # 需要大角度爬升
            return flag
        elif v2 > Vy > v1:
            flag = 8  # 需要小角度爬升
            return flag
        elif Vy > v3:
            flag = 2  # 小角度下压
            return flag
    elif h1 < Hm < h2:  # 稳定飞行区间
        if Vy < -3:
            flag = 8  # 需要小角度爬升
            return flag
        elif Vy > 10:
            flag = 22  # 需要大角度下压
            return flag
        elif 10 > Vy > 5:
            flag = 2  # 小角度下压
            return flag
        # elif IAS > velocity_cruising:
        #     flag = 5  # 超过目标最低速度
        #     return flag
        else:  # 意外情况
            flag = -1
            return flag
    elif Hm > h2 and Vy > 0:  # 开始下降
        flag = 22
        return flag


# 航向角度计算
def angle_between_vectors(dx, dy):
    # 将向量(dx, dy)和向量(0, 1)转换为numpy数组
    vector1 = np.array([dx, dy])
    vector2 = np.array([0, 1])
    # 计算向量的模长
    magnitude1 = np.linalg.norm(vector1)
    magnitude2 = np.linalg.norm(vector2)
    # 计算向量的点积
    dot_product = np.dot(vector1, vector2)
    # 计算夹角的余弦值
    cosine_angle = dot_product / (magnitude1 * magnitude2)
    # 通过反余弦函数计算夹角（以弧度为单位）
    angle_rad = np.arccos(cosine_angle)
    # 将弧度转换为角度
    angle_deg = np.degrees(angle_rad)
    return angle_deg


# 航向计算
def calculate_heading(player_coordinates, bombing_coordinates):
    px, py = player_coordinates
    # print(f"玩家坐标{px},{py}")
    bx, by = bombing_coordinates
    # print(f"战区坐标{bx},{by}")
    dx = bx - px
    dy = by - py

    # 坐标距离计算
    distance = math.sqrt(dx ** 2 + dy ** 2)

    # 夹角计算
    angle_degrees = angle_between_vectors(dx, -dy)
    if dx < 0:
        angle_degrees = 360 - angle_degrees
    if angle_degrees is None:
        angle_degrees = 0
    if distance is None:
        distance = 0
    return angle_degrees, distance


# 航向控制
def heading_control(IAS, map_size, time_flag, num, fox_flag):
    if IAS < 500:
        flag = 0  # 不适合调整航向
        return flag
    elif time_flag == 2:
        flag = 0  # 结束投弹
        return flag
    # 获得全部战区坐标和玩家坐标
    player_coordinates, bombing_coordinates = port8111.get_bombing_point_coordinates()
    # 获得第n个战区坐标
    # n = num - 1
    # bombing_coordinates = bombing_collection[n]
    # 计算目标航向和地图距离
    heading, map_distance = calculate_heading(player_coordinates, bombing_coordinates)
    # 获得飞机航向
    compass = port8111.get_compass()
    # 计算航向修正
    delta = heading - compass
    # 计算实际距离
    distance = (map_distance / 1000) * map_size

    # 判断正负性并打印修正值
    if delta < 0:
        delta += 360
    if delta > 180:
        delta = delta - 360

    distance = round(distance, 2)
    delta = round(delta, 3)
    heading = round(heading, 3)
    compass = round(compass, 3)
    print(f"战区坐标{bombing_coordinates},玩家坐标{player_coordinates},距离{distance}Km")
    print(f"目标航向{heading},飞机航向{compass},航向修正{delta}")

    if distance < bombing_distance and time_flag == 0:
        flag = 5    # 准备弹起投弹键
        return flag
    if distance < fox_two_distance and fox_flag == 0:
        flag = 7    # 准备抛洒热诱
        return flag
    if decelerate_distance != 0 and distance < decelerate_distance:
        flag = 1    # 减速板打开
        return flag
    # 看小键盘，4左转，6右转
    if -10 > delta >= -180:
        flag = 444
        return flag
    elif 10 < delta < 180:
        flag = 666
        return flag
    elif -3 > delta > -7:
        flag = 44
        return flag
    elif 3 < delta < 7:
        flag = 66
        return flag
    elif -0.3 > delta > -3:
        flag = 4
        return flag
    elif 0.3 < delta < 3:
        flag = 6
        return flag


# 飞向对方机场
def enemy_airfield(map_size, airbrake):
    # 获得机场坐标和玩家坐标
    _, enemy_airport, player_coordinates = port8111.get_coordinates()
    # 计算目标航向和地图距离
    heading, map_distance = calculate_heading(player_coordinates, enemy_airport)
    # 获得飞机航向
    compass = port8111.get_compass()
    # 计算航向修正
    delta = heading - compass
    # 计算实际距离
    distance = (map_distance / 1000) * map_size

    if delta < 0:
        delta += 360

        # 判断正负性并打印修正值
    if delta > 180:
        delta = delta - 360

    distance = round(distance, 2)
    delta = round(delta, 3)
    heading = round(heading, 3)
    compass = round(compass, 3)
    print(f"敌方机场坐标{enemy_airport},玩家坐标{player_coordinates},距离{distance}Km")
    print(f"目标航向{heading},飞机航向{compass},航向修正{delta}")
    if distance < 15 and airbrake == 0:
        flag = 1  # 开启减速板
        return flag
    # 看小键盘，4左转，6右转
    if -10 > delta >= -180:
        flag = 444
        return flag
    elif 10 < delta < 180:
        flag = 666
        return flag
    elif -3 > delta > -7:
        flag = 44
        return flag
    elif 3 < delta < 7:
        flag = 66
        return flag
    elif -0.3 > delta > -3:
        flag = 4
        return flag
    elif 0.3 < delta < 3:
        flag = 6
        return flag
