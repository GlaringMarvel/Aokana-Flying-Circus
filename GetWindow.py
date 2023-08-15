import time
import pygetwindow as gw    # 引入包pygetwindow使用别名gw（getWindows）

print("请以管理员身份运行")
time.sleep(1)
print("本软件完全开源免费，如果您在其他商家处购买到本产品，请主动联系购买平台进行退款")
time.sleep(1)
print("启动完毕，正在寻找游戏……")

x = 0
y = 0
def returData():
    while True:
        try:
            window = gw.getWindowsWithTitle('War Thunder')[0]   # 寻找游戏窗口
            x = window.left  # 窗口的左边界坐标
            y = window.top  # 窗口的顶部边界坐标

            # 测试新准星识别
            window_width, window_height = window.size

            center_x = window.left + (window_width // 2)

            print("成功找到游戏\n")
            print("窗口坐标 X："+str(x) + "，Y：" + str(y))    # 输出窗口坐标
            print("请勿随意拖动窗口")
            window.activate()
            time.sleep(3)
            return x, y, center_x
        except IndexError:
            print("未找到游戏窗口")
            time.sleep(3)