#binary classifier
import numpy as np      #importing numpy library

class Neuron:           # define a class named Neuron
  def __init__(self, n_inputs, bias = 0., weights = None):
    self.b = bias       # store the bias value inside the object
    if weights: self.ws = np.array(weights)
    else: self.ws = np.what dorandom.rand(n_inputs)     # details about weights

  def __call__(self, xs):      # to call Neuron like a function
    return self._f(xs @ self.ws + self.b)

  def _f(self, x):    # activation function (Leaky ReLU)
    return max(x*.2, x)  # if x < 0 -- scale it down (0.2x), else keep x

perceptron = Neuron(n_inputs = 4, bias = 0.05, weights = [0.5, 1.2, -0.3, 0.8])    # create a neuron
perceptron([1, -1, 0.5, 2])   # call the neuron
