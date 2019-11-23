#!/usr/bin/env python

import os
import cv2
import sys
import json
import random
import train_list

from PIL import Image

stuff_buf = train_list.stuff

total_count = sum([len(i) for i in stuff_buf])

id_pool = list(range(total_count))

random.shuffle(id_pool)

assert(len(stuff_buf) == 4)


def __get_annotation__(self, mask, image=None):

    _, contours, _ = cv2.findContours(
        mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    segmentation = []
    for contour in contours:
        # Valid polygons have >= 6 coordinates (3 points)
        if contour.size >= 6:
            segmentation.append(contour.flatten().tolist())
    RLEs = cocomask.frPyObjects(segmentation, mask.shape[0], mask.shape[1])
    RLE = cocomask.merge(RLEs)
    # RLE = cocomask.encode(np.asfortranarray(mask))
    area = cocomask.area(RLE)
    [x, y, w, h] = cv2.boundingRect(mask)

    if image is not None:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        cv2.drawContours(image, contours, -1, (0, 255, 0), 1)
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow("", image)
        cv2.waitKey(1)

    return segmentation, [x, y, w, h], area


coco_instance = {}

coco_instance["info"] = {"year": 2019,
                         "version": "1.0",
                         "description": "Attempting to convert reduced VOC to COCO format.",
                         "contributor": "Wang YM, Yu XQ, Du PD",
                         "url": "http://github.com/ricardoswang",
                         "date_created": "2019/11/23"
                         }
coco_instance["licenses"] = [{"id": 1,
                              "name": "copyright (c) 2019 contributors all rights reserved",
                              "url": "N/A"
                              },
                             {"id": 2,
                              "name": "copyleft, under public domain.",
                              "url": "N/A"
                              }]

coco_instance["categories"] = [
    {"supercategory": "Aeroplane", "id": 1, "name": "Aeroplane"},
    {"supercategory": "Car", "id": 2, "name": "Car"},
    {"supercategory": "Sofa", "id": 3, "name": "Sofa"},
    {"supercategory": "TV Monitor", "id": 4, "name": "TV Monitor"}
]

counter = 0

coco_instance["annotations"] = []
coco_instance["images"] = []

for index in range(4):
    for item in stuff_buf[index]:
        print(item)

        file_path = item[0]
        assert(type(file_path) == str)

        straint_box = item[1]
        assert(type(straint_box) == list and len(straint_box) == 4)

        im = Image.open(file_path)
        width, height = im.size

        coco_instance["images"].append({
            "license": 2,
            "file_name": file_path,
            "coco_url": "",
            "height": height,
            "width": width,
            "date_captured": "",
            "flickr_url": "",
            "id": id_pool[counter]
        })

        img = im.convert('RGB')
        mask = im.convert('L')

        # segmentation, bbox, area = self.__get_annotation__(mask, im)

        x, y, w, h = straint_box[0] * width, straint_box[1] * \
            height, (straint_box[2] - straint_box[0]) * \
            width, (straint_box[3] - straint_box[1]) * height

        coco_instance["annotations"].append({
            "segmentation": []],
            "area": 42,
            "iscrowd": 0,
            "image_id": id_pool[counter],
            "bbox": [x, y, w, h],
            "category_id": index + 1,
            "id": counter
        })
        counter += 1

with open('./' + input("input your expecting json output path >>> ") + '.json', 'w') as f:
    f.write(json.dumps(coco_instance))

print("Bye")
