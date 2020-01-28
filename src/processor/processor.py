from .states import initial_state
from ..controller import controller


class Processor(object):

    def __init__(self, logger, controller):
        self.state = initial_state()
        self.controller = controller
        self.logger = logger

    def process(self, model):
        self.state = self.state(model, self.logger)
        return model


