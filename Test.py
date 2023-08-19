import port8111

i = 0
while True:
    bombing_point = port8111.get_bombing_point_select(i)
    if bombing_point:
        print(f"战区：{i+1} 坐标：{bombing_point}")
    else:
        print("指定的 bombing_point 不存在")
    i += 1
    if i == 4:
        i = 0
