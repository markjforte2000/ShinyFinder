from ..ref import Reference


def run(controller):
    """
    Run from wild battle
    Hits joystick up then a button
    """
    controller.set_joystick_angle(joystick=Reference.JOYSTICK, angle=Reference.JOYSTICK_NORTH)  # move to run option
    controller.release_joystick(joystick=Reference.JOYSTICK, delay=Reference.BUTTON_PRESS_TIME)
    controller.press_button(button=Reference.A, delay=Reference.BUTTON_PRESS_TIME * 2)  # select run
    controller.press_button(button=Reference.A, delay=Reference.BUTTON_PRESS_TIME * 4)  # just to be safe

