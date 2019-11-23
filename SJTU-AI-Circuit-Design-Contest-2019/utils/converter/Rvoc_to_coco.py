#!/usr/bin/env python

import os
import sys
import PIL
import json
import random
import train_list

stuff_buf = train_list.stuff

categories = [
    "Aeroplane",
    "Car",
    "Sofa",
    "TV Monitor"
]

total_count = sum([len(i) for i in stuff_buf])

id_pool = list(range(total_count))

random.shuffle(id_pool)


assert(len(stuff_buf) == 4)

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
                              }]


for index in range(4):
    for item in stuff_buf[index]:
        print(item)

        file_path = item[0]
        assert(type(file_path) == str)

        straint_box = item[1]
        assert(type(straint_box) == list and len(straint_box) == 4)
