from ..ref import Reference


def run(controller):
    """
    Run from wild battle
    Hits joystick up then a button
    """
    controller.set_joystick_angle(joystick=Reference.JOYSTICK, angle=Reference.JOYSTICK_NORTH)
    controller.release_joystick(joystick=Reference.JOYSTICK, angle=Reference.JOYSTICK_NORTH, delay=0.1)
    controller.press_button(button=Reference.A, delay=.5)

