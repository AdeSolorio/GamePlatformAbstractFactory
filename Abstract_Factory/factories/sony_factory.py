from factories.game_platform_factory import GamePlatformFactory
from models.graphics_engine import GraphicsEngine
from models.sound_system import SoundSystem
from models.controller_support import ControllerSupport
from components.graphics.sony_graphics import SonyGraphics
from components.sound.sony_sound import SonySound
from components.controllers.sony_controller import SonyController

class SonyFactory(GamePlatformFactory):
    def create_graphics_engine(self):
        return SonyGraphics()
    
    def create_sound_system(self):
        return SonySound()
    
    def create_controller_support(self):
        return SonyController()
    
    # Método exclusivo para Sony
    def provide_ps_plus(self):
        return "Acceso a PS Plus"