from .states import initial_state
from ..controller import controller


class Processor(object):

    def __init__(self, logger):
        self.state = initial_state()
        self.controller = controller.Controller()
        self.logger = logger

    def process(self, model):
        self.state = self.state(model, self.logger)
        return model


