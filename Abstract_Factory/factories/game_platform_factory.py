from abc import ABC, abstractmethod
from models.graphics_engine import GraphicsEngine
from models.sound_system import SoundSystem
from models.controller_support import ControllerSupport

class GamePlatformFactory(ABC):
    @abstractmethod
    def create_graphics_engine(self):
        pass
    
    @abstractmethod
    def create_sound_system(self):
        pass
    
    @abstractmethod
    def create_controller_support(self):
        pass