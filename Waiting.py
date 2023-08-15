from python_imagesearch.imagesearch import imagesearcharea  # 引入识图函数


# 识图函数
def imgSearch(imgData, sx, sy, ex, ey):
    pos = imagesearcharea(imgData, sx, sy, ex, ey, precision=0.8)
    if pos[0] != -1:
        bollen = 1
        return bollen
    else:
        bollen = 0
        return bollen


# 【取消】按钮识别
def cancel_search(x, y):
    sx = x + 400
    sy = y
    ex = x + 800
    ey = y + 300
    imgData = "image/Loading/Cancel.png"
    bollen = imgSearch(imgData, sx, sy, ex, ey)
    if bollen == 1:
        print("正在匹配")
        return bollen
    else:
        bollen = 0
        return bollen


# 【取消】按钮识别2
def cancel_search_1(x, y):
    sx = x + 400
    sy = y
    ex = x + 800
    ey = y + 300
    imgData = "image/Loading/Cancel_1.png"
    bollen = imgSearch(imgData, sx, sy, ex, ey)
    if bollen == 1:
        print("正在匹配")
        return bollen
    else:
        bollen = 0
        return bollen


# 正在加入游戏界面识别
def wait_join(x, y):
    sx = x + 400
    sy = y + 300
    ex = x + 800
    ey = y + 700
    imgData = "image/Loading/WaitingJoin.png"
    bollen = imgSearch(imgData, sx, sy, ex, ey)
    if bollen == 1:
        print("正在加入游戏")
        print("空战-历史性能\n")
        return bollen
    else:
        bollen = 0
        return bollen


# 正在载入游戏界面识别
def wait_load(x, y):
    sx = x + 300
    sy = y
    ex = x + 900
    ey = y + 500
    imgData = "image/Loading/WarThunder.png"
    bollen = imgSearch(imgData, sx, sy, ex, ey)
    return bollen


# 开始战斗界面识别
def start_game(x, y):
    sx = x + 600
    sy = y + 500
    ex = x + 1500
    ey = y + 1600
    imgData = "image/Loading/StartGame.png"
    bollen = imgSearch(imgData, sx, sy, ex, ey)
    return bollen


# 【取消】按钮搜索
def start_cancel(x, y):
    sx = x
    sy = y + 500
    ex = x + 600
    ey = y + 800
    imgData = "image/Loading/StartCancel.png"
    bollen = imgSearch(imgData, sx, sy, ex, ey)
    return bollen

# 点击任何开始战斗按钮之后会到此判断
# def waiting(x, y):
#     wait = 1
#     while wait == 1:
#         cancel = start_cancel(x, y)
#         join = wait_join(x, y)
#         load = wait_load(x, y)
#         if join == 0 and load == 0 and cancel == 0:
#             wait = 0
#             bollen = 0          # 0 代表无法找到加入战斗和加载图片，需要重新判断机库还是战局
#             return bollen
#         else:
#             print("正在等待")
#             time.sleep(1)

# 循环判断是否加入战斗
# def waitSearch(x, y):
#     num = 0
#     bollen = 0
#     while num < 1000:
#         time.sleep(0.5)
#         # 匹配界面识别
#         bollen = waitCancel(x, y)
#         if bollen == 1:
#             num == 0
#             time.sleep(2)
#         # 加入游戏界面识别
#         bollen = waitJoin(x, y)
#         if bollen == 1:
#             num == 0
#             time.sleep(1)
#         # 载入游戏界面识别
#         bollen = waitLoad(x, y)
#         if bollen == 1:
#             print("正在载入……\n")
#             num == 0
#             time.sleep(1)
#         # 关键点：开始战斗界面识别
#         bollen = startGame(x, y)
#         if bollen == -1:
#             return bollen
#         num += 1
#     print(num)
