#!/usr/bin/env python

import IR
import statistics

from PIL import Image

stuff_buf = IR.stuff

r_vs = []
g_vs = []
b_vs = []

for cat in stuff_buf:
    for img_entry in cat:
        print(img_entry)

        file_path = img_entry[0]
        assert(type(file_path) == str)

        im = Image.open(file_path)
        width, height = im.size

        for wi in range(width):
            for hi in range(height):
                v = im.getpixel((wi, hi))
                assert(len(v) == 3)

                r_vs.append(v[0])
                g_vs.append(v[1])
                b_vs.append(v[2])

r_mean = statistics.mean(r_vs)
g_mean = statistics.mean(g_vs)
b_mean = statistics.mean(b_vs)

r_variance = statistics.variance(r_vs)
g_variance = statistics.variance(g_vs)
b_variance = statistics.variance(b_vs)

print("""
(つД`)ノ

===== MEAN ===== 
R: %.8f
G: %.8f
B: %.8f

=== VARIANCE ===
R: %.8f
G: %.8f
B: %.8f

EOF
""" % (r_mean, g_mean, b_mean, r_variance, g_variance, b_variance))
