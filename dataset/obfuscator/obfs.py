#!/usr/bin/env python

import os
import json
import pathlib
from PIL import Image, ImageEnhance


def dir_valid(dirr: str):
    if not pathlib.Path(dirr).is_dir():
        print("Cannot found path %s." % dirr)
        exit(-1)


image_folder = input("original image folder? >>> ")
dir_valid(image_folder)

label_folder = input("original label folder? >>> ")
dir_valid(label_folder)

obfs_image_folder = input("obfuscated image folder? >>> ")
dir_valid(obfs_image_folder)

obfs_label_folder = input("obfuscated label folder? >>> ")
dir_valid(obfs_label_folder)

sat_factor = float(input("saturation adjust factor? (float, 0 - 1) >>> "))
exp_factor = float(input("exposure adjust factor? (float, 0 - 1) >>> "))
ct_factor = float(
    input("contrast adjust factor? (float, 0 - 1) >>> "))

obfs_image_paths = []

# 饱和/欠饱和、过曝/欠曝、高对比/低对比

# origin
# over_sat
# under_sat
# over_exp
# under_exp
# over_contrast
# under_contrast

jpeg_compression_quality = int(
    input("jpeg compression quality? (the higher the better) >>> "))

for root, _, imgs in os.walk(image_folder):
    for img_file in imgs:
        # print(img_file)
        original_image = Image.open(os.path.join(root, img_file))

        over_sat_image = ImageEnhance.Color(
            original_image).enhance(1.0 + sat_factor)
        under_sat_image = ImageEnhance.Color(
            original_image).enhance(1.0 - sat_factor)

        over_exp_image = ImageEnhance.Brightness(
            original_image).enhance(1.0 + exp_factor)
        under_exp_image = ImageEnhance.Brightness(
            original_image).enhance(1.0 - exp_factor)

        over_ct_image = ImageEnhance.Contrast(
            original_image).enhance(1.0 + ct_factor)
        under_ct_image = ImageEnhance.Contrast(
            original_image).enhance(1.0 - ct_factor)

        original_image.save(os.path.join(
            obfs_image_folder, 'origin_' + img_file), quality=jpeg_compression_quality)
        over_sat_image.save(os.path.join(
            obfs_image_folder, 'over_sat_' + img_file), quality=jpeg_compression_quality)
        under_sat_image.save(os.path.join(
            obfs_image_folder, 'under_sat_' + img_file), quality=jpeg_compression_quality)
        over_exp_image.save(os.path.join(
            obfs_image_folder, 'over_exp_' + img_file), quality=jpeg_compression_quality)
        under_exp_image.save(os.path.join(
            obfs_image_folder, 'under_exp_' + img_file), quality=jpeg_compression_quality)
        over_ct_image.save(os.path.join(
            obfs_image_folder, 'over_ct_' + img_file), quality=jpeg_compression_quality)
        under_ct_image.save(os.path.join(
            obfs_image_folder, 'under_ct_' + img_file), quality=jpeg_compression_quality)

for root, _, labels in os.walk(label_folder):
    for label_file in labels:
        # print(label_file)

        with open(os.path.join(root, label_file), 'r') as org_f:
            contents = org_f.read()

        with open(os.path.join(obfs_label_folder, 'origin_' + label_file), 'w') as label_f:
            label_f.write(contents)

        with open(os.path.join(obfs_label_folder, 'over_sat_' + label_file), 'w') as label_f:
            label_f.write(contents)

        with open(os.path.join(obfs_label_folder, 'under_sat_' + label_file), 'w') as label_f:
            label_f.write(contents)

        with open(os.path.join(obfs_label_folder, 'over_exp_' + label_file), 'w') as label_f:
            label_f.write(contents)

        with open(os.path.join(obfs_label_folder, 'under_exp_' + label_file), 'w') as label_f:
            label_f.write(contents)

        with open(os.path.join(obfs_label_folder, 'over_ct_' + label_file), 'w') as label_f:
            label_f.write(contents)

        with open(os.path.join(obfs_label_folder, 'under_ct_' + label_file), 'w') as label_f:
            label_f.write(contents)

print("Bye")
