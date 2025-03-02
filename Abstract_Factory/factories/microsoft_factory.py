from factories.game_platform_factory import GamePlatformFactory
from models.graphics_engine import GraphicsEngine
from models.sound_system import SoundSystem
from models.controller_support import ControllerSupport
from components.graphics.microsoft_graphics import MicrosoftGraphics
from components.sound.microsoft_sound import MicrosoftSound
from components.controllers.microsoft_controller import MicrosoftController

class MicrosoftFactory(GamePlatformFactory):
    def create_graphics_engine(self):
        return MicrosoftGraphics()
    
    def create_sound_system(self):
        return MicrosoftSound()
    
    def create_controller_support(self):
        return MicrosoftController()
    
    # Método exclusivo para Microsoft
    def provide_game_pass(self):
        return "Acceso a Xbox Game Pass"
