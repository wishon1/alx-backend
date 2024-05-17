#!/usr/bin/env python3
"""
Simple pagination:

Implement a method named get_page that takes two integer arguments page with
default value 1 and page_size with default value 10.

You have to use this CSV file (same as the one presented at the top of the
project). Use assert to verify that both arguments are integers greater than 0.

Use index_range to find the correct indexes to paginate the dataset correctly
and return the appropriate page of the dataset (i.e. the correct list of rows).

If the input arguments are out of range for the dataset, an empty list should
be returned.
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Function named index_range that takes two integer arguments page and
    page_size.

    Args:
        page (int): the current page
        page_size (int): the size of the page

    Returns (tuple): A tuple of size two containing a start index and an end
        index corresponding to the range of indexes to return in a list for
        those particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        get_page: Retrieves the page of a given dataset.

        Args:
            page (int): The page to work with.
            page_size (int): The size of the page.

        Returns:
            list: The appropriate page of the dataset (i.e., the correct list
            of rows), or an empty list if the start index is greater than the
            length of the dataset.
        """
        # Use assert to verify that both arguments are integers greater than 0.
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]
