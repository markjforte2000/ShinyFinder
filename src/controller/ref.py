

class Reference(object):
    # Button Codes for Arduino
    A = 1
    B = 2
    X = 3
    Y = 4
    Z = 5
    L = 6
    R = 7
    JOYSTICK_R_X = 8
    JOYSTICK_R_Y = 9
    JOYSTICK_L_X = 10
    JOYSTICK_L_Y = 11
    START = 12
    # Invalid buttons - for conversion in controller.oy only
    JOYSTICK = -1
    CSTICK = -2
    # Button States
    BUTTON_PRESS = 2
    BUTTON_RELEASE = 1
    BUTTON_PRESS_TIME = 0.25
    JOYSTICK_VALUE_NEUTRAL = 128
    JOYSTICK_FULL_EXTENSION = 127
    JOYSTICK_HALF_EXTENSION = 63
    JOYSTICK_NORTH = 0
    JOYSTICK_NORTH_EAST = 45
    JOYSTICK_EAST = 90
    JOYSTICK_SOUTH_EAST = 135
    JOYSTICK_SOUTH = 180
    JOYSTICK_SOUTH_WEST = 225
    JOYSTICK_WEST = 270
    JOYSTICK_NORTH_WEST = 315
