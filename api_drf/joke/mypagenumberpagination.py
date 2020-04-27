from rest_framework.pagination import PageNumberPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 1
    max_page_size = 1
    page_size_query_param = 'size'
    page_query_param = 'page'


    '''
    cursor_query_param：表示url中页码的参数
		page_size_query_param：表示每页显示数据量的参数
		max_page_size：表示每页最大显示数量，做限制使用，避免突然大量的查询数据，数据库崩溃
		ordering：表示返回数据的排序方式
    '''
