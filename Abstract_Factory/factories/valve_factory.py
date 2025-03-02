from factories.game_platform_factory import GamePlatformFactory
from models.graphics_engine import GraphicsEngine
from models.sound_system import SoundSystem
from models.controller_support import ControllerSupport
from components.graphics.valve_graphics import ValveGraphics
from components.sound.valve_sound import ValveSound
from components.controllers.valve_controller import ValveController

class ValveFactory(GamePlatformFactory):
    def create_graphics_engine(self) -> GraphicsEngine:
        return ValveGraphics()
    
    def create_sound_system(self) -> SoundSystem:
        return ValveSound()
    
    def create_controller_support(self) -> ControllerSupport:
        return ValveController()
    
    # Método exclusivo para Valve
    def provide_steam_workshop(self):
        return "Acceso a Steam"