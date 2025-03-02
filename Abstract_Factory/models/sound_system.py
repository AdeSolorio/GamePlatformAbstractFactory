from abc import ABC, abstractmethod

class SoundSystem(ABC):
    @abstractmethod
    def play_sound(self):
        pass