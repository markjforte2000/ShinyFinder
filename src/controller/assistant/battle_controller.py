from ..ref import Reference


current_angle = 0


def walk_in_circle(controller):
    global current_angle
    current_angle += 10

    controller.set_joystick_angle(angle=current_angle, joystick=Reference.JOYSTICK)
    return
