from models.controller_support import ControllerSupport

class SonyController(ControllerSupport):
    def handle_input(self):
        return "Procesando entrada del controlador Sony"
    
    # Método específico de Sony
    def support_haptic_feedback(self):
        return "Activando retroalimentación avanzada en el controlador Sony"