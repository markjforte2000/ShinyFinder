
import numpy as np

from ..states import battle_start
from ...controller.assistant.battle_controller import walk_in_circle
from ... import controller as controller_ref

WHITE_THRESHOLD = 230


def world_state(model, logger, controller):
    # Check if battle begins
    average_white = np.average(model.frame)
    if average_white > WHITE_THRESHOLD:
        model.num_battles += 1
        logger.info('Battle {} started'.format(model.num_battles))
        # return battle start state
        controller.release_joystick(joystick=controller_ref.JOYSTICK)
        return battle_start.battle_start_state

    walk_in_circle(controller)
    return world_state
