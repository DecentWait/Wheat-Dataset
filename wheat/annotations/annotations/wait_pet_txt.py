import glob
import os

# 目标文件夹中要读取的文件类型
file_type = "*.png"

# 目标文件夹的路径
folder_path = "trimaps"

# 用于存储文件名的列表
file_names = []

# 遍历目标文件夹中的所有指定类型的文件
for filename in glob.glob(os.path.join(folder_path, file_type)):
    # 提取文件名并添加到列表中
    file_names.append(os.path.splitext(os.path.basename(filename))[0])

# 将文件名写入 trainval.txt 文件
with open("test.txt", "w") as f:
    for file_name in file_names:
        f.write(file_name + "\n")
