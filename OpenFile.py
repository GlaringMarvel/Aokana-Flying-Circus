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
    patterns = [r'flight_mode=(\d+)', r'decelerate=(\d+)', r'reorienting_direction=(\d+)']
    default_values = [0, 0, 0]
    value_descriptions = ["数据请求延时", "减速距离", "方位调整延时"]

    extracted_values = read_file_and_extract_values('Map.txt', patterns, default_values, value_descriptions)
    # 如果想要增加参数，那么下面也需要增加
    delay_time, distance, direction = extracted_values  # 解包操作

    return delay_time, distance, direction
