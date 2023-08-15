import time
from python_imagesearch.imagesearch import imagesearcharea  # 引入识图函数
import Fighting

def imgSearch(imgData, sx, sy, ex, ey ,precision):
    pos = imagesearcharea(imgData, sx, sy, ex, ey, precision)
    if pos[0] != -1:
        bollen = 1
        return bollen
    else:
        bollen = 0
        return bollen

def imgWT(x,y):
        sx = x + 300
        sy = y
        ex = x + 900
        ey = y + 500
        precision = 0.8
        imgData = "image/Back/WTback.png"
        bollen = imgSearch(imgData, sx, sy, ex, ey, precision)
        return bollen

def imgRe(x,y):
    sx = x + 300
    sy = y + 400
    ex = x + 900
    ey = y + 720
    precision = 0.9
    imgData = "image/Back/ReStart.png"
    bollen = imgSearch(imgData, sx, sy, ex, ey, precision)
    return bollen

def imgCon(x,y):
    sx = x + 300
    sy = y + 400
    ex = x + 900
    ey = y + 720
    imgData = "image/Back/Confirm.png"
    precision = 0.9
    bollen = imgSearch(imgData, sx, sy, ex, ey, precision)
    return bollen

def imgBuy(x,y):
    sx = x + 700
    sy = y + 300
    ex = x + 1000
    ey = y + 600
    precision = 0.6
    imgData = "image/Back/Buy.png"
    bollen = imgSearch(imgData, sx, sy, ex, ey, precision)
    return bollen

def imgRed(x, y):
    sx = x + 400
    sy = y + 300
    ex = x + 800
    ey = y + 600
    precision = 0.9
    imgData = "image/Back/Red.png"
    bollen = imgSearch(imgData, sx, sy, ex, ey, precision)
    return bollen

def imgStart(x, y):
    sx = x + 400
    sy = y
    ex = x + 800
    ey = y + 300
    precision = 0.8
    imgData = "image/HangarMenu/Battle.png"
    bollen = imgSearch(imgData, sx, sy, ex, ey, precision)
    return bollen

def Buy(x, y):
    bollen1 = imgBuy(x, y)
    bollen2 = imgWT(x, y)
    bollen = 0
    if bollen1 == 1 and bollen2 == 1:
        bollen = 1
        print("购买界面")
        return bollen
    else:
        return bollen

def imgFound(x, y):
    back = 0
    num = 0
    while num < 10:
        bollen = Fighting.back(x, y)
        if bollen == 1:     # 返回基地
            back = 1
            return back
        bollen = imgWT(x, y)
        if bollen == 1:
            time.sleep(3)
            print("正在加载")
        bollen = imgRe(x, y)
        if bollen == 1:     # 加入战斗
            back = 2
            return back
        bollen = imgCon(x, y)       # 研发
        if bollen == 1:
            back = 3
            return back
        num += 1