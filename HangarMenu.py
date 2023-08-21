from python_imagesearch.imagesearch import imagesearcharea  # 引入识图函数
import StateMachine


def battle_found(x, y):
    pos = imagesearcharea("image/HangarMenu/Battle.png", x + 400, y, x + 800, y + 300, precision=0.7)
    if pos[0] != -1:
        return 1  # 返回值1，识别成功
    else:
        return 0  # 返回值0，识别失败


# 判断接下来机库内鼠标行动的依据
def mouse_event():
    button_found = StateMachine.hangar_identify()
    if button_found == 1:  # 加入战斗按钮
        event = 1
        return event
    elif button_found == 2:  # 取消按钮
        event = 0
        return event
    elif button_found == 3:  # 研发前的确认按钮
        event = 2
        return event
    elif button_found == 4:  # 重新加入战斗按钮
        event = 2
        return event
    elif button_found == 5:  # 成员组锁定
        event = 3
        return event
    else:  # 无法识别,Esc事件
        event = 4
        return event
