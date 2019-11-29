#!/usr/bin/env python

import os


def get_images(folder_name='images'):

    paths = []

    path = os.getcwd() + "/%s/" % folder_name
    for _, _, files in os.walk(path):
        for filename in files:
            paths.append('./%s/%s' % (folder_name, filename))

    return paths
