from math import sin, cos, radians

from .controller_manager import ControllerManager
from .ref import Reference


class Controller(object):

    def __init__(self, port=None):
        self.manager = ControllerManager(port)
        return

    def press_button(self, button, delay=0):
        self.manager.add_task(button=button, value=Reference.BUTTON_PRESS, delay=delay)
        self.manager.add_task(button=button, value=Reference.BUTTON_RELEASE, delay=Reference.BUTTON_PRESS_TIME+delay)
        return

    def hold_button(self, button, delay=0):
        self.manager.add_task(button=button, value=Reference.BUTTON_PRESS, delay=delay)
        return

    def release_button(self, button, delay=0):
        self.manager.add_task(button=button, value=Reference.BUTTON_RELEASE, delay=delay)
        return

    def set_joystick_angle(self, joystick, angle, extension=Reference.JOYSTICK_FULL_EXTENSION, delay=0):
        # get joystick extension from unit circle centered around neutral position
        angle_radians = radians(angle)
        joystick_x = int(extension * sin(angle_radians)) + Reference.JOYSTICK_VALUE_NEUTRAL
        joystick_y = int(extension * cos(angle_radians)) + Reference.JOYSTICK_VALUE_NEUTRAL
        if joystick == Reference.JOYSTICK:
            self.manager.add_task(button=Reference.JOYSTICK_L_X, value=joystick_x, delay=delay)
            self.manager.add_task(button=Reference.JOYSTICK_L_Y, value=joystick_y, delay=delay)
        elif joystick == Reference.CSTICK:
            self.manager.add_task(button=Reference.JOYSTICK_R_X, value=joystick_x, delay=delay)
            self.manager.add_task(button=Reference.JOYSTICK_R_Y, value=joystick_y, delay=delay)
        return

    def release_joystick(self, joystick, delay=0):
        if joystick == Reference.JOYSTICK:
            self.manager.add_task(button=Reference.JOYSTICK_L_X, value=Reference.JOYSTICK_VALUE_NEUTRAL, delay=delay)
            self.manager.add_task(button=Reference.JOYSTICK_L_Y, value=Reference.JOYSTICK_VALUE_NEUTRAL, delay=delay)
        elif joystick == Reference.CSTICK:
            self.manager.add_task(button=Reference.JOYSTICK_R_X, value=Reference.JOYSTICK_VALUE_NEUTRAL, delay=delay)
            self.manager.add_task(button=Reference.JOYSTICK_R_Y, value=Reference.JOYSTICK_VALUE_NEUTRAL, delay=delay)
        return

    def get_error_stream(self):
        return self.manager.get_error_stream()

    def get_success_stream(self):
        return self.manager.get_success_stream()

    def update(self):
        self.manager.update()
