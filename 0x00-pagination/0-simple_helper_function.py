#!/usr/bin/env python3
""" module for the index_range function implementation """

from typing import Tuple


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
