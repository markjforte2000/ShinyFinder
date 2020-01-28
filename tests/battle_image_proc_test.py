from src.image_processor.menu_processor import process_menu

import cv2
import pytesseract
from time import time
import platform


def main():

    if platform.system() is "Windows":
        pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


    filename = 'resources/test/pss_battle.jpg'
    image = cv2.imread(filename)

    start = time()
    items = process_menu(image)
    end = time()
    print("Took {0} secs".format(end-start))
    for item in items:
        print(item.name)

    # cv2.imshow("image", image)
    # cv2.waitKey(0)


if __name__ == '__main__':
    main()
