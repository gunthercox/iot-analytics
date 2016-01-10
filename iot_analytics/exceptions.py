class InvalidTypeException(Exception):

    def __init__(self, message="The type received is not a known type."):
        self.message = message

    def __str__(self):
        return self.message
