from datetime import datetime

import numpy as np
import pytz

from ..states import world_state


BLACK_THRESHOLD = 10


def battle_end_state(model, logger, controller):
    """Monitor battle for end"""
    # Check if battle is over
    average = np.average(model.frame)
    if average < BLACK_THRESHOLD:
        logger.info('Battle {} ended'.format(model.num_battles))
        return world_state.world_state
    return battle_end_state
