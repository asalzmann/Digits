import numpy as np
import math

class neuralNetwork(object):

	def __init__(self):
		#sizes of each layer
		self.inputLayerSize = 784
		self.outputLayerSize = 10
		self.hiddenLayerSize = 15

		# arrays of weights that take us from input to hidden and hidden to output
		self.w1 = np.random.randn(self.inputLayerSize, self.hiddenLayerSize)
		self.w2 = np.random.random(self.hiddenLayerSize, self.outputLayerSize)


	def sigmoid(self, x):
		'''returns the sigmoid of x'''
		return 1/(1+ math.pow(math.e, -x))

	def sigmoidPrime(self, x):
		'''returns the derivative of the sigmoid (the nabla)'''
		return np.exp(-x)/ ((1+ np.exp(-x)) ** 2)

	def costFunction(self, w, b):
		'''returns the cost function given an array of weights and biases'''
		self.a = self.forward(w)
		return  1/(2*n) * sum(y - self.a**2)

	def forward(self, X):
		'''X is the input to the neural network. a is the output with the current weights'''
		self.z2 = np.dot(X, self.w1)
		self.a2 = self.sigmoid(self.z2)
		self.z3 = np.dot(self.a2, self.w2)
		a = self.sigmoid(self.z3)
		return a 




