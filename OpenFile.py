import re


def read_file_and_extract_values(filename, patterns, default_values, value_descriptions):
    # 读取文件
    file = open(filename, 'r', encoding='utf-8')
    content = file.read()
    file.close()

    extracted_values = []
    for pattern, default_value, value_description in zip(patterns, default_values, value_descriptions):
        # 使用正则表达式提取数值
        match = re.search(pattern, content)
        if match:
            value = match.group(1)
            try:
                extracted_value = int(value)  # 尝试将值转换为整数
            except ValueError:
                try:
                    extracted_value = float(value)  # 尝试将值转换为浮点数
                except ValueError:
                    print(f"{value_description}无法转换为数值，重置为默认值")
                    extracted_value = default_value
            extracted_values.append(extracted_value)
        else:
            print(f"{value_description}重置为默认值")
            extracted_values.append(default_value)

    return extracted_values


def read_values():
    # 如果想要增加参数，那么这里需要增加字段
    patterns = [r'flight_mode=(\d+(\.\d+)?)',  # 修改：匹配整数或小数
                r'decelerate=(\d+(\.\d+)?)',
                r'reorienting_direction=(\d+(\.\d+)?)',
                r'infrared_decoy=(\d+(\.\d+)?)',
                r'bombing_distance=(\d+(\.\d+)?)',
                r'press_time=(\d+(\.\d+)?)',
                r'Harrier=(\d+)',
                r'Mode=(\d+)',
                r'delay_takeoff=(\d+)',
                r'speed_limit=(\d+)',
                r'max_speed=(\d+)']
    # 如果想要增加参数，那么这里需要增加默认值
    default_values = [0.5, -1, 0.5, 10, 3, 5, 0, 2, 0, 0, 950]
    # 如果想要增加参数，那么这里需要增加字段
    value_descriptions = ["数据请求延时",
                          "减速距离",
                          "方位调整延时",
                          "热诱抛洒距离",
                          "战区剩余距离判断",
                          "投弹键剩余按压时间",
                          "鹞式战机",
                          "飞行模式",
                          "延迟入场",
                          "限速开关",
                          "最大速度"]

    extracted_values = read_file_and_extract_values('Map.txt', patterns, default_values, value_descriptions)
    # 如果想要增加参数，那么下面需要增加变量
    (delay_time,
     decelerate,
     direction,
     fox_2,
     bombing_distance,
     press_time,
     harrier,
     mode,
     delay_takeoff,
     speed_limit,
     max_speed) = extracted_values  # 解包操作

    # 如果想要增加参数，那么这里需要返回值
    return (delay_time,
            decelerate,
            direction,
            fox_2,
            bombing_distance,
            press_time,
            harrier,
            mode,
            delay_takeoff,
            speed_limit,
            max_speed)


# 自动降落数据读取
def read_land():
    # 如果想要增加参数，那么这里需要增加字段
    patterns = [r'checkpoint_4_h=(\d+)',
                r'checkpoint_4_v=(\d+)',
                r'checkpoint_3_h=(\d+)',
                r'checkpoint_3_v=(\d+)',
                r'checkpoint_2_h=(\d+)',
                r'checkpoint_2_v=(\d+)',
                r'checkpoint_1_h=(\d+)',
                r'checkpoint_1_v=(\d+)',
                r'checkpoint_0_v=(\d+)']
    # 如果想要增加参数，那么这里需要增加默认值
    default_values = [1000, 900, 700, 700, 400, 500, 200, 300, 300]
    # 如果想要增加参数，那么这里需要增加字段
    value_descriptions = ["检查点4高度",
                          "检查点4速度",
                          "检查点3高度",
                          "检查点3速度",
                          "检查点2高度",
                          "检查点2速度",
                          "检查点1高度",
                          "检查点1速度",
                          "着陆速度"]

    extracted_values = read_file_and_extract_values('Map.txt', patterns, default_values, value_descriptions)
    # 如果想要增加参数，那么下面需要增加变量
    (checkpoint_4_h,
     checkpoint_4_v,
     checkpoint_3_h,
     checkpoint_3_v,
     checkpoint_2_h,
     checkpoint_2_v,
     checkpoint_1_h,
     checkpoint_1_v,
     checkpoint_0_v) = extracted_values  # 解包操作

    checkpoint_four = (checkpoint_4_h, checkpoint_4_v)
    checkpoint_three = (checkpoint_3_h, checkpoint_3_v)
    checkpoint_two = (checkpoint_2_h, checkpoint_2_v)
    checkpoint_one = (checkpoint_1_h, checkpoint_1_v)

    # 如果想要增加参数，那么这里需要返回值
    return (checkpoint_four,
            checkpoint_three,
            checkpoint_two,
            checkpoint_one,
            checkpoint_0_v)


# 端口请求模式读取
def read_port():
    # 如果想要增加参数，那么这里需要增加字段
    patterns = [r'port8111=(\d+)']
    # 如果想要增加参数，那么这里需要增加默认值
    default_values = [1]
    # 如果想要增加参数，那么这里需要增加字段
    value_descriptions = ["端口请求模式"]

    extracted_values = read_file_and_extract_values('Map.txt', patterns, default_values, value_descriptions)
    # 如果想要增加参数，那么下面需要增加变量
    port8111 = extracted_values  # 解包操作

    # 如果想要增加参数，那么这里需要返回值
    return port8111
