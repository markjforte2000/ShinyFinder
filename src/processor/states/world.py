from datetime import datetime

import numpy as np
import pytz

from ..states import battle_start

WHITE_THRESHOLD = 230


def world_state(model):
    # Check if battle begins
    average_white = np.average(model.frame)
    print(average_white)
    if average_white > WHITE_THRESHOLD:
        print('Battle started at: {}'.format(datetime.now(pytz.timezone('America/New_York'))))
        model.num_battles += 1
        # return battle start state
        return battle_start.battle_start_state
    return world_state
