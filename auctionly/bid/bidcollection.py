
""" Iterator design pattern: collection of bids for the bid iterator"""
from collections.abc import Iterable,
from .biditerator import BidIterator


class BidCollection(Iterable):
    """collection of bid items"""

    def __init__(self, collection) -> None:
        self._collection = collection

    def __iter__(self) -> BidIterator:
        return BidIterator(self._collection)

    def get_reverse_iterator(self) -> BidIterator:
        return BidIterator(self._collection, True)

    def add_item(self, item):
        self._collection.append(item)
