class StorageInterface(object):

    def __init__(self):
        # Assume read and write permissions by default
        self.permissions = [
            "read",
            "write",
        ]

        self.initialize()

    def can(self, permission):
        """
        Check if the current interface has a given permission.
        """
        return permission in self.permissions

    def initialize(self):
        """
        This method should be overridden by a subclass.
        """
        raise NotImplementedError(
            "The mthod `initialize` should "
            "be overridden by a subclass."
        )
