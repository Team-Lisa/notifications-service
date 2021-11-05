
class EmptyParameterError(Exception):

    def __init__(self, emptyParameter):
        self.message = emptyParameter + ' is required'

class EmptyPasswordError(Exception):
    pass