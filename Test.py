import Fighting
import port8111
import math
import json
import requests
import time
import ujson
import rapidjson


url = "http://127.0.0.1:8111/state"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
}
session = requests.Session()
session.timeout = 5
# interval = 0.1
# response = session.get(url, headers=headers)
# print("Response Status:", response.status_code)
# print("Response Body (UTF-8):", response.text)
# print("Exiting...")

while True:
    response = session.get(url, headers=headers)
    # data = rapidjson.loads(response.text)
    # ias_value = data["IAS, km/h"]
    # response = session.get(url)
    # print("Response Status:", response.status_code)
    print("Response Body (UTF-8):", response.text)
    data = json.loads(response.text)
    ias_value = data["IAS, km/h"]
    # print("Exiting...")
    # time.sleep(interval)
    # print("IAS Value:", ias_value)

import requests
import time

# Define the URL and headers
url = "http://127.0.0.1:8111/state"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
}

# Create a session with timeout
session = requests.Session()
session.timeout = 5

# Create a loop to send requests at an interval
# interval = 0.1  # 100 milliseconds
# try:
while True:
    # Send the HTTP request
    response = session.get(url, headers=headers)

    # Print the response status
    # print("Response Status:", response.status_code)

    # Print the response body (UTF-8)
    print("Response Body (UTF-8):", response.text)

    # Wait for the next interval
    # time.sleep(interval)
# except KeyboardInterrupt:
#     print("Exiting...")

# i = 1
# while True:
#     map_size = port8111.get_size()
#     # print(f"地图尺寸：{map_size}m")
#     Vy, Hm, throttle, IAS, airbrake = port8111.getState()
#     print(f"空速：{IAS} 高度：{Hm} 爬升率：{Vy} 节流阀：{throttle}")
#     start_compass = port8111.get_compass()
#     airfield_height = Hm
#     print(f"起飞航向{start_compass}，起飞高度{airfield_height}m")
#     _, _, player_coordinates = port8111.get_coordinates()
#     print(f"玩家坐标{player_coordinates}")

# while i == 1:
#     (friendly_airport, checkpoint_1, checkpoint_2,
#      checkpoint_3, checkpoint_4, airfield_compass) = Fighting.checkpoint(map_size, start_compass)
#     checkpoint_collection = [friendly_airport, checkpoint_1, checkpoint_2, checkpoint_3, checkpoint_4]
#     i += 1

# print(
#     f"机场坐标：{friendly_airport}检查点1{checkpoint_1}检查点2{checkpoint_2}检查点3{checkpoint_3}检查点4{checkpoint_4}，")

# 定义圆心O、半径distance、点A、圆心角compass

# O = (0, 0)
# distance = 2
# A = (0, 1)
# compass = 60
# if 180 > compass >= 0:      # 如果大于90小于180，例如120，那么等于正常的60度，如果是60，那么就是正常的120
#     compass = 180 - compass
# elif 360 >= compass >= 180:
#     compass = 540 - compass
#
#
#
# # 计算圆心角的弧度值
# radians = compass * math.pi / 180
#
# # 计算B点的极坐标
# r = distance
# theta = math.pi / 2 - radians
#
# # 计算B点的直角坐标
# x = r * math.cos(theta)
# y = r * math.sin(theta)
# B = (x, y)
#
# # 打印B点的坐标
# print(f"B点的坐标为({x:.2f}, {y:.2f})")
