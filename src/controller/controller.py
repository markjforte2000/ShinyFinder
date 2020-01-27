from math import sin, cos, radians

from .controller_manager import ControllerManager
from .ref import Reference


class Controller(object):

    def __init__(self, port=None):
        self.manager = ControllerManager(port)
        return

    def press_button(self, button):
        self.manager.add_task(button=button, value=Reference.BUTTON_PRESS)
        self.manager.add_task(button=button, value=Reference.BUTTON_RELEASE, delay=Reference.BUTTON_PRESS_TIME)
        return

    def hold_button(self, button):
        self.manager.add_task(button=button, value=Reference.BUTTON_PRESS)
        return

    def release_button(self, button):
        self.manager.add_task(button=button, value=Reference.BUTTON_RELEASE)
        return

    def set_joystick_angle(self, joystick, angle, extension=Reference.JOYSTICK_FULL_EXTENSION):
        # get joystick extension from unit circle centered around neutral position
        angle_radians = radians(angle)
        joystick_x = int(extension * sin(angle_radians)) + Reference.JOYSTICK_VALUE_NEUTRAL
        joystick_y = int(extension * cos(angle_radians)) + Reference.JOYSTICK_VALUE_NEUTRAL
        if joystick == Reference.JOYSTICK:
            self.manager.add_task(button=Reference.JOYSTICK_L_X, value=joystick_x)
            self.manager.add_task(button=Reference.JOYSTICK_L_Y, value=joystick_y)
        elif joystick == Reference.CSTICK:
            self.manager.add_task(button=Reference.JOYSTICK_R_X, value=joystick_x)
            self.manager.add_task(button=Reference.JOYSTICK_R_Y, value=joystick_y)
        return

    def release_joystick(self, joystick):
        if joystick == Reference.JOYSTICK:
            self.manager.add_task(button=Reference.JOYSTICK_L_X, value=Reference.JOYSTICK_VALUE_NEUTRAL)
            self.manager.add_task(button=Reference.JOYSTICK_L_Y, value=Reference.JOYSTICK_VALUE_NEUTRAL)
        elif joystick == Reference.CSTICK:
            self.manager.add_task(button=Reference.JOYSTICK_R_X, value=Reference.JOYSTICK_VALUE_NEUTRAL)
            self.manager.add_task(button=Reference.JOYSTICK_R_Y, value=Reference.JOYSTICK_VALUE_NEUTRAL)
        return

    def get_error_stream(self):
        return self.manager.get_error_stream()

    def get_success_stream(self):
        return self.manager.get_success_stream()

    def update(self):
        self.manager.update()
