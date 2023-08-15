# http://desktop-rqq242g:8111/
import time

import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import re

retry_strategy = Retry(
    total=3,    # 最大重试次数（包括第一次请求）
    backoff_factor=0.1,     # 重试之间的退避因子，用于计算重试之间的等待时间
    status_forcelist=[500, 502, 503, 504]   # 需要触发重试的 HTTP 状态码列表
)
# 创建了一个 HTTPAdapter 实例，并将 Retry 实例传递给它
retry_strategy.method_whitelist = ["GET"]

adapter = HTTPAdapter(max_retries=retry_strategy)
pool = requests.Session()
pool.mount("http://", adapter)  # 创建了一个 Session 对象，并将适配器挂载到 http:// 前缀上

# 读取配置
# 读取文件
file = open('data.txt', 'r')
content = file.read()
file.close()

# 使用正则表达式提取数值
pattern = r'get=(\d+)'
match = re.search(pattern, content)
if match:
    value = match.group(1)
    num = int(value)
    print(f"get等待时间:{num}")
else:
    num = 0
    print("get等待时间重置为默认值")

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
# 通过传入参数获得指定数据
# def getData(url,str):
#     response = pool.get(url)
#     data = response.json()
#     try:
#         answer = data[str]
#         return answer
#     except KeyError:
#         return None
# http://localhost:8111/state
# 重要参数："AoA, deg":攻角    "H, m":高度   "power 1, hp": 发动机马力

# http://localhost:8111/indicators
# "throttle":节流阀  "type": "dummy_plane"=未起飞
# 炸弹点示例↓
# {"type":"bombing_point","color":"#fa0C00","color[]":[250,12,0],"blink":0,"icon":"bombing_point","icon_bg":"none","x":0.517530,"y":0.471646},

# 判断飞机是否出生
# def startReady():
#     url = 'http://localhost:8111/indicators'
#     str = "type"  # "type": "dummy_plane"=未重生飞机
#     type = getData(url, str)
#     return type

# 获取节流阀
def getThro():
    url = 'http://localhost:8111/state'
    # str = "throttle"  # "throttle":节流阀
    throttle = getData(url, "throttle 1, %")
    return throttle

def getState():
    url = 'http://localhost:8111/state'
    Vy, Hm, IAS, throttle = getData(url, "Vy, m/s", "H, m", "IAS, km/h", "throttle 1, %")
    if Vy is None:
        Vy = 0
    if Hm is None:
        Hm = 0
    if IAS is None:
        IAS = 0
    if throttle is None:
        throttle = 0
    # str = "Vy, m/s"    # "Vy, m/s":垂直速率
    # Vy = getData(url, str)
    # str = "H, m"        # "H, m":高度
    # Hm = getData(url, str)
    # str = "IAS, km/h"   # "IAS, km/h":空速
    # IAS = getData(url, str)

    # url = 'http://localhost:8111/indicators'
    # # str = "power 1, hp"        # "power 1, hp": 发动机马力
    # power = getData(url, "power 1, hp")
    time.sleep(num)
    return Vy, Hm, throttle, IAS

# url = 'http://localhost:8111/state'
# str = "Vy, m/s"    # "Vy, m/s":垂直速率
# Vy = getData(url, str)
# print("Vy")
# print(Vy)
# str = "H, m"        # "H, m":高度
# Hm = getData(url, str)
# print("H, m")
# print(Hm)
# str = "IAS, km/h"   # "IAS, km/h":空速
# IAs = getData(url, str)

# url = 'http://localhost:8111/indicators'
# str = "throttle"    # "throttle":节流阀
# throttle = getData(url, str)
# str = "power 1, hp"        # "power 1, hp": 发动机马力
# power = getData(url, str)
# return Vy, Hm, power ,IAs
# while True:
#     Vy, Hm, power, IAS = getState()
#     print(f"空速： {IAS} 高度： {Hm} 爬升率： {Vy} 发动机功率： {power}")