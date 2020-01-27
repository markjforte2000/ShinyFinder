from .states import initial_state
from ..controller import controller


class Processor(object):

    def __init__(self):
        self.state = initial_state()
        self.controller = controller.Controller()

    def process(self, model):
        self.state = self.state(model)
        return model


