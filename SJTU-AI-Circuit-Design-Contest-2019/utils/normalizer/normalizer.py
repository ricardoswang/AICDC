#!/usr/bin/env python

import json

with open(input("Where's your result json file? >>>"), 'r') as f:
    result_data = json.load(f)

with open(input("Where's your origin json file? >>>"), 'r') as f:
    origin_data = json.load(f)

path_mapping = {}

for img in origin_data["images"]:
    path_mapping[img['id']] = (img['width'], img['height'])

for result in result_data:
    pass

# {"image_id": 292,
#  "category_id": 0,
#     "bbox": [-4.66, -93.44, 10.72, 24.06],
#     "score": 0.01}
