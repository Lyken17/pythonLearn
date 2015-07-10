#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image, ImageFilter
import os, sys
import os.path

pic_type = {".png",".jpeg",".jpg"}

#rootdir = "/Users/admin/pylearn/pic"
rootdir = "/Users/admin/Desktop/tmp"

for infile in os.listdir(rootdir):
    infile = os.path.join(rootdir, infile)
    # print infile
    # print rootdir
    # print 'This is infile', infile
    f, e = os.path.splitext(os.path.realpath(infile))
    # print f
    # print e
    if e.lower() in pic_type:
        #print infile
        #print os.path.realpath(infile)
        #print "F = " + f
        #print "E = " + e

        file_path = os.path.realpath(infile)

        print file_path

        im = Image.open(file_path)
        w, h = im.size
        im.thumbnail((w//2, h//2))
        im.save(f + ' thumbnail' + ".png","png")

        print "This picture :'%s' has been thumnailed by ZLG" % file_path
