from random import random
from abc import ABC

class NeuralNetwork(ABC):
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
