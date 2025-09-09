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
        ...