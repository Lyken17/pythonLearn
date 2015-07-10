#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from sklearn import *
from sklearn.neighbors import KDTree
import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
kdt = KDTree(X, leaf_size=30, metric='euclidean')
print kdt.query(X, k=2, return_distance=False) 

print "Hi"