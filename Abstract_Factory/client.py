from factories.game_platform_factory import GamePlatformFactory

class Game:
    def __init__(self, factory: GamePlatformFactory):
        self.graphics = factory.create_graphics_engine()
        self.sound = factory.create_sound_system()
        self.controller = factory.create_controller_support()
    
    def run(self):
        print("Iniciando juego...")
        print(self.graphics.render())
        print(self.sound.play_sound())
        print(self.controller.handle_input())
        print("Juego corriendo...")