#!/usr/bin/env python
import path_checker as pac
from PIL import Image
folder_name = input(
    'Tell me the folder name that contains txt files? >>> ')

txt_names = pac.get_files(folder_name, extension='.txt')

image_path = input('Tell me the folder name that contains jpg files? >>> ')

result_string = []

for txt_name in txt_names:
    jpg_path = './%s/%s' % (image_path, txt_name.replace('.txt', ''))
    txt_path = './%s/%s' % (folder_name, txt_name)
    w, h = Image.open(jpg_path).size

    with open(txt_path, 'r') as tf:
        lines = tf.readlines()
        for line in lines:
            tokens = line.split(' ')
            print(tokens)
            assert(len(tokens) == 7)
            x1, y1, x2, y2 = int(tokens[0]) / w, int(tokens[1]) / \
                h, int(tokens[2]) / w, int(tokens[3]) / h
            result_string.append('%s, %f, %f, %f, %f' % (
                txt_name.replace('.jpg.txt', ''), x1, y1, x2, y2))

output_where = input('Where would you like to put the result? >>> ')
with open(output_where, 'w') as wf:
    wf.write('\n'.join(result_string))

print('done')
