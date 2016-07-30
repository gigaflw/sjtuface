#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by BigFlower at 16/7/30

from core import FaceRecognitionSys
import argparse

if __name__ == '__main__':
    f = FaceRecognitionSys("testing")
    parser = argparse.ArgumentParser(description="SJTU face recognition system.")
    parser.add_argument("-i", action="store_true",
                        help="Initialize the database on server according to images in 'database' directory")
    parser.add_argument("-f", metavar="path_to_image", help="The path to the image you want to identify.")
    a = parser.parse_args()
    if a.i:
        f.initialize()
    if a.f:
        f.identify_new_face(a.f)
