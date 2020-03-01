#!/usr/bin/env python

from PIL import Image, ImageDraw

img_path = input("image? >>> ")

image_obj = Image.open(img_path)

width, height = image_obj.size

drawer = ImageDraw.Draw(image_obj)

strokeWidth = 5

color = [(255, 0, 0), (0, 0, 255)]

while True:
    bbox = input(
        r"input %d %f %f %f %f to mark a darknet-like boundary box. press enter to show the result\n")

    bbox = bbox.strip()

    if bbox == '':
        break

    items = bbox.split(' ')

    assert(len(items) == 5)

    cat = int(items[0])

    centerx, centery, bboxw, bboxh = [float(x) for x in items[1:]]

    x1, y1, x2, y2 = centerx - bboxw / 2, centery - \
        bboxh / 2, centerx + bboxw / 2, centery + bboxh / 2

    drawer.rectangle([(x1 * width, y1 * height),
                      (x2 * width, y2 * height)], outline=color[cat], width=strokeWidth)

image_obj.show()
