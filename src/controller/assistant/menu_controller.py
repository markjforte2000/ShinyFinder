from ..ref import Reference


def run(controller):
    """
    Run from wild battle
    Hits joystick up then a button
    """
    controller.set_joystick_angle(joystick=Reference.JOYSTICK, angle=Reference.JOYSTICK_NORTH)
    controller.set_joystick_angle(joystick=Reference.JOYSTICK, angle=Reference.JOYSTICK_NORTH,
                                  delay=Reference.BUTTON_PRESS_TIME)
    controller.press_button(button=Reference.A, delay=2 * Reference.BUTTON_PRESS_TIME)
    controller.press_button(button=Reference.A, delay=6 * Reference.BUTTON_PRESS_TIME)

