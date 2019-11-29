#!/usr/bin/env python
import os

rvoc_txt = input("Input the txt file that matches those images >>> ")
os.system('cat HEADER %s > imp.py' % rvoc_txt)
