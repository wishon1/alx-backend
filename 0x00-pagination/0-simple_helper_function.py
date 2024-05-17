#!/usr/bin/env python3
"""
module containing a function named index_range that takes two integer
arguments page and page_size. The function should return a tuple of size
two containing a start index and an end index corresponding to the range of
indexes to return in a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    function named index_range that takes two integer arguments page and
    page_size

    Args:
        page(int): the current page
        page_size(int): the size of the page

    Returns(tuple): tuple of size two containing a start index and an end
        index corresponding to the range of indexes to return in a list for
        those articular pagination parameters
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
