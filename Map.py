import requests
import hashlib


def calculate_md5(file_data):
    md5_hash = hashlib.md5()
    md5_hash.update(file_data)
    return md5_hash.hexdigest()


# 这些内容是校验MD5值
def MD5():
    url = 'http://localhost:8111/map.img'
    try:
        response = requests.get(url, timeout=5)  # 设置超时时间为5秒
        if response.status_code == 200:
            file_data = response.content
            md5_value = calculate_md5(file_data)
            return md5_value  # 返回md5值
        else:
            print("获取地图失败")
    except requests.exceptions.Timeout:
        print("地图请求超时")
        return None


# 获取地图数据
def mapData(map_name):
    # 打开文件
    with open('Map.txt', 'r', encoding='utf-8') as file:  # 打开文件并指定编码方式为UTF-8
        # 逐行读取文件内容
        for line in file:
            if map_name in line:
                data = line.split(':')[1].strip()  # 提取冒号后面的数据部分并去除首尾空格
                values = data.split(',')  # 将数据部分按逗号分割成不同的部分
                h1 = int(values[0].split('=')[1])
                h2 = int(values[1].split('=')[1])
                v1 = int(values[2].split('=')[1])
                v2 = int(values[3].split('=')[1])
                v3 = int(values[4].split('=')[1])
                number = int(values[5].split('=')[1])
                time = int(values[6].split('=')[1])
                north_direction = int(values[7].split('=')[1])
                south_direction = int(values[8].split('=')[1])
                return h1, h2, v1, v2, v3, number, time, north_direction, south_direction
        return None


def foundMap():
    h1 = 1000
    h2 = 1500
    v1 = 5
    v2 = 15
    v3 = 20
    number = map_found = time = north_direction = south_direction = 1
    NoMap = 'e4e7e3c8f378aa215cdd19a1f4c3a1b3'
    Vietnam = 'a546079510cd41d19f5a26bbbc4e738d'
    SinaiPeninsula = '24a39808b80abe5359d23ec454ffb536'
    GolanHeights = '166b151d03e6ecb507b0af3ba19583cf'
    Spain = '4c088fd502175f94fe1cf82a58135d82'
    PyreneesMountains = 'd8997861e6b8bb555064bb554719a18b'
    BigCity = 'ed9014e03f959769e15f31bc263838a5'
    Afghanistan = 'eeadce7b9a2be282c84bb72e982d0302'
    RockiesCanyon = '924d7cadb5bf24f243474386195251b7'
    md5 = MD5()
    if md5 == NoMap:
        print("非战斗中")
        map_found = 0
        return h1, h2, v1, v2, v3, number, map_found, time, north_direction, south_direction
    elif md5 is None:
        print("正在加载")
        map_found = 2
        return h1, h2, v1, v2, v3, number, map_found, time, north_direction, south_direction
    elif md5 == Vietnam:
        print("地图 越南")
        h1, h2, v1, v2, v3, number, time, north_direction, south_direction = mapData('Vietnam')
        return h1, h2, v1, v2, v3, number, map_found, time, north_direction, south_direction
    elif md5 == SinaiPeninsula:
        print("地图 西奈半岛")
        h1, h2, v1, v2, v3, number, time, north_direction, south_direction = mapData('SinaiPeninsula')
        return h1, h2, v1, v2, v3, number, map_found, time, north_direction, south_direction
    elif md5 == GolanHeights:
        print("地图 戈兰高地")
        h1, h2, v1, v2, v3, number, time, north_direction, south_direction = mapData('GolanHeights')
        return h1, h2, v1, v2, v3, number, map_found, time, north_direction, south_direction
    elif md5 == Spain:
        print("地图 西班牙")
        h1, h2, v1, v2, v3, number, time, north_direction, south_direction = mapData('Spain')
        return h1, h2, v1, v2, v3, number, map_found, time, north_direction, south_direction
    elif md5 == PyreneesMountains:
        print("地图 比利牛斯山脉")
        h1, h2, v1, v2, v3, number, time, north_direction, south_direction = mapData('PyreneesMountains')
        return h1, h2, v1, v2, v3, number, map_found, time, north_direction, south_direction
    elif md5 == BigCity:
        print("地图 大都会")
        h1, h2, v1, v2, v3, number, time, north_direction, south_direction = mapData('BigCity')
        return h1, h2, v1, v2, v3, number, map_found, time, north_direction, south_direction
    elif md5 == Afghanistan:
        print("地图 阿富汗")
        h1, h2, v1, v2, v3, number, time, north_direction, south_direction = mapData('Afghanistan')
        return h1, h2, v1, v2, v3, number, map_found, time, north_direction, south_direction
    elif md5 == RockiesCanyon:
        print("地图 洛基峡谷")
        h1, h2, v1, v2, v3, number, time, north_direction, south_direction = mapData('RockiesCanyon')
        return h1, h2, v1, v2, v3, number, map_found, time, north_direction, south_direction
    else:
        return h1, h2, v1, v2, v3, number, map_found, time, north_direction, south_direction
