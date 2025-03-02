from abc import ABC, abstractmethod

class GraphicsEngine(ABC):
    @abstractmethod
    def render(self):
        pass