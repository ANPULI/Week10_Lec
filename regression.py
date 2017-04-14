# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 22:48:26 2017

@author: zhengzhang
"""
import matplotlib.pyplot as plt
import sample
import random

def genDistribution(xMean, xSD, yMean, ySD, n, namePrefix):
    samples = []
    for s in range(n):
        x = random.gauss(xMean, xSD)
        y = random.gauss(yMean, ySD)
        samples.append(sample.Sample(namePrefix+str(s), [x, y]))
    return samples
    
def make_data(n):
    linear_data = [ sample.Sample('', [x/(float(SCALE)), x/(float(SCALE))], '') for x in range(n) ]
    mean = 0
    std = DEV * SCALE
    
    noise = genDistribution(mean, std, mean, std, n, '')
    data = [linear_data[i] + noise[i] for i in range(n)]
    return data
    
if __name__ == "__main__":

    # Consts for x/y scale, deviation limit, number of samples, choice of k, class names
    # ALTER THESE PARAMETERS TO CREATE DIFFERENT TEST SETS
    SCALE = 10
    DEV = 0.03
    SAMPLES = 100

    # Generating random data
    data = make_data(SAMPLES)
    train_data = data[:80]
    test_data = data[80:]

    # Plotting the randomly generated data
    d_x = [ d.getFeatures()[0] for d in train_data]
    d_y = [ d.getFeatures()[1] for d in train_data]
#    plt.scatter(d_x, d_y)
    
    w = 0.5
    num_iter = 20
    steps = 0
    learning_rate = 0.01
    n = len(train_data)
#    for iter in range(iter_num):
    margin = 0.01
    while True:
        
        pred_y = [w*x for x in d_x]
        
        plt.scatter(d_x, d_y)
        plt.plot(d_x, pred_y, 'r')
        plt.show()
        
        error = 0
        for i in range(n):
            error += (pred_y[i] - d_y[i]) ** 2
        error /= 2*n
        print("error is %0.2f" % error)
        if error <= margin or steps > num_iter:
            break
        steps += 1
        
        grad = [(pred_y[i] - d_y[i]) * d_x[i] for i in range(n)]
        grad = sum(grad)/n
        w -= learning_rate * grad
#        if input("cont? (y/n)") == 'n':
#            break

