# 0x00. Pagination
## Back-end

## Resources:
- [REST API Design: Pagination](https://www.moesif.com/blog/technical/api-design/REST-API-Design-Filtering-Sorting-and-Pagination/#pagination)
- [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS)

## Learning Objectives
- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

## Setup: Popular_Baby_Names.csv
[use this data file for your project](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240517%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240517T102212Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=49c013ecd55475f20a1c9961bd75f3d18ee6949fc44cb3a3396ed244c4dac0b2)

## Tasks
0. Simple helper function
- Write a function named index_range that takes two integer arguments page and page_size.
The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.

File: 0-simple_helper_function.py

1. Simple pagination
- Copy index_range from the previous task and the following class into your code

- Implement a method named get_page that takes two integer arguments page with default value 1 and page_size with default value 10.

	* You have to use this CSV file (same as the one presented at the top of the project)
	* Use assert to verify that both arguments are integers greater than 0.
	* Use index_range to find the correct indexes to paginate the dataset correctly and return the appropriate page of the dataset (i.e. the correct list of rows).
	* If the input arguments are out of range for the dataset, an empty list should be returned.

File: 1-simple_pagination.py

2. Hypermedia pagination
- Replicate code from the previous task.
- Implement a get_hyper method that takes the same arguments (and defaults) as get_page and returns a dictionary containing the following key-value pairs:
	* page_size: the length of the returned dataset page
	* page: the current page number
	* data: the dataset page (equivalent to return from previous task)
	* next_page: number of the next page, None if no next page
	* prev_page: number of the previous page, None if no previous page
	* total_pages: the total number of pages in the dataset as an integer

Make sure to reuse get_page in your implementation.

You can use the math module if necessary.

File: 2-hypermedia_pagination.py

3. Deletion-resilient hypermedia pagination
- The goal here is that if between two queries, certain rows are removed from the dataset, the user does not miss items from dataset when changing page.
- Start 3-hypermedia_del_pagination.py with this code:

- Implement a get_hyper_index method with two integer arguments: index with a None default value and page_size with default value of 10.
- The method should return a dictionary with the following key-value pairs:
		* index: the current start index of the return page. That is the index of the first item in the current page. For example if requesting page 3 with page_size 20, and no data was removed from the dataset, the current index should be 60.
		* next_index: the next index to query with. That should be the index of the first item after the last item on the current page.
		* page_size: the current page size
		* data: the actual page of the dataset
- Requirements/Behavior:
	* use assert to verify that index is in a valid range.
	* If the user queries index 0, page_size 10, they will get rows indexed 0 to 9 included.
	* If they request the next index (10) with page_size 10, but rows 3, 6 and 7 were deleted, the user should still receive rows indexed 10 to 19 included.

file: 3-hypermedia_del_pagination.py
