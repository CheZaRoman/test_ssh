# def factorial(n):
#     res = 1
#     for i in range(1,n+1):
#         res *= i
#
#     return res
#
# print(factorial(5))


class Parser:

    def __init__(self, url):
        self.url = url
        self.page = None
        self.data = None

    def __get_html_page(self):
        print('__get_html_page')
        self.page = "HTML page"

    def __parse(self):
        print('__parse')
        self.data = {"data": 1234}

    def run(self):
        self.__get_html_page()
        self.__parse()




p = Parser('www.google.com')
p.run()
print(p.data)
