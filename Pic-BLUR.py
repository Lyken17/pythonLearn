#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageFilter

# 打开一个jpg图像文件，注意路径要改成你自己的:
im = Image.open('k123.jpg')

im2 = im.filter(ImageFilter.BLUR)
im2.save('thumbnail.jpg', 'jpeg')
