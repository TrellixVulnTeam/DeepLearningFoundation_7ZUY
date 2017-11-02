#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nonlining
#
# Created:     02/11/2017
# Copyright:
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
from miniflow import *

def main():
    X_data = [[0.,0.], [1.,0.] ,[0.,1.] ,[1.,1.]]

    X_data = np.array(X_data)

    y_label = [[0., 0., 0., 1.]]
    y_label = np.array(y_label)

    W_layer1 = np.random.randn(2,1)
    b_layer1 = np.random.randn(1)

    X, y = Input(), Input()
    W1, b1 = Input(), Input()

    L1 = Linear(X, W1, b1)
    S1 = Sigmoid(L1)

    cost = MSE(y, S1)

    feed_dict = {
        X: X_data,
        y: y_label,
        W1: W_layer1,
        b1: b_layer1
    }

    graph = topological_sort(feed_dict)

    trainables = [W1, b1]

    epochs = 100
    learning_rate=0.1
    for i in range(epochs):

        forward_and_backward(graph)
        for t in trainables:
            partial = t.gradients[t]
            t.value -= learning_rate * partial
        print "MSE",graph[-1].value

    print W1.value
    print b1.value

if __name__ == '__main__':
    main()
