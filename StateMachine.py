import Back
import Fighting
import Map
import port8111
import GetWindow
import HangarMenu
import Waiting


# 初始判断
# 死亡状态判定
def declaration_death():
    h1, h2, v1, v2, v3, _, map_found, _, _, _ = Map.foundMap()
    if map_found == 0:  # 判断地图，是否在战局内
        flag = 0  # 第一种情况，非战斗中
        return flag
    elif map_found == 2:
        flag = 1  # 第二种情况，正在加载，无法请求地图
        return flag
    print(f"飞行高度区间: {h1}m - {h2}m, v1: {v1}, v2: {v2}, v3: {v3}")
    _, _, throttle, IAS, _ = port8111.getState()
    if throttle == 0 and IAS < 100:  # 判断是否死亡
        flag = 2  # 第三种情况，等待起飞/死亡
        return flag
    elif throttle != 0 and IAS > 100:  # 判断是否战斗中
        flag = 3  # 第四种情况，战斗中
        return flag
    elif throttle == 0 and IAS > 100:  # 逆天bvvd，飞机加入战斗界面空速还挺高
        flag = 4  # 第五种情况，玩家未出生
        return flag


# 机库内的识别
# 死亡状态判断返回flag为0时
def hangar_identify():
    # 获取窗口坐标
    x, y, center_x = GetWindow.window_found()
    battle_picture = HangarMenu.battle_found(x, y)  # 寻找加入战斗按钮
    if battle_picture == 1:  # 如果找到加入战斗按钮
        flag = 1  # 找到标志为1
        return flag
    cancel_picture = Waiting.cancel_search(x, y)  # 寻找取消按钮
    if cancel_picture == 1:  # 如果找到取消按钮
        flag = 2  # 找到标志为2
        return flag
    cancel_picture1 = Waiting.cancel_search_1(x, y)  # 寻找取消按钮1
    if cancel_picture1 == 1:  # 如果找到取消按钮
        flag = 2  # 找到标志为2
        return flag
    confirm_picture = Back.confirm_picture(x, y)  # 寻找研发前的确认按钮
    if confirm_picture == 1:  # 如果找到研发前的确认按钮
        flag = 3  # 找到标志为3
        return flag
    restart = Back.restart(x, y)  # 寻找重新加入战斗
    if restart == 1:  # 如果找到重新加入战斗按钮
        flag = 4  # 找到标志为4
        return flag
    red_warning = Back.red_warning(x, y)  # 成员组是否锁定
    if red_warning == 1:
        flag = 5  # 如果成员组锁定
        return flag
    else:  # 如果全部无法识别，返回标志5
        flag = 6  # 需要Esc
        return flag


# 战局中的非正常状态识别
# 死亡状态判断返回flag为2时
def battle_state():
    # 获取窗口坐标
    x, y, center_x = GetWindow.window_found()
    start_game = Waiting.start_game(x, y)  # 寻找加入战斗（重生次数1）
    if start_game == 1:
        flag = 0  # 找到标志为0
        return flag
    start_cancel = Waiting.start_cancel(x, y)  # 寻找加入战斗后的取消按钮
    if start_cancel == 1:
        flag = 1  # 找到标志为1
        return flag
    back_picture = Fighting.back(x, y)  # 寻找死亡后返回基地按钮
    if back_picture == 1:
        flag = 2  # 找到标志为2
        return flag
    else:
        flag = 3  # 之后判断玩家是否处于己方机场，标志为3
        return flag
