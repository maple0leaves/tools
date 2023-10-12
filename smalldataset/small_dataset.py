import os
import random
from pathlib import Path
import shutil

def delete_labels_by_ratio(folder_path, deletion_ratio):
    # 获取文件夹中的所有图片文件
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # 计算要删除的图片数量
    num_images_to_delete = int(len(image_files) * deletion_ratio)

    # 随机选择要删除的图片
    images_to_delete = random.sample(image_files, num_images_to_delete)

    # 删除选定的图片
    for image in images_to_delete:
        image_path = os.path.join(folder_path, image)
        os.remove(image_path)

    print(f"{num_images_to_delete} images deleted out of {len(image_files)}.")

# 使用示例：删除50%的图片
# delete_images_by_ratio(r"F:\ZZLcode\hand_glove(small)\labels\train", 0.5)


def makesmall(imgpath,labelpath):
    labelfiles = [f for f in os.listdir(labelpath) if os.path.isfile(os.path.join(labelpath, f))]
    labelname = [Path(x).stem for x in labelfiles]
    imgfiles = [f for f in os.listdir(imgpath) if os.path.isfile(os.path.join(imgpath, f))]
    for img in imgfiles:
        name,_ = os.path.splitext(img)
        if name not in labelname:
            image_path = os.path.join(imgpath, img)
            os.remove(image_path)
        print("making.......")
        
if __name__ =="__main__":

    files =['test', 'train', 'trainval', 'val']
    # deletion_ratio : how many do you want to delete ,save 1- deletion_ratio
    deletion_ratio = 0.5
    # imgpath is images path
    # labelpath is labels path
    # depend on deletion_ratio remove label in labelpath and use label
    # file name save img in imgpath .
    for file in files:
        imgpath = r'F:\ZZLcode\hand_glove_last\images\\'+file
        labelpath = r'F:\ZZLcode\hand_glove_last\labels\\'+file
        # labelpath could not change
        delete_labels_by_ratio(labelpath, 0.5)
        makesmall(imgpath=imgpath, labelpath=labelpath)
