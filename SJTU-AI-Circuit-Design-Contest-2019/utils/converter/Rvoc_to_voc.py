#!/usr/bin/env python

import os
import cv2
import sys
import json
import random
import IR

from PIL import Image
from xml.etree.ElementTree import Element

stuff_buf = IR.stuff

total_count = sum([len(i) for i in stuff_buf])

assert(len(stuff_buf) == 4)

cat_name = ["Aeroplane", "Car", "Sofa", "TV Monitor"]

for index in range(4):
    for item in stuff_buf[index]:
        print(item)

        file_path = item[0]
        assert(type(file_path) == str)

        straint_box = item[1]
        assert(type(straint_box) == list and len(straint_box) == 4)

        im = Image.open(file_path)
        width, height = im.size

        # segmentation, bbox, area = self.__get_annotation__(mask, im)

        x1, y1, x2, y2 = straint_box[0] * width, straint_box[1] * \
            height, (straint_box[2]) * \
            width, (straint_box[3]) * height

        # coco_instance["annotations"].append({
        # "segmentation": [],
        # "area": 42,
        # "iscrowd": 0,
        # "image_id": id_pool[counter],
        # "bbox": [x, y, w, h],
        # "category_id": index + 1,
        # "id": counter
        # })

        file_name = file_path.split('/')[-1]
        xml_content = """
<?xml version="1.0" encoding="utf-8"?>
<annotation>
    <folder>AICDC2019</folder>
    <filename>%s</filename>
    <size>
        <width>%d</width>
        <height>%d</height>
        <depth>3</depth>
    </size>
    <object>
        <name>%s</name>
        <bndbox>
            <xmin>%d</xmin>
            <xmax>%d</xmax>
            <ymin>%d</ymin>
            <ymax>%d</ymax>
        </bndbox>
        <truncated>0</truncated>
        <difficult>0</difficult>
    </object>
    <segmented>0</segmented>
</annotation>
        """ % (file_name, width, height, cat_name[index], int(x1), int(y1), int(x2), int(y2))

        with open(file_path.replace(file_name, '') + '/xml/' + file_name + '.xml', 'w') as f:
            f.write(xml_content)
