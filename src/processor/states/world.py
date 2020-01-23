from datetime import datetime

import numpy as np
import pytz

from ..states import battle_start


def world_state(model):
    white_threshold = 240
    # Check if battle begins
    if np.average(model.frame) > white_threshold:
        print('Battle started at: {}'.format(datetime.now(pytz.timezone('America/New_York'))))
        model.num_battles += 1
        # return battle start state
        return battle_start.battle_start_state
    return world_state
