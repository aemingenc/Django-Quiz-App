from rest_framework.pagination import PageNumberPagination,CursorPagination


class PageNumPage(PageNumberPagination):
    page_size = 1

class CurserPage(CursorPagination):
    page_size = 2
    ordering= "difficulty"