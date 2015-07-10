#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter
import os, sys
import os.path
from shutil import copy


pic_type = {".png",".jpeg",".jpg"}
gif_type = {".gif"}


copy_path = "/Users/admin/Pictures/test/Temp"

rootdir = "/Users/admin/Pictures/test/Picture"

for root, dirs, files in os.walk(rootdir):
    # print infile
    # print rootdir
    # print 'This is infile', infile
    #f, e = os.path.splitext(os.path.realpath(infile))
    # print f
    # print e
    print "============================================"
    print "root is ", root
    for i in files:
        file_path = os.path.join(root, i)
        print "files is ", i
        print "path is ", file_path
        #tmp_path = os.path.join(copy_path, i)
        tmp_path = copy_path + '/GIF/' + i
        print "tmp_path is ", tmp_path
        copy(file_path, tmp_path)
        #copy(file_path)

    #if e.lower() in pic_type:
        #print infile
        #print os.path.realpath(infile)
        #print "F = " + f
        #print "E = " + e

        #file_path = os.path.realpath(infile)

        #im = Image.open(file_path)
        #w, h = im.size
        #im.thumbnail((w//2, h//2))
        #im.save(f + ' thumbnail' + ".jpeg","jpeg")
        #print "This picture :'%s' has been thumnailed by ZLG" % file_path
