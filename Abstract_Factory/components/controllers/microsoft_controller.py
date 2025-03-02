from models.controller_support import ControllerSupport

class MicrosoftController(ControllerSupport):
    def handle_input(self):
        return "Procesando entrada del controlador Microsoft"
    
    # Método específico de Microsoft
    def support_adaptive_triggers(self):
        return "Configurando gatillos adaptivos del controlador Microsoft"