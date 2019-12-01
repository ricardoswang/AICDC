#!/usr/bin/env python

import json

json_path = input("Where's your main json file? >>> ")

jf = open(json_path, 'r')
data = json.load(jf)

only_one = input(
    "For each image, only one annotation is permitted, right? >>> [y/n]")

if only_one == 'y':
    only_one = True
else:
    only_one = False

images = {}
for img in data['images']:
    images.update({
        img['id']: {
            'name': img['filename'],
            'size': (img['width'], img['height']),
            'annotation': []
        }
    })

for anno in data['annotations']:
    bbox = anno['bbox']
    iid = anno['image_id']

    if only_one:
        if anno['image_id']['annotation'] != []:
            continue

    cat = anno['category_id']

    image_pps = images[iid]
    tw, th = image_pps['size']
    x1, y1, w, h = bbox[0], bbox[1], bbox[2], bbox[3]
    cx, cy = x1 + w / 2, y1 + h / 2

    images[iid]['annotations'].append(
        [cat, [cx / tw, cy / th, w / tw, h / th]])

export_path = input("Which folder would you like to put txt files? >>> ")

if not export_path.endswith('/'):
    export_path += '/'
for ids, image in image.items():
    txt_fn = image['name'].replace('.jpg', '.txt')
    with open(export_path + txt_fn, 'w') as f:
        for anno in image['annotation']:
            f.write('%d %f %f %f %f' %
                    (anno[0], anno[1][0], anno[1][1], anno[1][2], anno[1][3]))
