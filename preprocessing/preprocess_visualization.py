#Eitan Spivak
#311391866

import os
import random
from PIL import Image
import matplotlib.pyplot as plt

orig_hr_dir = "DIV2K_valid_HR"
cropped_hr_dir = "DIV2K_valid_HR_cropped"
lr_dir = "DIV2K_valid_LR_bicubic_X4"

filenames = [f for f in os.listdir(orig_hr_dir) if f.endswith('.png')]
sample_files = random.sample(filenames, 5)

for fname in sample_files:
    orig_path = os.path.join(orig_hr_dir, fname)
    cropped_path = os.path.join(cropped_hr_dir, fname)
    lr_path = os.path.join(lr_dir, fname)
    orig_img = Image.open(orig_path)
    cropped_img = Image.open(cropped_path)
    lr_img = Image.open(lr_path)
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1)
    plt.imshow(orig_img)
    plt.title("Original HR")
    plt.axis("off")
    plt.subplot(1, 3, 2)
    plt.imshow(cropped_img)
    plt.title("Cropped/Resized HR")
    plt.axis("off")
    plt.subplot(1, 3, 3)
    plt.imshow(lr_img)
    plt.title("Downsampled LR (×4)")
    plt.axis("off")
    plt.suptitle(fname)
    plt.tight_layout()
    plt.show()
