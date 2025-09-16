from abc import abstractmethod  # Faute
 # Faute

class NeuralLayer(): # Faute
    def __init__(self, neurones_to_use: list[Neurone]):  # Faute ?
        self.__neurones: list[Neurone] = neurones_to_use  # Faute ?

    @property
    def neurones(self) -> list[Neurone]:  # Faute ?
        return self.__neurones
    
    def forward(self, inputs: list[float]) -> list[float]:
        return [neurone.forward(inputs) for neurone in self.neurones]

class SigmoideNeuralLayer:   # Faute
    pass

class TanHNeuralLayer:   # Faute
    pass

class ReLUNeuralLayer:   # Faute
    pass