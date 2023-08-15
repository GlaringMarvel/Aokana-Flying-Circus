import time
import pygetwindow as gw  # 引入包pygetwindow使用别名gw（getWindows）


def window_found():
    while True:
        try:
            window = gw.getWindowsWithTitle('War Thunder')[0]  # 寻找游戏窗口
            x = window.left  # 窗口的左边界坐标
            y = window.top  # 窗口的顶部边界坐标

            # 测试新准星识别
            window_width, window_height = window.size

            center_x = window.left + (window_width // 2)

            # print("窗口坐标 X：" + str(x) + "，Y：" + str(y))  # 输出窗口坐标
            window.activate()
            time.sleep(3)
            return x, y, center_x
        except IndexError:
            print("未找到游戏窗口")
            time.sleep(3)
