from .neuralnetwork import Perceptron

def main():
    network = Perceptron(2)
    print(network.predict([0, 1]))
    print(network.predict([1, 1]))

if __name__ == "__main__":
    main()
