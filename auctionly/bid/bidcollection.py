
""" Iterator design pattern: collection of bids for the bid iterator"""
from collections.abc import Iterable
from collections.abc import Iterator


class BidCollection(Iterable):
    """collection of bid items"""

    def __init__(self, collection):
        self._collection = collection

    def __iter__(self):
        """ iterating """
        return BidIterator(self._collection)

    def get_reverse_iterator(self):
        """ reverse iterator """
        return BidIterator(self._collection, True)

    def add_item(self, item):
        """ add item to iterator """
        self._collection.append(item)


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

    def hasNext(self):
        if self._reverse:
            return self._index >= 0
        return self._index < len(self._collection)

    def changeDirection(self):
        if self._reverse is 1:
            self._reverse = 0
        self._reverse = 0
