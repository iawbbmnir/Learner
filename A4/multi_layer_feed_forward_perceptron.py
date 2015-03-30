# Multi Layer Feed Forward Perceptron

import neurolab as nl
import numpy as np
import pylab as pl


class MultiLayerFeedForwardPerceptron:
    def __init__(self, domain, label, minMax, test_domain):
        print(minMax)

        domain = np.array(domain)
        label = np.array(label)

        # print domain

        # Create net with len(minMax) input neurons and 1 output neuron
        self.net = nl.net.newff(minMax, [1, 1])
        self.error = self.net.train(domain, label, epochs=200, show=1)

    def test(self, test_domain):
        return (self.net.sim(test_domain))
