import Fighting

player_coordinates = (0.380712, 0.76687)
bombing_coordinates = (0.397752, 0.502876)
angle_degrees, distance = Fighting.calculate_heading(player_coordinates, bombing_coordinates)
print(f"角度 {angle_degrees} 距离 {distance}")
x = distance * 13100
print(x)
