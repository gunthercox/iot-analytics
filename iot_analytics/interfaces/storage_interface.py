class StorageInterface(object):
    """
    This base class should be subclassed by all other storage interfaces.
    """

    def __init__(self, **kwargs):
        # Assume read and write permissions by default
        self.permissions = [
            "read",
            "write",
        ]

        self.initialize(**kwargs)

    def can(self, permission):
        """
        Check if the current interface has a given permission.
        """
        return permission in self.permissions

    def initialize(self, **kwargs):
        """
        This method should be overridden by a subclass.
        """
        raise NotImplementedError(
            "The method `initialize` should "
            "be overridden by a subclass."
        )

    def timestamp(self):
        from datetime import datetime
        import json

        return json.dumps({'date': datetime.now()}, default=datetime.isoformat)
