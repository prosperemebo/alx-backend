#!/usr/bin/env python3
""" module for server class implementation """

import csv
from typing import List, Tuple


def index_range(page, page_size) -> Tuple[int]:
    """
    This function returns a tuple of size two containing a
    start index and an end index corresponding to the range
    of indexes to return in a list for those particular
    pagination parameters.

    Args:
        page (int): _description_
        page_size (int): _description_
    """
    skip = page_size * page
    offset = page_size * (page - 1)
    return (offset, skip)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return specific page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        offset, skip = index_range(page, page_size)

        try:
            return self.dataset()[offset:skip]
        except IndexError:
            return []
