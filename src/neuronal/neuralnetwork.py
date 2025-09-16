from abc import ABC
from .neurallayers import (
    NeuralLayer, ReLUNeuralLayer, SigmoideNeuralLayer, TanHNeuralLayer, SigmoidNeurone, ReLUNeurone
    )

class NeuralNetwork(ABC):
    def __init__(self, layers_to_use: list[NeuralLayer]):
        self.__layers: list[NeuralLayer] = layers_to_use

    @property
    def layers(self) -> list[NeuralLayer]:
        return self.__layers
    
    def predict(self, inputs: list[float]) -> list[float]:
        for layer in self.layers:
            inputs = layer.forward(inputs)
        return inputs

class Perceptron(NeuralNetwork):
    def __init__(self, total_inputs_count: int):

        # Créer les neurones pour chaque couche
        relu_neurones = []
        for _ in range(total_inputs_count):
            neurone = ReLUNeurone(0)
            relu_neurones.append(neurone)

        sigmoid_neurones = [SigmoidNeurone(len(relu_neurones))]

        # Instancier les couches
        input_layer: ReLUNeuralLayer = ReLUNeuralLayer(relu_neurones)
        output_layer: SigmoideNeuralLayer = SigmoideNeuralLayer(sigmoid_neurones)

        # Appeler le constructeur parent
        layers: list[NeuralLayer] = [input_layer, output_layer]

        super().__init__(layers)
