#-------------------------------------------------------------------------------
# Name:        Digits
# Purpose:
#
# Author:      jwang32
#
# Created:     07/07/2017
# Copyright:   (c) jwang32 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.utils import shuffle, resample
import numpy as np
from miniflow import *

epochs = 10

def main():
    data = load_digits()
    X_ = data['data']
    y_ = data['target']

    n_features = X_.shape[1]

    n_hidden = 8
    kernel_size = (3,3)

    W_layer1 = np.random.randn(n_hidden, kernel_size[0]*kernel_size[1])
    b_layer1 = np.zeros(n_hidden)
    # test
    print W_layer1[0]
    print X_[0]
    print conv(X_[0], (8,8) ,W_layer1[0], kernel_size) + b_layer1[0]


    W_layer2 = np.random.randn(n_hidden, 1)
    b_layer2 = np.zeros(1)

    X, y = Input(), Input()
    W1, b1 = Input(), Input()
    W2, b2 = Input(), Input()



if __name__ == '__main__':
    main()
