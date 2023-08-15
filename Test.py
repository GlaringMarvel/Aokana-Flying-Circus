import time
import re
import Back
import Fighting
import pygetwindow as gw    # 引入包pygetwindow使用别名gw（getWindows）
import pyautogui




# x=0
# y=0
# try:
#     window = gw.getWindowsWithTitle('War Thunder')[0]  # 寻找游戏窗口
#     x = window.left  # 窗口的左边界坐标
#     y = window.top  # 窗口的顶部边界坐标
#     print("成功找到游戏\n")
#     print("窗口坐标 X：" + str(x) + "，Y：" + str(y))  # 输出窗口坐标
#     print("请勿随意拖动窗口")
#     window.activate()
#     time.sleep(2)
# except IndexError:
#     print("未找到游戏窗口")
#     time.sleep(2)
# bollen = Back.imgWT(x, y)
# print(bollen)
# flag = Back.imgFound(x, y)
# print(flag)
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

else:
    speed = 900
    print("空速重置为默认值")


def find_country_data(country):
    with open('Map.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if country in line:
                data = line.split(':')[1].strip()
                values = data.split(',')
                h1 = int(values[0].split('=')[1])
                h2 = int(values[1].split('=')[1])
                v1 = int(values[2].split('=')[1])
                v2 = int(values[3].split('=')[1])
                v3 = int(values[4].split('=')[1])
                return h1, h2, v1, v2, v3
    return None

country_data = find_country_data("Spain")
if country_data:
    h1, h2, v1, v2, v3 = country_data
    print(f"h1: {h1}, h2: {h2}, v1: {v1}, v2: {v2}, v3: {v3}")
else:
    print("Country data not found.")
