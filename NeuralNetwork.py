import numpy as np

class NeuralNetwork(object):

	def __init__(self):
		self.inputLayerSize = 4
		self.outputLayerSize = 1
		self.hiddenLayerSize = 3

		#initialize weights around the mean
		self.W1 = 2*np.random.random((2, self.inputLayerSize)) - 1
		self.W2 = 2*np.random.random((4, self.outputLayerSize)) - 1

	def train(self, X, y):

		#train for 500,000 epochs
		for j in range(500000):
			layer0 = X
			layer1 = self.sigmoid(np.dot(layer0, self.W1))
			layer2 = self.sigmoid(np.dot(layer1, self.W2))
			
			#error
			layer2_error = y - layer2
			if (j % 10000) == 0:
				print("Error: " + str(np.mean(np.abs(layer2_error))))

			#backpropagate 
			layer2_delta = layer2_error*self.sigmoid_prime(layer2)
			layer1_error = layer2_delta.dot(self.W2.T)
			layer1_delta = layer1_error * self.sigmoid_prime(layer1)

			self.W2 += layer1.T.dot(layer2_delta) * .1
			self.W1 += layer0.T.dot(layer1_delta) * .1

	# test input X
	def getResult(self, X):
		weights1 = self.W1
		weights2 = self.W2

		layer0 = X
		layer1 = self.sigmoid(np.dot(layer0, weights1))
		layer2 = self.sigmoid(np.dot(layer1, weights2))
		return layer2
	
	#non-linear function (sigmoid)
	def sigmoid(self, z):
		return 1 / (1 + np.exp(-z))

	#sigmoid derivative
	def sigmoid_prime(self, z):
		return np.exp(-z)/((1+np.exp(-z))**2)


def main():
	X = np.array([[1, 1],
				 [1, 0],
				 [0, 1],
				 [0, 0]])

	y = np.array([[0],
				[1], 
				[1], 
				[0]])

	print(X, "\n ==============\n", y)

	nn = NeuralNetwork()

	print("\n===========\n")
	nn.train(X, y)

	print("\n===========\n")
	print(nn.getResult(np.array([[0, 0],
				 [0, 1],
				 [1, 1],
				 [1, 0]])))

if  __name__=="__main__":
	main()
