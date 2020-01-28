import cv2
import numpy as np
import imutils
import pytesseract
import concurrent.futures
import os


from .menu_item import MenuItem
from src import logger


LOGGER_NAME = "MENU_PROC"


def process_menu(frame):
    """
        Returns list of 4 MenuItem,
        sorted from top to bottom
        with name of item and if it is selected
    """
    # set tesseract max thread count to 4
    os.environ['OMP_THREAD_LIMIT'] = '4'
    logger.debug("Trying to find menu items", source=LOGGER_NAME)
    # get contours
    non_selected_contours, selected_contour = get_contours(frame)
    logger.debug("Found menu items", source=LOGGER_NAME)

    all_contours = non_selected_contours.copy()
    all_contours.append(selected_contour)

    # sort by height
    logger.debug("Sorting items", source=LOGGER_NAME)
    all_contours = sorted(all_contours, key=average_height)

    # isolate text and combine to one image
    logger.debug("Isolating Text", source=LOGGER_NAME)
    # create all black mask
    all_text = np.ones(frame.shape[:2], dtype="uint8") * 0
    i = 0
    selected_pos = 0  # keep track of for later
    for contour in all_contours:
        is_selected = contour is selected_contour
        text = isolate_contour_text(frame, contour, is_selected)
        # convert text to gray
        text = cv2.cvtColor(text, cv2.COLOR_BGR2GRAY)
        all_text = cv2.bitwise_or(all_text, text)
        if is_selected:
            selected_pos = i
        i += 1

    logger.debug("Begin processing text", source=LOGGER_NAME)

    logger.debug("Done processing text", source=LOGGER_NAME)

    logger.debug("Creating items", source=LOGGER_NAME)
    menu_items = []
    pos = 0
    text = get_text_from_contour(all_text)

    logger.debug("Menu Processor done", source=LOGGER_NAME)
    return menu_items


def create_menu_item(text, pos, is_selected):
    item = MenuItem(text, is_selected, pos)
    return item


def average_height(contour):
    avg = 0
    n = 0
    for i in contour:
        avg += i[0][1]
        n += 1
    return avg/n


def get_text_from_contour(text_image):
    """Returns string found in contour"""
    text = pytesseract.image_to_string(text_image)
    # replace é with e
    text = text.replace('é', 'e')
    logger.debug("Got text: {}".format(text), source=LOGGER_NAME)
    return text


def isolate_contour_text(frame, contour, is_selected):
    """Returns all white image except for black text inside contour"""
    # if area is not selected, invert frame
    if not is_selected:
        frame = cv2.bitwise_not(frame)
    # create all black mask
    mask = np.ones(frame.shape[:2], dtype="uint8") * 0
    # draw all white filled in contour
    cv2.drawContours(mask, [contour], -1, (255, 255, 255), -1)
    # get part of frame in contour and mask
    text = cv2.bitwise_and(frame, frame, mask=mask)
    # invert it
    text = cv2.bitwise_not(text)
    return text


def get_contours(frame):
    """Returns tuple (3 non-selected items, 1 Selected Item)"""
    # threshold for white and black
    lower_black = np.array([0, 0, 0], dtype=np.uint8)
    upper_black = np.array([10, 10, 10], dtype=np.uint8)
    lower_white = np.array([240, 240, 240], dtype=np.uint8)
    upper_white = np.array([255, 255, 255], dtype=np.uint8)

    # find all menu items
    non_selected_items_mask = cv2.inRange(frame, lower_white, upper_white)
    selected_item_mask = cv2.inRange(frame, lower_black, upper_black)

    # find contours
    non_selected_contours = cv2.findContours(non_selected_items_mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    selected_contours = cv2.findContours(selected_item_mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    non_selected_contours = imutils.grab_contours(non_selected_contours)
    selected_contours = imutils.grab_contours(selected_contours)

    # remove 2 largest contours from non selected - hp bars
    non_selected_contours = sorted(non_selected_contours, key=cv2.contourArea)[:len(non_selected_contours) - 2]
    # get largest 3 remaining contours
    non_selected_contours = non_selected_contours[-3:]

    # get largest selected contours
    selected_contours = sorted(selected_contours, key=cv2.contourArea)[-1:]
    selected_contour = selected_contours[0]

    return non_selected_contours, selected_contour
