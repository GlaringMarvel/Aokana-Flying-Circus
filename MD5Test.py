import hashlib

def calculate_md5(file_path):
    with open(file_path, 'rb') as file:
        md5_hash = hashlib.md5()
        while True:
            data = file.read(4096)  # 以块的方式读取文件
            if not data:
                break
            md5_hash.update(data)
    return md5_hash.hexdigest()

# 示例用法
file_path = 'map/BigCity.img'
md5_value = calculate_md5(file_path)
print("MD5:", md5_value)