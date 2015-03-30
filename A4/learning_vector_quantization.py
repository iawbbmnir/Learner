import numpy as np
import neurolab as nl
import numpy.random as rand
import pylab as pl


class LearningVectorQuantization:
    def __init__(self, domain, label, minMax):

        # Create train samples
        input = np.array(domain)
        target = np.array(label)

        self.net = nl.net.newlvq(minMax, 10, [1])
        # Train network
        error = self.net.train(input, target, epochs=100)

        # Plot result
        # xx, yy = np.meshgrid(np.arange(-3, 3.4, 0.2), np.arange(-3, 3.4, 0.2))
        # xx.shape = xx.size, 1
        # yy.shape = yy.size, 1
        # i = np.concatenate((xx, yy), axis=1)
        # o = net.sim(i)
        # grid1 = i[o[:, 0]>0]
        # grid2 = i[o[:, 1]>0]

        # class1 = input[target[:, 0]>0]
        # class2 = input[target[:, 1]>0]

        # pl.plot(class1[:,0], class1[:,1], 'bo', class2[:,0], class2[:,1], 'go')
        # pl.plot(grid1[:,0], grid1[:,1], 'b.', grid2[:,0], grid2[:,1], 'gx')
        # pl.axis([-3.2, 3.2, -3, 3])
        # pl.xlabel('Input[:, 0]')
        # pl.ylabel('Input[:, 1]')
        # pl.legend(['class 1', 'class 2', 'detected class 1', 'detected class 2'])
        # pl.show()

    def test(self, test_domain):
        return (self.net.sim(test_domain))
