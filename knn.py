# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 18:17:10 2017

@author: zhengzhang
"""
import sample
import random
import util
    
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

    k_nearest_neighbours = result[:k]

    # Assigning a label to the new point based on the k neighbours
    label_votes = { l:0 for l in util.LABELS }
    for x in k_nearest_neighbours:
        label_votes[ x.getLabel() ] += 1
    max_label = sorted(label_votes, key = label_votes.get, reverse = True)[0]
    
    print(p)
    p.setLabel(max_label)
    print(p)
    
if __name__ == "__main__":
    
    random.seed(0)
    n = 100
    K = 3
    
    data = util.genDistribution(n=10)
    for d in data:
        d.setLabel(random.choice(util.LABELS))

    print("before....")
    util.plot_data(data)
    
    new_pt = sample.Sample('', [0.2, 0.3], '')
    knn(new_pt, data, K)
    
    data.append(new_pt)
    print("\nafter....")
    util.plot_data(data)   
