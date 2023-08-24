import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import json
import OpenFile

retry_strategy = Retry(
    total=3,  # 最大重试次数（包括第一次请求）
    backoff_factor=0.1,  # 重试之间的退避因子，用于计算重试之间的等待时间
    status_forcelist=[500, 502, 503, 504]  # 需要触发重试的 HTTP 状态码列表
)
# 创建了一个 HTTPAdapter 实例，并将 Retry 实例传递给它
retry_strategy.method_whitelist = ["GET"]

adapter = HTTPAdapter(max_retries=retry_strategy)
pool = requests.Session()
pool.mount("http://", adapter)  # 创建了一个 Session 对象，并将适配器挂载到 http:// 前缀上

# 设置请求模式
mode = OpenFile.read_port()
if mode == 1:
    address = 'localhost'
else:
    address = '127.0.0.1'


# 访问端口获取数据
def getData(url, *args):
    response = pool.get(url)
    data = response.json()
    result = []
    for arg in args:
        try:
            answer = data[arg]
            result.append(answer)
        except KeyError:
            result.append(None)
    return tuple(result)


# 获取飞行参数
def getState():
    url = 'http://' + address + ':8111/state'
    Vy, Hm, IAS, throttle, airbrake = getData(url, "Vy, m/s", "H, m", "IAS, km/h", "throttle 1, %", "airbrake, %")
    if Vy is None:
        Vy = 0
    if Hm is None:
        Hm = 0
    if IAS is None:
        IAS = 0
    if throttle is None:
        throttle = 0
    if airbrake is None:
        airbrake = 0
    return Vy, Hm, throttle, IAS, airbrake


# 获取数据
def extractCoordinates(data, color):
    coordinates = []
    for item in data:
        if item.get("color") == color:
            coordinates.append((item.get("sx"), item.get("sy")))
    return coordinates


def extractPlayerCoordinates(data):
    coordinates = []
    for item in data:
        if item.get("icon") == "Player":
            coordinates.append((item.get("x"), item.get("y")))
    return coordinates


# 获取双方机场坐标以及玩家坐标
def get_coordinates():
    url = 'http://' + address + ':8111/map_obj.json'
    response = pool.get(url)  # 使用连接池发送请求
    data = response.json()
    player_coordinates = (-1, -1)
    friendly_airport = (-1, -1)
    enemy_airport = (-1, -1)

    for item in data:
        # 己方机场
        if item.get("type") == "airfield" and item.get("color") == "#174DFF":
            fx = item.get("sx")
            fy = item.get("sy")
            friendly_airport = (fx, fy)
        # 敌方机场
        elif item.get("type") == "airfield" and item.get("color") == "#fa0C00":
            sx = item.get("sx")
            sy = item.get("sy")
            enemy_airport = (sx, sy)
        # 玩家坐标
        elif item.get("icon") == "Player":
            x = item.get("x")
            y = item.get("y")
            player_coordinates = (x, y)

    # 如果玩家坐标未获取到，则创建 (-1, -1)
    # if player_coordinates is None:
    #     player_coordinates = (-1, -1)

    return friendly_airport, enemy_airport, player_coordinates


# 获得战区坐标和载具坐标
def get_bombing_point_coordinates():
    url = 'http://' + address + ':8111//map_obj.json'
    response = pool.get(url)  # 使用连接池发送请求
    data = response.json()
    player_coordinates = (-1, -1)
    bombing_points = (-1, -1)

    for obj in data:
        if obj["icon"] == "bombing_point":
            bombing_points = (obj["x"], obj["y"])
            break

    for obj in data:
        if obj["icon"] == "Player":
            player_coordinates = (obj["x"], obj["y"])
            break

    return player_coordinates, bombing_points


# 飞机航向专属get
def get_indicators(url, *args):
    response = pool.get(url)
    data = response.json()
    result = []
    for arg in args:
        try:
            answer = data[arg]
            result.append(answer)
        except KeyError:
            result.append(None)
    return result[0] if len(result) > 0 else None


# 获得飞机航向
def get_compass():
    url = 'http://' + address + ':8111/indicators'
    compass = get_indicators(url, "compass")
    if compass is None:
        compass = 0
    return compass


# 获得地图大小
def get_size():
    try:
        url = 'http://' + address + ':8111/map_info.json'
        response = pool.get(url)  # 使用连接池发送请求
        data = response.json()  # 解析 JSON 数据

        # 获取 "grid_size" 中的第一个数值
        grid_size = data["grid_size"][0]
    except (requests.RequestException, KeyError, IndexError):
        # 捕获请求异常、KeyError（当"grid_size"不存在）和IndexError（当"grid_size"为空列表）异常
        grid_size = 65535

    return grid_size


# 获得战区坐标和载具坐标(test)
def get_bombing_point_select(index):
    url = 'http://' + address + ':8111/map_obj.json'
    response = requests.get(url)  # 发送请求获取数据

    try:
        data = response.json()
    except json.JSONDecodeError as e:
        # 处理JSONDecodeError异常
        print("JSON解析错误:", e)
        # 或者提供默认值
        data = []

    player_coordinates = (-1, -1)
    bombing_points = []  # 存储所有的 bombing_point 坐标

    # 寻找玩家坐标
    for obj in data:
        if obj["icon"] == "Player":
            player_coordinates = (obj["x"], obj["y"])
            break

    # 寻找战区坐标
    for obj in data:
        if obj["icon"] == "bombing_point":
            bombing_points.append((obj["x"], obj["y"]))

    # 获得战区个数
    amount = len(bombing_points)

    # 如果地图上不存在战区
    if len(bombing_points) == 0:
        bombing_points.append((-1, -1))

    if index > len(bombing_points):
        index = len(bombing_points)
    elif index < 0:
        index = 0

    return player_coordinates, bombing_points[index], amount
