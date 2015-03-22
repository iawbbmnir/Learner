# Multi Layer Feed Forward Perceptron

import neurolab as nl
import numpy as np
import pylab as pl


class MultiLayerFeedForwardPerceptron:
    def __init__(self, domain, label, minMax):
        # print(domain)
        # print(label)
        print(minMax)

        # Create net with len(minMax) input neurons and 1 output neuron
        # self.net = nl.net.newff(minMax, [10, 1])
        # self.error = self.net.train(domain, label, epochs=100, show=1)

        net = nl.net.newff(minMax, [10, 1])
        error = net.train_gd(domain, label, epochs=100, show=1)

    def test(self, test_domain):
        return (self.net.sim(test_domain))
