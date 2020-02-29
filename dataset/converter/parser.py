#!/usr/bin/env python

import os
import json

filename = input("json? >>> ")

i_wrapping_path = input("image path prefix? >>> ")
l_wrapping_path = input("label path prefix? >>> ")

print("""
Be sure that your image path prefix and label path prefix matches exactly as decalred in https://github.com/ultralytics/yolov3/wiki/Train-Custom-Data.
""")

with open(filename, 'r') as load_f:
    obj = json.load(load_f)

image_map = {}
cat_map = {}
image_list = []

for image_obj in obj['images']:
    image_map.update({
        image_obj['id']: (image_obj['width'],
                          image_obj['height'], image_obj['file_name'])
    })

for cat_obj in obj['categories']:
    cat_map.update({
        cat_obj['id']: cat_obj['name']
    })

for anno_obj in obj['annotations']:
    x1, y1, x2, y2 = anno_obj['bbox']

    center_x, center_y, rect_w, rect_h = (
        x1 + x2) / 2, (y1 + y2) / 2, (x2 - x1), (y2 - y1)

    width, height, image_name = anno_obj['image_id']

    label_name = os.path.join(
        l_wrapping_path, image_name.replace('.jpg', '.txt'))

    with open(label_name, 'w') as label_f:
        label_f.write("%d %.6f %.6f %.6f %.6f" % (
            anno_obj['category_id'], center_x / width, center_y / height, rect_w / width. rect_h / height))

    image_list.append(os.path.join(i_wrapping_path, image_name))

print("parsing over!")

names_path = input("where to place your .names file? >>> ")

with open(names_path, 'w') as names_f:

    cats = []
    for _, v in sorted(cat_map.items(), key=lambda v: v[0]):
        cats.append(v)

    names_f.write('\n'.join(cats))

txt_path = input("where to place your .txt file? >>> ")

with open(txt_path, 'w') as txt_f:

    txt_path.write('\n'.join(image_list))

print("Bye")
