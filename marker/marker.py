#!/usr/bin/env python

from math import sqrt
from random import randint
from PIL import Image, ImageDraw, ImageFont

img_path = input("image? >>> ").strip()

image_obj = Image.open(img_path)

width, height = image_obj.size

drawer = ImageDraw.Draw(image_obj)

__strokeWidth = 5
__textSizeRatio = 66
__textMarginRatio = 1.3
__markTextSize = int(sqrt(width * height)) // __textSizeRatio

try:
    __markFont = ImageFont.truetype("./DIN-Bold.otf", __markTextSize)
except:
    __markFont = ImageFont.truetype("Times New Roman", __markTextSize)

color = []

counter = 0

while True:
    bbox = input(
        r"input %d %f %f %f %f to mark a darknet-like boundary box. press enter to show the result" + '\n')

    bbox = bbox.strip()

    if bbox == '':
        break

    items = bbox.split(' ')

    if not len(items) == 5:
        continue

    cat = int(items[0])

    while len(color) <= cat:
        color.append((randint(0, 255), randint(0, 255), randint(0, 255)))

    centerx, centery, bboxw, bboxh = [float(x) for x in items[1:]]

    x1, y1, x2, y2 = centerx - bboxw / 2, centery - \
        bboxh / 2, centerx + bboxw / 2, centery + bboxh / 2

    drawer.rectangle([(x1 * width, y1 * height),
                      (x2 * width, y2 * height)], outline=color[cat], width=__strokeWidth)

    drawer.text((x1 * width, y1 * height - __markTextSize * __textMarginRatio), "#%d, Type %d" % (counter, cat), fill=color[cat],
                font=__markFont, align='left')

    counter += 1

image_obj.show()
