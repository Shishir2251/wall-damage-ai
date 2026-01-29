import os
import random
import shutil

# === CONFIG ===
dataset_root = r"C:\Users\Shishir\Projects\wall-damage-ai\training\dataset"
images_path = os.path.join(dataset_root, "images")
labels_path = os.path.join(dataset_root, "labels")

train_ratio = 0.8  # 80% train, 20% val

# === CREATE TRAIN/VAL FOLDERS ===
train_images_path = os.path.join(dataset_root, "images", "train")
val_images_path = os.path.join(dataset_root, "images", "val")
train_labels_path = os.path.join(dataset_root, "labels", "train")
val_labels_path = os.path.join(dataset_root, "labels", "val")

os.makedirs(train_images_path, exist_ok=True)
os.makedirs(val_images_path, exist_ok=True)
os.makedirs(train_labels_path, exist_ok=True)
os.makedirs(val_labels_path, exist_ok=True)

# === LIST ALL IMAGES ===
all_images = [f for f in os.listdir(images_path) if f.endswith(".jpg") or f.endswith(".png")]
random.shuffle(all_images)

# === SPLIT DATA ===
split_idx = int(len(all_images) * train_ratio)
train_images = all_images[:split_idx]
val_images = all_images[split_idx:]

# === MOVE TRAIN FILES ===
for img in train_images:
    shutil.move(os.path.join(images_path, img), os.path.join(train_images_path, img))
    label_file = os.path.splitext(img)[0] + ".txt"
    if os.path.exists(os.path.join(labels_path, label_file)):
        shutil.move(os.path.join(labels_path, label_file), os.path.join(train_labels_path, label_file))

# === MOVE VAL FILES ===
for img in val_images:
    shutil.move(os.path.join(images_path, img), os.path.join(val_images_path, img))
    label_file = os.path.splitext(img)[0] + ".txt"
    if os.path.exists(os.path.join(labels_path, label_file)):
        shutil.move(os.path.join(labels_path, label_file), os.path.join(val_labels_path, label_file))

print("Dataset split complete!")
print(f"Total images: {len(all_images)}")
print(f"Train: {len(train_images)}, Val: {len(val_images)}")
