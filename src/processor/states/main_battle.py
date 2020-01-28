from datetime import datetime

import numpy as np
import pytz

from ..states import world_state


BLACK_THRESHOLD = 10


def main_battle_state(model, logger):
    """Monitor battle for end and shiny"""
    # Check if battle is over
    average = np.average(model.frame)
    logger.debug(data=average, source="MAIN BATTLE")
    if average < BLACK_THRESHOLD:
        logger.debug('Battle {} ended'.format(model.num_battles))
        return world_state.world_state
    return main_battle_state
