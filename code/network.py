import numpy as np


class Network:

    def __init__(self, layers):
        self.layers = layers
        self.biases = [np.random.randn(x) for x in layers[1:]]
        self.weights = [np.random.randn(x, y) for x, y in zip(layers[1:], layers[:-1])]
    
    def GradientDescent(self, x, y):
        pass
    
    def SGD(self, no_of_batches, epochs):
        pass
    
    def CreateBatch(self, no_of_batches):
        pass
    
    def feedforward(self, x):
        num_layers = len(self.layers) - 1
        
        z = [np.zeros(i) for i in self.layers[1:]]
        a = [np.zeros(i) for i in self.layers[1:]]

        for i in range(num_layers):
            z[i] = self.weights[i] * x + self.biases[i]
            a[i] = sigmoid(z[i])
            x = a[i]

        return z, a, x

        # Loop over layers
        # create a l

def sigmoid(x):
    return 1/(1 + np.exp(x))

if __name__ == "__main__":
    
    layers = (784, 30, 10)
    nn = Network(layers)

    print(f"Biases = {len(nn.biases)}\nWeights = {len(nn.weights)}")
    print(f"Shape of Biases for each layers {[x.shape for x in nn.biases]}")
    print("Shape of weights for each layer = {0}".format([x.shape for x in nn.weights]))
