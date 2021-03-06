#!/usr/bin/python

from perceptron import Perceptron

f = lambda x: x

class LinearUnit(Perceptron):
    def __init__(self, input_num):
        Perceptron.__init__(self, input_num, f)

def get_training_dataset():
    input_vecs = [[5],[3],[8],[1.4],[10.1]]    
    lables = [5500, 2300, 7600, 1800, 11400]
    return input_vecs, lables

def train_linear_unit():
    lu = LinearUnit(1)
    input_vecs, labels = get_training_dataset()
    lu.train(input_vecs, labels, 10, 0.01)
    return lu

if __name__ == '__main__':
    linear_unit = train_linear_unit()

    print (linear_unit)

    #test
    print( 'work 3.4 years, monthly salary=%.2f' % linear_unit.predict([3.4]))
    print ('work 15 years, monthly salary=%.2f' % linear_unit.predict([15]))
    print ('work 1.5 years, monthly salary=%.2f' % linear_unit.predict([1.5]))
    print ('work 6.3 years, monthly salary=%.2f' % linear_unit.predict([6.4]))
