import pygame
import time

def init_controller():
    pygame.init()
    pygame.joystick.init()
    if pygame.joystick.get_count() == 0:
        print("No controller found.")
        return None
    else:
        controller = pygame.joystick.Joystick(0)
        controller.init()
        print("Controller initialized:", controller.get_name())
        return controller

def read_controller(controller):
    pygame.event.pump()
    
    # Get controller input values
    buttons = [controller.get_button(i) for i in range(controller.get_numbuttons())]
    axes = [controller.get_axis(i) for i in range(controller.get_numaxes())]
    
    # Print the values
    print("Buttons:", buttons)
    print("Axes:", axes)
    
    # Example usage: check if a specific button is pressed
    if buttons[0] == 1:
        print("Button 0 pressed!")

def main():
    controller = init_controller()
    if controller is None:
        return
    
    while True:
        read_controller(controller)
        time.sleep(5)
        

if __name__ == "__main__":
    main()