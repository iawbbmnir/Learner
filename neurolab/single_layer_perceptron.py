# Single Layer Perceptron

import neurolab as nl
import pylab as pl


class SingleLayerPerceptron:
    def __init__(self, domain, label, minMax):
        # print(domain)
        # print(label)
        # print(minMax)

        # Create net with 2 inputs and 1 neuron
        self.net = nl.net.newp(minMax, 1)
        self.error = self.net.train(domain, label, epochs=1000, show=100, lr=0.5)

        # Plot results
        # pl.plot(self.error)
        # pl.xlabel('Epoch number')
        # pl.ylabel('Train error')
        # pl.grid()
        # pl.show()

    def test(self, test_domain):
        return (self.net.sim(test_domain))
