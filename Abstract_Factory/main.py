from client import Game
from factories.sony_factory import SonyFactory
from factories.microsoft_factory import MicrosoftFactory
from factories.valve_factory import ValveFactory

def main():
    # Crear juego para Sony PlayStation
    print("Creando juego para Sony PlayStation")
    sony_factory = SonyFactory()
    ps_game = Game(sony_factory)
    ps_game.run()
    # Método exclusivo de Sony
    print(sony_factory.provide_ps_plus())
    print()
    
    # Crear juego para Microsoft Xbox
    print("Creando juego para Microsoft Xbox")
    microsoft_factory = MicrosoftFactory()
    xbox_game = Game(microsoft_factory)
    xbox_game.run()
    # Método exclusivo de Microsoft
    print(microsoft_factory.provide_game_pass())
    print()
    
    # Crear juego para Valve Steam
    print("Creando juego para Valve Steam")
    valve_factory = ValveFactory()
    pc_game = Game(valve_factory)
    pc_game.run()
    # Método exclusivo de Valve
    print(valve_factory.provide_steam_workshop())
    print()
    
    # Métodos específicos de los controladores
    print("Características específicas de los controladores")
    sony_controller = sony_factory.create_controller_support()
    print(sony_controller.support_haptic_feedback())
    
    microsoft_controller = microsoft_factory.create_controller_support()
    print(microsoft_controller.support_adaptive_triggers())
    
    valve_controller = valve_factory.create_controller_support()
    print(valve_controller.support_touchpad())

if __name__ == "__main__":
    main()