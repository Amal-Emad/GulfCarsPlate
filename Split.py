#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 22:30:12 2024

@author: amal-alkraimeen
"""

# =============================================================================
#                        CAR & PLATE DETECTION  
# =============================================================================

'''
1. Copy images and labels into new directories, ensuring the process is correct.
2. Split the data (images and labels) into training and testing sets.
3. Create a main directory structure:
    - MAIN
        - CARS
            - IMAGES
                - TRAIN
                - TEST
            - LABELS
                - TRAIN
                - TEST
        - PLATES
            - IMAGES
                - TRAIN
                - TEST
            - LABELS
                - TRAIN
                - TEST
'''

import os
import shutil
import random

# Paths
src_img_dir = '/home/amal-alkraimeen/Desktop/CAR&PLATE/car&plate_code/samples/trg_sample_img'  
src_lbl_dir = '/home/amal-alkraimeen/Desktop/CAR&PLATE/car&plate_code/samples/trg_sample_label'  
dst_img_dir = '/home/amal-alkraimeen/Desktop/CAR&PLATE/car&plate_code/Copied/dst_image_dir'  
dst_lbl_dir = '/home/amal-alkraimeen/Desktop/CAR&PLATE/car&plate_code/Copied/dst_lbl_dir'  
main_dir = '/home/amal-alkraimeen/Desktop/CAR&PLATE/car&plate_code/Copied'    

# Step 1: Copy images and labels into new directories and ensure the process is correct
os.makedirs(dst_img_dir, exist_ok=True)
os.makedirs(dst_lbl_dir, exist_ok=True)

img_files = os.listdir(src_img_dir)
lbl_files = os.listdir(src_lbl_dir)


lbl_files_dict = {os.path.splitext(lbl_file)[0]: lbl_file for lbl_file in lbl_files}

# Copy images and  labels
for img_file in img_files:
    base_name = os.path.splitext(img_file)[0]
    if base_name in lbl_files_dict:
        src_img_file = os.path.join(src_img_dir, img_file)
        dst_img_file = os.path.join(dst_img_dir, img_file)
        shutil.copy2(src_img_file, dst_img_file)

        src_lbl_file = os.path.join(src_lbl_dir, lbl_files_dict[base_name])
        dst_lbl_file = os.path.join(dst_lbl_dir, lbl_files_dict[base_name])
        shutil.copy2(src_lbl_file, dst_lbl_file)

print(f"Copied {len(os.listdir(dst_img_dir))} images and {len(os.listdir(dst_lbl_dir))} labels.")

# Step 2: Split the data into training and testing (80% train, 20% test)
img_files = os.listdir(dst_img_dir)
lbl_files = os.listdir(dst_lbl_dir)
combined_files = list(zip(img_files, lbl_files))
random.shuffle(combined_files)
split_index = int(0.8 * len(combined_files))
train_files = combined_files[:split_index]
test_files = combined_files[split_index:]

# Step 3: Create the main directory structure
os.makedirs(os.path.join(main_dir, 'cars', 'images', 'train'), exist_ok=True)
os.makedirs(os.path.join(main_dir, 'cars', 'images', 'test'), exist_ok=True)
os.makedirs(os.path.join(main_dir, 'cars', 'labels', 'train'), exist_ok=True)
os.makedirs(os.path.join(main_dir, 'cars', 'labels', 'test'), exist_ok=True)
os.makedirs(os.path.join(main_dir, 'plates', 'images', 'train'), exist_ok=True)
os.makedirs(os.path.join(main_dir, 'plates', 'images', 'test'), exist_ok=True)
os.makedirs(os.path.join(main_dir, 'plates', 'labels', 'train'), exist_ok=True)
os.makedirs(os.path.join(main_dir, 'plates', 'labels', 'test'), exist_ok=True)

# Move files to their  dirs
for img_file, lbl_file in train_files:
    shutil.copy2(os.path.join(dst_img_dir, img_file), os.path.join(main_dir, 'cars', 'images', 'train', img_file))
    shutil.copy2(os.path.join(dst_lbl_dir, lbl_file), os.path.join(main_dir, 'cars', 'labels', 'train', lbl_file))

for img_file, lbl_file in test_files:
    shutil.copy2(os.path.join(dst_img_dir, img_file), os.path.join(main_dir, 'cars', 'images', 'test', img_file))
    shutil.copy2(os.path.join(dst_lbl_dir, lbl_file), os.path.join(main_dir, 'cars', 'labels', 'test', lbl_file))

print("Data has been split into training and testing sets.")
