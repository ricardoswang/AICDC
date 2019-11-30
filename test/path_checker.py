#!/usr/bin/env python

import os


def get_files(folder_name, extension=None):

    paths = []

    path = os.getcwd() + "/%s/" % folder_name
    for _, _, files in os.walk(path):
        # print(filename)
        for filename in files:
            if extension == None:
                path.append(filename)
            else:
                if filename.endswith(extension):
                    paths.append(filename)

    return paths
