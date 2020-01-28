from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
from time import sleep

from src.model import Model
from src.processor import Processor
from src.display import show
from src.logger import Logger
from src import controller


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
RESOLUTION = (SCREEN_WIDTH, SCREEN_HEIGHT)


def main():
    print('Starting Shiny Finder')
    logger = Logger()

    stream = PiCamera()
    stream.resolution = RESOLUTION
    stream.framerate = 32
    raw_capture = PiRGBArray(stream, size=RESOLUTION)

    cnt = controller.Controller(port="/dev/ttyAMA0")

    model = Model(None, 0, 0)  # init
    processor = Processor(logger=logger, controller=cnt)

    for frame in stream.capture_continuous(raw_capture, format="bgr", use_video_port=True):

        cnt.update()

        model.frame = frame.array
        model = processor.process(model)

        show(model)

        raw_capture.truncate(0)

        key = cv2.waitKey(25) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord('q'):
            break
        if key == ord('a'):
            cnt.press_button(button=controller.A)
            logger.info("Pressed A", source="CONTROLLER")


if __name__ == '__main__':
    main()
