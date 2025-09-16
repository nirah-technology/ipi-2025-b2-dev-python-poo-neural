from random import uniform
from abc import ABC, abstractmethod
from math import exp, tanh

class Neurone(ABC):
    def __init__(self, number_of_inputs_connections: int):
        # Déclarer la liste des connexion avec les neurones précédents.
        self.__weights: list[float] = [0.0] * number_of_inputs_connections
        # Initialiser la valeur des connexion avec une valeur aléatoire
        for index in range(len(self.__weights)):
            self.__weights[index] = uniform(-1, 1)
        self.__bias: float = uniform(-1, 1)
        print(self.__bias)

    @abstractmethod
    def activate(self, value: float) -> float:
        raise NotImplementedError()
    
    def forward(self, inputs: list[float]) -> float:
        z = sum(
            weight * input for weight, input in zip(self.__weights, inputs)
            ) + self.__bias
        return self.activate(z)

class SigmoidNeurone(Neurone):
    def __init__(self, number_of_inputs_connections: int):
        super().__init__(number_of_inputs_connections)

    def activate(self, x: float):
        return 1 / (1 + exp(-x))

class ReLUNeurone(Neurone):
    def __init__(self, number_of_inputs_connections: int):
        super().__init__(number_of_inputs_connections)

    def activate(self, value: float):
        return max(0, value)

class TanHNeurone(Neurone):
    def __init__(self, number_of_inputs_connections: int):
        super().__init__(number_of_inputs_connections)
    
    def activate(self, value: float):
        return tanh(value)
