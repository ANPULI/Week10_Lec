# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 17:52:09 2016

@author: zhengzhang
"""

def knn(p, data, k):
    # Calculating the distances b/w p & every pt. in data
    distances = {}
    for d in data:
        if d.distance(p) not in distances.keys():
            distances[ d.distance(p) ] = [ d ]
        else:
            distances[ d.distance(p) ].append(d)

    # Sorting the k nearest neighbours
    result = []        
    for key in sorted(distances.keys()):
        result.extend( distances[key] )
    return result[:k]
