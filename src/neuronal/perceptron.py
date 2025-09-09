from random import random

class Neurone:
    def __init__(self, number_of_inputs_connections: int):
        # Déclarer la liste des connexion avec les neurones précédents.
        self.__weights: list[float] = [0.0] * number_of_inputs_connections
        # Initialiser la valeur des connexion avec une valeur aléatoire
        for index in range(len(self.__weights)):
            self.__weights[index] = random()

class NeuralLayer:
    def __init__(self, neurones_to_use: list[Neurone]):
        self.__neurones: list[Neurone] = neurones_to_use

    @property
    def neurones(self) -> list[Neurone]:
        return self.__neurones

class NeuralNetwork:
    def __init__(self, layers_to_use: list[NeuralLayer]):
        self.__layers: list[NeuralLayer] = layers_to_use

    @property
    def layers(self) -> list[NeuralLayer]:
        return self.__layers
    
    @staticmethod
    def create_perceptron(
            number_of_input_neurones: int,
            number_of_hidden_neurones: int,
            number_of_output_neurones: int
            ):
        
        layers: list[NeuralLayer] = []

        # Input        
        input_neurones: list[Neurone] = [Neurone(0)] * number_of_input_neurones
        input_layer: NeuralLayer = NeuralLayer(input_neurones)
        layers.append(input_layer)

        # Hidden
        hidden_neurones: list[Neurone] = [Neurone(len(input_neurones))] * number_of_hidden_neurones
        hidden_layer: NeuralLayer = NeuralLayer(hidden_neurones)
        layers.append(hidden_layer)

        # Output
        output_neurones: list[Neurone] = [Neurone(len(hidden_neurones))] * number_of_output_neurones
        output_layer: NeuralLayer = NeuralLayer(output_neurones)
        layers.append(output_layer)

        return NeuralNetwork(layers)
