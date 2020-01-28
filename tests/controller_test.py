from src import controller

from time import sleep
import threading


button_dict = {
    'A': controller.A,
    'B': controller.B,
    'X': controller.X,
    'Y': controller.Y,
    'Z': controller.Z,
    'L': controller.L,
    'R': controller.R,
    'Start': controller.START,
    'Joystick': controller.JOYSTICK,
    'CStick': controller.CSTICK
}


def update_controller(cont):
    while True:
        cont.update()


def main():
    cnt = controller.Controller(port='/dev/ttyAMA0')
    sleep(4)  # wait for arduino to reboot

    # separate thread to constantly update the controller
    update_tread = threading.Thread(target=update_controller, args=(cnt,))
    update_tread.daemon = True
    update_tread.start()

    while True:
        print('Enter button to press')
        button = input('')
        if button not in button_dict.keys():
            print('Invalid button: {}'.format(button))
            continue
        button = button_dict[button]

        if button is controller.CSTICK or button is controller.JOYSTICK:
            for i in range(360):
                cnt.set_joystick_angle(button, i)
                sleep(0.01)
            cnt.release_joystick(button)
        else:
            cnt.press_button(button)

        for error in cnt.get_error_stream():
            print('ERROR - {}'.format(error))


if __name__ == '__main__':
    main()
