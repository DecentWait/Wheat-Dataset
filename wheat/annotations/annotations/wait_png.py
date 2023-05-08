from PIL import Image
import os

# 指定文件夹路径
folder_path = "trimaps"

# 循环处理文件夹中的每个文件
for filename in os.listdir(folder_path):
    if filename.endswith(".png"):
        # 打开图片
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path)
        
        # 将图片转换为黑白二值图像
        img = img.convert("1")
        
        # 保存为新文件
        new_filename = os.path.splitext(filename)[0] + ".png"
        new_img_path = os.path.join(folder_path, new_filename)
        img.save(new_img_path)
