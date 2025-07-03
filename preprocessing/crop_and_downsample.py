#Eitan Spivak
#311391866

import os
from PIL import Image

# ==== Configuration ====
base_dir = "./"  # or your data root directory
folders = ["DIV2K_train_HR", "DIV2K_valid_HR"]
target_size = (2040, 1356)  # (width, height)
lr_scale = 4

def center_crop(img, target_w, target_h):
    w, h = img.size
    left = (w - target_w) // 2
    upper = (h - target_h) // 2
    return img.crop((left, upper, left + target_w, upper + target_h))

for folder in folders:
    in_path = os.path.join(base_dir, folder)
    hr_out_folder = folder + "_cropped"
    hr_out_path = os.path.join(base_dir, hr_out_folder)
    lr_out_folder = hr_out_folder.replace("HR", "LR_bicubic_X4")
    lr_out_path = os.path.join(base_dir, lr_out_folder)
    os.makedirs(hr_out_path, exist_ok=True)
    os.makedirs(lr_out_path, exist_ok=True)

    print(f"Processing {folder} → {hr_out_folder} / {lr_out_folder}")

    for filename in os.listdir(in_path):
        if not filename.lower().endswith(".png"):
            continue
        img_path = os.path.join(in_path, filename)
        with Image.open(img_path) as img:
            img = img.convert("RGB")
            w, h = img.size
            # Crop or resize to target size
            if w >= target_size[0] and h >= target_size[1]:
                hr_cropped = center_crop(img, *target_size)
            else:
                hr_cropped = img.resize(target_size, Image.BICUBIC)
            # Save cropped HR image
            hr_cropped.save(os.path.join(hr_out_path, filename))
            # Make dimensions divisible by scale
            w_c, h_c = hr_cropped.size
            w_c, h_c = w_c - w_c % lr_scale, h_c - h_c % lr_scale
            hr_cropped = hr_cropped.crop((0, 0, w_c, h_c))
            # Downsample LR
            lr_img = hr_cropped.resize((w_c // lr_scale, h_c // lr_scale), Image.BICUBIC)
            lr_img.save(os.path.join(lr_out_path, filename))
    print(f"Done {folder}.\n")
