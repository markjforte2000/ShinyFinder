from datetime import datetime

import numpy as np
import pytz

from ..states import world


BLACK_THRESHOLD = 10


def main_battle_state(model):
    """Monitor battle for end and shiny"""
    # Check if battle is over
    global BLACK_THRESHOLD
    if np.average(model.frame) < BLACK_THRESHOLD:
        print('Battle ended at: {}'.format(datetime.now(pytz.timezone('America/New_York'))))
        return world.world_state
    return main_battle_state
