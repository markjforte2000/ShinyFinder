from ...controller.assistant import menu_controller
from ..states import battle_end_state

import numpy as np

MENU_POINT = (564, 325)
MENU__THRESHOLD = 255


def battle_run_state(model, logger, controller):

    # wait for menu to show up
    if not is_menu_up(model.frame, MENU_POINT):
        return battle_run_state

    # run from battle
    logger.info("Running from battle {}".format(model.num_battles))
    menu_controller.run(controller)

    # return battle end state
    return battle_end_state.battle_end_state


def is_menu_up(frame, point):
    roi_size = 10  # (10x10)
    roi_values = frame[point[0] - roi_size: point[0] + roi_size, point[1] - roi_size: point[1] + roi_size].copy()
    print(roi_values)
    # menu is up if average is exactly menu threshold
    return np.average(roi_values) == MENU__THRESHOLD
