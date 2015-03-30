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

        # self.net.trainf = nl.train.train_gdx

        self.error = self.net.train(domain, label, epochs=300, show=1)

        print self.net

        # out = self.net.sim(test_domain)
        # pl.subplot(211)
        # pl.plot(self.error)
        # pl.xlabel('Epoch number')
        # pl.ylabel('error (default SSE)')

        # x2 = np.linspace(0,20,20)
        # y2 = self.net.sim(x2.reshape(x2.size,1)).reshape(x2.size)

        # y3 = out.reshape(len(domain))

        # pl.subplot(212)
        # pl.axis([0,20,-1.5,1.5])
        # pl.plot(x2, y2, '-',domain , label, '.', domain, y3, 'p')
        # pl.legend(['train target', 'net output'])
        # pl.show()

    def test(self, test_domain):
        # print self.net.sim(test_domain)
        return (self.net.sim(test_domain))
