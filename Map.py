import requests
import hashlib

def calculate_md5(file_data):
    md5_hash = hashlib.md5()
    md5_hash.update(file_data)
    return md5_hash.hexdigest()

# 这些内容是校验MD5值
def MD5():
    url = 'http://localhost:8111/map.img'
    response = requests.get(url)

    if response.status_code == 200:
        file_data = response.content
        md5_value = calculate_md5(file_data)
        return md5_value    # 返回md5值
    else:
        print("获取地图失败")

# 获取地图数据
def mapData(map_name):
    # 打开文件
    with open('Map.txt', 'r', encoding='utf-8') as file:            # 打开文件并指定编码方式为UTF-8
        # 逐行读取文件内容
        for line in file:
            if map_name in line:
                data = line.split(':')[1].strip()                   # 提取冒号后面的数据部分并去除首尾空格
                values = data.split(',')                            # 将数据部分按逗号分割成不同的部分
                h1 = int(values[0].split('=')[1])
                h2 = int(values[1].split('=')[1])
                v1 = int(values[2].split('=')[1])
                v2 = int(values[3].split('=')[1])
                v3 = int(values[4].split('=')[1])
                return h1, h2, v1, v2, v3
        return None

def foundMap():
    h1 = 1000
    h2 = 1500
    v1 = 5
    v2 = 15
    v3 = 20
    press = 1
    Vietnam = 'a546079510cd41d19f5a26bbbc4e738d'
    SinaiPeninsula = '24a39808b80abe5359d23ec454ffb536'
    GolanHeights = '166b151d03e6ecb507b0af3ba19583cf'
    Spain = '4c088fd502175f94fe1cf82a58135d82'
    PyreneesMountains = 'd8997861e6b8bb555064bb554719a18b'
    BigCity = 'ed9014e03f959769e15f31bc263838a5'
    md5 = MD5()
    if md5 == Vietnam:
        print("地图 越南")
        press = 1
        h1, h2, v1, v2, v3 = mapData('Vietnam')
        return h1, h2, v1, v2, v3, press
    elif md5 == SinaiPeninsula:
        print("地图 西奈半岛")
        press = 1
        h1, h2, v1, v2, v3 = mapData('SinaiPeninsula')
        return h1, h2, v1, v2, v3, press
    elif md5 == GolanHeights:
        print("地图 戈兰高地")
        press = 1
        h1, h2, v1, v2, v3 = mapData('GolanHeights')
        return h1, h2, v1, v2, v3, press
    elif md5 == Spain:
        print("地图 西班牙")
        press = 2
        h1, h2, v1, v2, v3 = mapData('Spain')
        return h1, h2, v1, v2, v3, press
    elif md5 == PyreneesMountains:
        print("地图 比利牛斯山脉")
        press = 1
        h1, h2, v1, v2, v3 = mapData('PyreneesMountains')
        return h1, h2, v1, v2, v3, press
    elif md5 == BigCity:
        print("地图 大都会")
        press = 2
        h1, h2, v1, v2, v3 = mapData('BigCity')
        return h1, h2, v1, v2, v3, press
    else:
        return h1, h2, v1, v2, v3, press

