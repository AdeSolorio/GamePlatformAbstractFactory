from models.controller_support import ControllerSupport

class ValveController(ControllerSupport):
    def handle_input(self):
        return "Procesando entrada del controlador Valve"
    
    # Método específico de Valve
    def support_touchpad(self):
        return "Activando funcionalidad del trackpad táctil de Valve"