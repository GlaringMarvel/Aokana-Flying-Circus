from python_imagesearch.imagesearch import imagesearcharea  # 引入识图函数
import pygetwindow
import OpenFile
import port8111
import math
import numpy as np
import datetime
# from simple_pid import PID

# 读取文件设置
_, decelerate_distance, _, fox_two_distance, bombing_distance, _, _, _, _, _, _ = OpenFile.read_values()
print(f"减速距离设置为： {decelerate_distance} Km")
print(f"热诱抛洒距离设置为： {fox_two_distance} Km")
print(f"战区剩余距离判断设置为： {bombing_distance} Km")


# 获取当前时间
def get_current_time():
    current_time = datetime.datetime.now()
    return current_time


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


# 距离和航向角计算
def distance_delta(player_coordinates, bombing_coordinates, map_size):
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
    return distance, delta


# 航向操作判断
def delta_control(delta):
    # 看小键盘，4左转，6右转
    if -15 > delta >= -180:
        flag = 4444
        return flag
    elif 15 < delta < 180:
        flag = 6666
        return flag
    elif -7 > delta > -15:
        flag = 444
        return flag
    elif 7 < delta < 15:
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


# 航向控制
def heading_control(IAS, map_size, time_flag, num, fox_flag):
    if IAS < 500:
        flag = 0  # 不适合调整航向
        return flag
    elif time_flag == 2:
        flag = 0  # 结束投弹
        return flag
    # 获得全部战区坐标和玩家坐标
    # player_coordinates, bombing_coordinates = port8111.get_bombing_point_coordinates()
    while -1 < num < 5:
        player_coordinates, bombing_coordinates = port8111.get_bombing_point_select(num - 1)
        if bombing_coordinates is None:
            num -= 1
        elif num == 0:
            print("不存在战区")
            break
        elif bombing_coordinates is not None:
            break

    # 获得距离和航向角
    distance, delta = distance_delta(player_coordinates, bombing_coordinates, map_size)

    if distance < bombing_distance and time_flag == 0:
        flag = 5  # 准备弹起投弹键
        return flag
    if distance < fox_two_distance and fox_flag == 0:
        flag = 7  # 准备抛洒热诱
        return flag
    if decelerate_distance > 0 and distance < decelerate_distance:
        flag = 1  # 减速板打开
        return flag
    else:
        # 航向操作判断
        flag = delta_control(delta)
        return flag


# 延迟入场
def delay_control(IAS, delay_start_time, time, north_direction, south_direction):
    flag = 0
    ccrp_flag = -1
    if IAS < 500:  # 不适合调整航向
        return ccrp_flag, flag

    # 获得机场坐标和玩家坐标
    friendly_airport, _, player_coordinates = port8111.get_coordinates()
    # 计算位于哪里出生
    airfield_x, airfield_y = friendly_airport
    if airfield_y < 0.5:
        heading = north_direction
    else:
        heading = south_direction

    # 获得飞机航向
    compass = port8111.get_compass()
    # 计算航向修正
    delta = heading - compass

    # 航向操作判断
    flag = delta_control(delta)
    delta = round(delta, 3)
    heading = round(heading, 3)
    compass = round(compass, 3)
    print(f"玩家坐标：{player_coordinates}，飞机航向：{compass}，目标航向：{heading}，航向修正：{delta}")

    # 计算时间差
    now_time = get_current_time()
    time_difference = now_time - delay_start_time
    seconds_passed = time_difference.total_seconds()
    seconds_passed = int(seconds_passed)
    print(f"已经过 {seconds_passed} s，总延迟时间 {time} s")
    if seconds_passed > time:
        ccrp_flag = 0

    return ccrp_flag, flag


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
    else:
        # 航向操作判断
        flag = delta_control(delta)
        return flag


# 逛街
# 航向控制
def go_shopping(map_size, time_flag, num):
    # 获得全部战区坐标和玩家坐标
    # player_coordinates, bombing_coordinates = port8111.get_bombing_point_coordinates()
    while -1 < num < 5:
        player_coordinates, bombing_coordinates = port8111.get_bombing_point_select(num)
        if bombing_coordinates is None:
            num -= 1
        elif num == -1:
            print("不存在战区")
            break
        elif bombing_coordinates is not None:
            break

    # 获得距离和航向角
    distance, delta = distance_delta(player_coordinates, bombing_coordinates, map_size)

    if distance < bombing_distance and time_flag == 0:
        flag = 5  # 准备弹起投弹键
        return flag
    else:
        # 航向操作判断
        flag = delta_control(delta)
        return flag


# 坐标计算
def calculate_point(x1, y1, angle, distance):
    # 将角度转换为弧度制
    angle_rad = math.radians(angle)

    # 计算坐标
    x2 = x1 + distance * math.cos(angle_rad)
    y2 = y1 + distance * math.sin(angle_rad)

    return x2, y2


# 返回检查点计算
def checkpoint(map_size):
    distance1 = 5000 / map_size     # 检查点1
    distance2 = 10000 / map_size    # 检查点2
    distance3 = 15000 / map_size    # 检查点3
    distance4 = 20000 / map_size    # 检查点4
    # 获得机场朝向
    airfield_compass = port8111.get_compass()
    # 获得机场坐标
    friendly_airport, _, _ = port8111.get_coordinates()
    a1, a2 = friendly_airport
    if airfield_compass > 180:
        airfield_compass = - airfield_compass
    dx1, dy1 = calculate_point(a1, a2, airfield_compass, distance1)
    checkpoint_1 = (dx1, dy1)
    dx2, dy2 = calculate_point(a1, a2, airfield_compass, distance2)
    checkpoint_2 = (dx2, dy2)
    dx3, dy3 = calculate_point(a1, a2, airfield_compass, distance3)
    checkpoint_3 = (dx3, dy3)
    dx4, dy4 = calculate_point(a1, a2, airfield_compass, distance4)
    checkpoint_4 = (dx4, dy4)
    return checkpoint_1, checkpoint_2, checkpoint_3, checkpoint_4


# PID控制测试
# def pid_control(h1, h2, Vy, Hm, throttle, IAS, ):
#     from simple_pid import PID
#
#     # 设置PID控制器的参数
#     Kp = 0.5  # 比例系数
#     Ki = 0.1  # 积分系数
#     Kd = 0.2  # 微分系数
#
#     # 设置目标飞行速度
#     target_speed = 1000  # 假设目标速度为300
#
#     # 初始化PID控制器
#     pid = PID(Kp, Ki, Kd, setpoint=target_speed)
#
#     # 设置节流阀控制范围
#     throttle_min = 0  # 最小节流阀值
#     throttle_max = 110  # 最大节流阀值
#
#     # 设置IAS与target_speed的差值范围
#     error_threshold = 150
#
#     # 计算IAS与target_speed的差值
#     error = IAS - target_speed
#
#     # 根据差值调整throttle_control
#     if abs(error) > error_threshold:
#         # 差值过大，加快调整速度
#         throttle_control = pid(error)
#     else:
#         # 差值较小，放缓调整速度
#         throttle_control = pid(error, dt=1)
#
#     # 限制throttle_control的取值范围
#     throttle_control = max(min(throttle_control, 0.5), -0.5)
#
#     # 根据throttle_control设置节流阀
#     if IAS < target_speed:
#         # IAS小于target_speed，增加节流阀
#         throttle = min(throttle + throttle_control, throttle_max)
#     else:
#         # IAS大于target_speed，减小节流阀
#         throttle = max(throttle + throttle_control, throttle_min)
#
#     # 设置节流阀控制值
#     set_throttle(throttle)
