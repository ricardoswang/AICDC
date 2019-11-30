#!/usr/bin/env python

import numpy
import kmeans as km
import imp

stuff = imp.stuff

bboxes = []

for cati in range(4):
    for tok in stuff[cati]:
        bboxes.append(numpy.array([i for i in tok[1][2:]]))
l = [list(l) for l in km.kmeans(numpy.array(bboxes), 9)]

for i in l:
    print("%d,%d" % (int(i[0] * 416), int(i[1] * 416)), end=',  ')
