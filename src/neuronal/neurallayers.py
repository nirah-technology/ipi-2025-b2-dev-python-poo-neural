from abc import ABC
from .neurones import Neurone, SigmoidNeurone, TanHNeurone, ReLUNeurone

class NeuralLayer(ABC):
    def __init__(self, neurones_to_use: list[Neurone]):
        self.__neurones: list[Neurone] = neurones_to_use

    @property
    def neurones(self) -> list[Neurone]:
        return self.__neurones
    
    def forward(self, inputs: list[float]) -> list[float]:
        return [neurone.forward(inputs) for neurone in self.neurones]

class SigmoideNeuralLayer(NeuralLayer):
    def __init__(self, neurones_to_use: list[SigmoidNeurone]):
        assert neurones_to_use is not None
        for neurone in neurones_to_use:
            if (not isinstance(neurone, SigmoidNeurone)):
                raise ValueError
        super().__init__(neurones_to_use)

class TanHNeuralLayer(NeuralLayer):
    def __init__(self, neurones_to_use: list[TanHNeurone]):
        assert neurones_to_use is not None
        for neurone in neurones_to_use:
            if (not isinstance(neurone, TanHNeurone)):
                raise ValueError
        super().__init__(neurones_to_use)

class ReLUNeuralLayer(NeuralLayer):
    def __init__(self, neurones_to_use: list[ReLUNeurone]):
        assert neurones_to_use is not None
        for neurone in neurones_to_use:
            if (not isinstance(neurone, ReLUNeurone)):
                raise ValueError
        super().__init__(neurones_to_use)