from abc import ABC, abstractmethod

class ControllerSupport(ABC):
    @abstractmethod
    def handle_input(self):
        pass