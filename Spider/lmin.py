#!/usr/bin/python
#-*- coding: utf-8 -*-
#encoding=utf-8

import urllib2
import urllib
import os
from BeautifulSoup import BeautifulSoup

def getAllImageLink():
    for pages in xrange(10):
        html = urllib2.urlopen('http://file.lmin.me/fcl/result.html').read()
        soup = BeautifulSoup(html)

        liResult = soup.findAll('div')

        for li in liResult[:10]:
            print [tmp.text for tmp in li.findAll('span')],
            print
            #imageEntityArray = li.findAll('img')
            #for image in imageEntityArray:
                #link = image.get('data-src')
                #imageName = image.get('data-id')
                #filesavepath = '/Users/admin/Pictures/test/Temp/%s.jpg' % imageName
                #urllib.urlretrieve(link,filesavepath)
                #print filesavepath

if __name__ == '__main__':
    getAllImageLink()


<span>(*)</span>
