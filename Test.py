import Fighting
import port8111


while True:
    map_size = port8111.get_size()
    print(f"地图尺寸：{map_size}m")
    Vy, Hm, throttle, IAS, airbrake = port8111.getState()
    print(f"空速：{IAS} 高度：{Hm} 爬升率：{Vy} 节流阀：{throttle}")
    keyboard_event = Fighting.enemy_airfield(map_size, airbrake)


