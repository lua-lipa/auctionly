

from collections.abc import Iterable, Iterator
from .bidcollection import BidCollection


class BidIterator(Iterator):
    """ Concrete iterator to iterate over the Bid objects """
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: BidCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            if self._reverse:
                self._position += -1
            else:
                self._position += 1
        except IndexError:
            raise StopIteration()

        return value
