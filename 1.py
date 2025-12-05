class A:
    def __init__(self, request):
        self.request = request
        print(f'я принял  {self.request} {self.request.POST}')


class Request:
    def __init__(self):
        self.GET = ''
        self.POST = {'login': 'admin', 'password': '1234'}


def login():
    request = Request()
    form = A(request)


login()
