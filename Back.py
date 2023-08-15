from python_imagesearch.imagesearch import imagesearcharea  # 引入识图函数


def imgSearch(imgData, sx, sy, ex, ey, precision):
    pos = imagesearcharea(imgData, sx, sy, ex, ey, precision)
    if pos[0] != -1:
        bollen = 1
        return bollen
    else:
        bollen = 0
        return bollen


def imgWT(x, y):
    sx = x + 300
    sy = y
    ex = x + 900
    ey = y + 500
    precision = 0.8
    imgData = "image/Back/WTback.png"
    bollen = imgSearch(imgData, sx, sy, ex, ey, precision)
    return bollen


def restart(x, y):
    sx = x + 300
    sy = y + 400
    ex = x + 900
    ey = y + 720
    precision = 0.9
    imgData = "image/Back/ReStart.png"
    bollen = imgSearch(imgData, sx, sy, ex, ey, precision)
    return bollen


def confirm_picture(x, y):
    sx = x + 300
    sy = y + 400
    ex = x + 900
    ey = y + 720
    imgData = "image/Back/Confirm.png"
    precision = 0.9
    bollen = imgSearch(imgData, sx, sy, ex, ey, precision)
    return bollen


def red_warning(x, y):
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
