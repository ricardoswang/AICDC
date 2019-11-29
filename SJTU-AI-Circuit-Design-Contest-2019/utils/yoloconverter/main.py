#!/usr/bin/env python

import txt_manager
import imp
import path_checker

path = input("Input the folder name you wanna process >>> ")

images_name = path_checker.get_images(path)

print("Traversed folder ./%s, gotta %d image(s)." % (path, len(images_name)))

if images_name == []:
    exit(-1)

stuff = imp.stuff

txt_paths = []

for cati in range(4):
    for item in stuff[cati]:
        assert(len(item) == 2)
        abs_path = item[0]
        assert(type(abs_path) == str)
        bbox = item[1]
        assert(type(bbox) == list)
        assert(len(bbox) == 4)

        filename = abs_path.split('/')[-1]

        for rel_path in images_name:
            if filename in rel_path:
                txtpath = rel_path.replace('.jpg', '.txt')
                txt_paths.append(txtpath)
                with open(txtpath, 'w') as tf:
                    tf.write("%d %.6f %.6f %.6f %.6f" %
                             (cati, bbox[0], bbox[1], bbox[2], bbox[3]))
                break

txt_index_path = input("Where would you like to put your index txt file? >>> ")

with open(txt_index_path, 'w') as tif:
    tif.write('\n'.join(txt_paths))

print("done")
