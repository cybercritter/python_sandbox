"""
  Object that stores a generic message header
"""


class MessageHeader:
    def __init__(self) -> None:
        self._id = None
        self._origin = None
        self._dest = None
        self._size = None

    @property
    def id(self):
        return self._id

    @property
    def origin(self):
        return self._origin

    @property
    def dest(self):
        return self._dest

    @property
    def size(self):
        return self._size
