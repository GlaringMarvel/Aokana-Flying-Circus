import time  # 调用时间函数
import GetWindow  # 调用窗口索引
import HangarMenu
import pyautogui  # 调用鼠标移动
import keyboard  # 调用键盘按键
import StateMachine
import port8111  # 调用8111端口
import Fighting  # 调用战斗中图像识别
import Map  # 地图识别
import OpenFile
import datetime


# 鼠标单击事件
def click():
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.mouseUp()


# CCRP开启
def ccrp_start():
    keyboard.press('o')
    time.sleep(0.1)
    keyboard.release('o')


# Esc单击事件
def esc():
    keyboard.press('esc')
    time.sleep(0.3)
    keyboard.release('esc')


# 单击【加入战斗】
def start_game(x, y):
    pyautogui.moveTo(x + 650, y + 70)
    time.sleep(1)
    click()


# 油门轴事件
def pushW():
    keyboard.press('w')
    time.sleep(3)
    keyboard.release('w')


# 鼠标移动事件：向上
def moveUp(m):
    keyboard.press(';')
    time.sleep(m)
    keyboard.release(';')


# 鼠标移动事件：向下
def moveDwon(m):
    keyboard.press('.')
    time.sleep(m)
    keyboard.release('.')


# 鼠标移动事件：向左
def moveL(m):
    keyboard.press(',')
    time.sleep(m)
    keyboard.release(',')


# 鼠标移动事件：向右
def moveR(m):
    keyboard.press('/')
    time.sleep(m)
    keyboard.release('/')


# 点击下方重新加入战斗
def restart(x, y):
    pyautogui.moveTo(x + 640, y + 650)
    time.sleep(1)
    click()


# 成员组锁定点击
def red_click(x, y):
    pyautogui.moveTo(x + 640, y + 415)
    time.sleep(1)
    click()


# 点击加入战斗（重生次数1）
def start_game_1(x, y):
    pyautogui.moveTo(x + 950, y + 710)
    time.sleep(1)
    click()


# 点击返回基地
def back(x, y):
    pyautogui.moveTo(x + 1000, y + 710)
    time.sleep(1)
    click()


# 鼠标居中
def mouse_center(x, y):
    pyautogui.moveTo(x + 650, y + 360)


# 减速板事件
def keyboard_h():
    keyboard.press('h')
    time.sleep(0.1)
    keyboard.release('h')


# 获取当前时间
def get_current_time():
    current_time = datetime.datetime.now()
    return current_time


# 开启热诱循环，致敬长空之王（bushi）
def fox_two():
    keyboard.press('p')
    time.sleep(0.1)
    keyboard.release('p')


# 获取data.txt中的设置
get_delay, _, direction_delay = OpenFile.read_values()
print(f"数据请求延时设置为：{get_delay}")
print(f"方向调整延时设置为：{direction_delay}")

# 设立判断标志
flag = 0
while True:
    # 获取窗口坐标
    x, y, center_x = GetWindow.window_found()
    print("窗口坐标 X：" + str(x) + "，Y：" + str(y))  # 输出窗口坐标
    # 机库判断循环
    while flag < 6:
        # 判断当前游戏状态，战局or机库
        hangar = StateMachine.declaration_death()
        if hangar == 0:  # 0 当前在机库中
            print("当前位置：机库")
            # 鼠标点击事件判断
            mouse_event = HangarMenu.mouse_event()
            if mouse_event == 0:  # 等待匹配
                flag = 0  # 0 不做任何操作，开始判断是否进入战局
                print("正在等待")
                time.sleep(1)
            elif mouse_event == 1:  # 点击加入战斗
                start_game(x, y)
                flag = 1  # 1 已点击加入战斗，开始判断是否开始匹配
                print("加入战斗")
                time.sleep(1)
            elif mouse_event == 2:  # 点击下方重新加入战斗
                restart(x, y)
                flag = 2  # 2 可能开始匹配或者进入研发界面，需要判断是否开始匹配
                print("重新加入战斗")
                time.sleep(1)
            elif mouse_event == 3:  # 点击成员组锁定
                red_click(x, y)
                print("成员组锁定,等待60s")
                flag = 3  # 3 成员组锁定，需要重新判断是否可以加入战斗
                time.sleep(60)
            elif mouse_event == 4:  # Esc事件
                mouse_center(x, y)
                time.sleep(1)
                esc()
                print("Esc")
                flag = 4  # 4 esc事件，需要重新判断是否可以加入战斗
                time.sleep(1)
            else:  # 防报错容错
                print("机库鼠标事件未知")
        # elif hangar == 1:   # 1 正在加载，无法请求地图
        #     wait = Waiting.waiting(x, y)
        #     if wait == 0:   # 未找到加载动画
        #         flag = 5    # 5 可能已加入战局或返回基地，需要重新读取地图
        elif hangar == 2:  # 2 飞机未起飞或坠毁，需要判断玩家是否在机场上
            print("位置判断")
            flag = 6  # 6 飞机位置判断
            break
        elif hangar == 3:  # 3 飞机正常飞行中
            print("正在飞行")
            flag = 7  # 7 飞机正常飞行中
            break
        elif hangar == 4:  # 4 载具未出生
            print("载具未出生")
            flag = 8  # 8 载具未出生
            break

    # 非正常战斗状态判断循环
    map_size = port8111.get_size()  # 获取地图大小
    print(f"地图尺寸：{map_size}m")
    while flag > 5:
        x, y, center_x = GetWindow.window_found()
        # 寻找加入战斗（重生次数1），寻找加入战斗后的取消按钮，寻找死亡后返回基地按钮
        battle_state = StateMachine.battle_state()
        if battle_state == 0:  # 寻找到加入战斗（重生次数1）
            start_game_1(x, y)  # 点击加入战斗（重生次数1）
            flag = 9  # 9 载具未出生,但已点击加入
            print("加入战斗（重生次数1）")
        elif battle_state == 2:  # 寻找死亡后返回基地按钮
            back(x, y)
            flag = 0  # 10 已点击返回基地
            print("返回基地")
            time.sleep(7)
            break
        elif battle_state == 3:
            bollen = Fighting.compare_coordinates()
            if bollen != -1:
                print("载具出生")
                flag = 10  # 载具出生
                break
            else:
                print("载具未出生")
        elif flag == 9:
            bollen = Fighting.compare_coordinates()
            if bollen != -1:
                print("载具出生")
                flag = 10  # 载具出生
                break
            else:
                print("载具未出生")

    time_flag = 0
    # 战斗操作判断
    while flag > 8:
        # 判断节流阀位置
        Vy, Hm, throttle, IAS = port8111.getState()
        if throttle < 110 and 11 > flag > 8:
            print(f"节流阀：{throttle} 正在加力;")
            pushW()
            h1, h2, v1, v2, v3, num, _ = Map.foundMap()  # 地图识别
            print(f"飞行高度区间: {h1}m - {h2}m, v1: {v1}, v2: {v2}, v3: {v3}")
            flag = 12

        ccrp_flag = 0
        speed_brake = 0
        # 飞行状态循环判断
        while True:
            Vy, Hm, throttle, IAS = port8111.getState()
            print(f"空速：{IAS} 高度：{Hm} 爬升率：{Vy} 节流阀：{throttle}")
            # 关于y轴控制的判断
            keyboard_event = Fighting.flight_controller(h1, h2, v1, v2, v3, Vy, Hm, throttle, IAS)
            if keyboard_event == 0:
                # 以下是关于载具是否坠毁的判断,懒得简化了
                bollen = Fighting.compare_coordinates()
                if bollen == 1:
                    print("载具位于机场")
                    if throttle < 110 and flag == 10:
                        print(f"节流阀：{throttle} 正在加力;")
                        pushW()
                        h1, h2, v1, v2, v3, num, _ = Map.foundMap()  # 地图识别
                        print(f"飞行高度区间: {h1}m - {h2}m, v1: {v1}, v2: {v2}, v3: {v3}")
                        flag = 12
                else:
                    print("载具不位于机场")
                    flag = 6
                    keyboard.release('u')
                    break
            # 2为下压，8为抬头
            elif keyboard_event == 2:
                moveDwon(m=0.01)
                print("下降：小幅")
            elif keyboard_event == 22:
                moveDwon(m=0.05)
                print("下降：大幅")
            elif keyboard_event == 8:
                moveUp(m=0.01)
                print("爬升：小幅")
            elif keyboard_event == 88:
                moveUp(m=0.05)
                print("爬升：大幅")
            time.sleep(get_delay)

            # 开启CCRP
            if IAS > 500 and ccrp_flag == 0:
                # 激活CCRP
                ccrp_start()
                ccrp_flag = 1
                time.sleep(1)
                # frequency = 0
                # while frequency < num:      # 实现选择第几个战区
                #     ccrp_start()
                #     ccrp_flag = 1
                #     frequency += 1
                #     time.sleep(1)
            elif ccrp_flag != 0:
                keyboard.press('u')  # 空格猴子

            # 关于航向的控制（x轴）
            if time_flag < 2:  # 如果玩家未完成投弹
                keyboard_event = Fighting.heading_control(IAS, map_size, time_flag, num)
            elif time_flag == 2:  # 如果玩家完成投弹
                keyboard_event = Fighting.enemy_airfield(map_size, speed_brake)
            if keyboard_event == 666:
                moveR(m=0.5)
                print("航向修正：右")
            elif keyboard_event == 444:
                moveL(m=0.5)
                print("航向修正：左")
            elif keyboard_event == 66:
                moveR(m=0.05)
                print("航向修正：右")
            elif keyboard_event == 44:
                moveL(m=0.05)
                print("航向修正：左")
            elif keyboard_event == 6:
                moveR(m=0.01)
                print("航向修正：右")
            elif keyboard_event == 4:
                moveL(m=0.01)
                print("航向修正：左")
            elif keyboard_event == 1 and speed_brake == 0:  # 开启减速板
                keyboard_h()
                print("开启减速板")
                speed_brake = 1  # 减速板判定
            elif keyboard_event == 5 and time_flag == 0:  # 即将到达战局，开始计时
                # 长空之王专属热诱弹
                fox_two()
                # 获取当前时间
                start_time = get_current_time()
                time_flag = 1

            # 计算经过的时间差
            if time_flag == 1:
                end_time = get_current_time()
                time_difference = end_time - start_time
                seconds_passed = time_difference.total_seconds()
                if seconds_passed > 10:  # 弹起投弹键
                    keyboard.release('u')
                    time_flag = 2
                    if speed_brake == 1:
                        keyboard_h()
                        speed_brake = 0
            time.sleep(direction_delay)
