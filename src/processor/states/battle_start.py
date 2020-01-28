from time import time
from datetime import datetime

import numpy as np
import pytz

from ..states import main_battle

first_message_time = None
second_message_time = None
no_message = True
SHINY_THRESHOLD = 4.0
MESSAGE_POINT = (0.85, 0.9)
MESSAGE_THRESHOLD = 40.0


def battle_start_state(model, logger):
    # compare message times if both set
    global first_message_time, second_message_time, no_message, SHINY_THRESHOLD, MESSAGE_POINT
    if first_message_time and second_message_time:
        # check if shiny
        delay = second_message_time - first_message_time
        logger.debug("Time in between messages: {}".format(delay))
        first_message_time = None
        second_message_time = None
        no_message = True
        if delay > SHINY_THRESHOLD:
            logger.info("Shiny Found!")
            model.num_shinies += 1

        # return main battle state
        return main_battle.main_battle_state

    # create message point
    height, width = model.frame.shape[:2]
    point = (int(MESSAGE_POINT[0] * height), int(MESSAGE_POINT[1] * width))

    # check if message is down
    if not no_message:
        if not is_message_up(model.frame, point):
            no_message = True
        # normal return
        return battle_start_state

    # if message is up set time
    if is_message_up(model.frame, point):
        no_message = False
        if first_message_time:
            second_message_time = time()
        else:
            first_message_time = time()

    return battle_start_state


def is_message_up(frame, point):
    roi_size = 10  # (10x10)
    roi_values = frame[point[0] - roi_size: point[0] + roi_size, point[1] - roi_size: point[1] + roi_size].copy()
    # message is up if average is exactly message threshold
    return np.average(roi_values) == MESSAGE_THRESHOLD
