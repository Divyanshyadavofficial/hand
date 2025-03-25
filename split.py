import os
import shutil
import random


data_dir = "Data"  
train_dir = "Train"
val_dir = "Val"


split_ratio = 0.8  


os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)


for class_name in os.listdir(data_dir):
    class_path = os.path.join(data_dir, class_name)
    if not os.path.isdir(class_path):
        continue

 
    os.makedirs(os.path.join(train_dir, class_name), exist_ok=True)
    os.makedirs(os.path.join(val_dir, class_name), exist_ok=True)

    # Get all files in the class folder
    images = os.listdir(class_path)
    random.shuffle(images)

    # Compute split index
    split_index = int(len(images) * split_ratio)

    # Move files to train and val folders
    for i, image in enumerate(images):
        src_path = os.path.join(class_path, image)
        if i < split_index:
            dst_path = os.path.join(train_dir, class_name, image)
        else:
            dst_path = os.path.join(val_dir, class_name, image)
        shutil.move(src_path, dst_path)

print("Data successfully split into Train and Val folders!")
