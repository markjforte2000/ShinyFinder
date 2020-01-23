from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
from time import sleep

from src.model import Model
from src.processor import Processor
from src.display import show

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
RESOLUTION = (SCREEN_WIDTH, SCREEN_HEIGHT)


def main():
    stream = PiCamera()
    stream.resolution = RESOLUTION
    stream.framerate = 32
    raw_capture = PiRGBArray(stream, size=RESOLUTION)

    model = Model(None, 0, 0)  # init
    processor = Processor()

    for frame in stream.capture_continuous(raw_capture, format="bgr", use_video_port=True):

        model.frame = frame.array
        model = processor.process(model)

        show(model)

        raw_capture.truncate(0)

        # if the `q` key was pressed, break from the loop
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    main()
