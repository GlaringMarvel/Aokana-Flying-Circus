import time
import pygetwindow as gw  # 引入包pygetwindow使用别名gw（getWindows）

# 介绍
print("本软件完全开源免费，如果你是付费购买，请自行联系商家或者平台退款")
print("项目地址：https://github.com/GlaringMarvel/Aokana-Flying-Circus")
print("详情请看README.md")
print("作者：天之川桔猫 ——BiliBili\n")
print("请勿随意移动游戏窗口\n")
time.sleep(3)


# 寻找窗口
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
