#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination

The goal here is that if between two queries, certain rows are removed from the
dataset, the user does not miss items from dataset when changing page.

Start 3-hypermedia_del_pagination.py with this code:
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict:
        """
        Retrieve a paginated subset of the dataset along with pagination metadata.

        Args:
            index (int, optional): The starting index of the requested page.
            Defaults to None.
            page_size (int, optional): The number of items to include on each page.
            Defaults to 10.

        Returns:
            dict: A dictionary containing the following key-value pairs:
                - index (int): The starting index of the current page. For example,
                if requesting page 3 with a page_size of 20 and no data has been
                removed, the current index would be 60.

                - next_index (int): The index to use for the next page request. This
                is the index of the first item after the last item on the current page.

                - page_size (int): The current page size.

                - data (list): The actual items of the dataset for the current page.

        Behavior:
            - Uses assert to ensure that the provided index is within the valid range of
            the dataset.

            - If the user queries index 0 with page_size 10, they will receive items
            indexed from 0 to 9 inclusive.

            - If the user requests the next index (e.g., 10) with page_size 10, but certain
            rows (e.g., 3, 6, and 7) have been deleted, the user should still receive the
            items indexed from 10 to 19 inclusive, effectively skipping over the deleted
            items.
        Raises:
            AssertionError: If the provided index is out of the valid range.
        """
        index_data = self.index_dataset()
        assert index is not None and index >= 0 and index <= max(index_data.keys())

        page_content = []
        data_count = 0
        next_index = None
        start = index if index else 0

        for key, item in index_data.item():
            if key >= start and data_count < page_size:
                page_content.append(item)
                data_count += 1
                continue
            if data_count == page_size:
                next_index = 1
                break

        page_info = {
            'index': index,
            'next_index': next_index,
            'page_size': len(page_content),
            'data': page_content,
        }
        return page_content
