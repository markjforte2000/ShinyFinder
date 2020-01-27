import sys

import cv2

from src.model import Model
from src.processor import Processor
from src.display import show
from src.logger import Logger


def main():
    print('Starting Shiny Finder')
    logger = Logger(log_file="shiny_finder_test_log.txt", automatic_file_writes=False)
    
    filename = 'resources/test/shiny_test_1-1_cropped.mp4'
    cap = cv2.VideoCapture(filename)

    if not cap.isOpened():
        logger.warning("Error opening video file at " + filename)
        sys.exit(0)

    model = Model(None, 0, 0)
    processor = Processor()

    while cap.isOpened():
        ret, frame = cap.read()
        model.frame = frame
        if not ret:
            break

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        model = processor.process(model)
        show(model)

    logger.write_to_file()  # update log file


if __name__ == '__main__':
    main()
