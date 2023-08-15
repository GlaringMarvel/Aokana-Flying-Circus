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
            extracted_value = int(value)
            extracted_values.append(extracted_value)
        else:
            print(f"{value_description}重置为默认值")
            extracted_values.append(default_value)

    return extracted_values


def read_values():
    # 如果想要增加参数，那么这里需要增加字段
    patterns = [r'flight_mode=(\d+)',
                r'decelerate=(\d+)',
                r'reorienting_direction=(\d+)',
                r'infrared_decoy=(\d+)',
                r'bombing_distance=(\d+)',
                r'press_time=(\d+)']
    # 如果想要增加参数，那么这里需要增加默认值
    default_values = [0.5, 0, 0.5, 10, 3, 5]
    # 如果想要增加参数，那么这里需要增加字段
    value_descriptions = ["数据请求延时", "减速距离", "方位调整延时", "热诱抛洒距离", "战区剩余距离判断", "投弹键剩余按压时间"]

    extracted_values = read_file_and_extract_values('Map.txt', patterns, default_values, value_descriptions)
    # 如果想要增加参数，那么下面需要增加变量
    delay_time, distance, direction, fox_2, bombing_distance, press_time = extracted_values  # 解包操作

    # 如果想要增加参数，那么这里需要返回值
    return delay_time, distance, direction, fox_2, bombing_distance, press_time
