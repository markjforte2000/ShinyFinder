

from .states import initial_state


class Processor(object):

    def __init__(self):
        self.state = initial_state()

    def process(self, model):
        self.state = self.state(model)
        return model


