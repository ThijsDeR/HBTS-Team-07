import pygame

class Controller:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        if pygame.joystick.get_count() == 0:
            print("No controller found.")
        else:
            controller = pygame.joystick.Joystick(0)
            controller.init()
            print("Controller initialized:", controller.get_name())
            self.controller = controller

    def read_controller(self):
        pygame.event.pump()
        
        # Get controller input values
        buttons = [self.controller.get_button(i) for i in range(self.controller.get_numbuttons())]
        axes = [self.controller.get_axis(i) for i in range(self.controller.get_numaxes())]
        controller_dict = {
            "left": abs(axes[0]) if axes[0] < 0 else 0,
            "right": axes[0] if axes[0] > 0 else 0,
            "forward": (axes[5] + 1) / 2,
            "backward": (axes[4] + 1) / 2,
            "quiting": True if (buttons[6]) else False
        }
        
        return controller_dict