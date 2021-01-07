def myfunc():
    string='Cppsecrets'
    n=len(string)
    arr=[]
    for i in range(n):
        for j in range(i+1,n+1):
            a=string[i:j]
            arr.append(a)
    print(arr)


def my_func():
    pass


class Rectangle:
    def __init__(self, WIDTH, HEIGHT):
        self.width = WIDTH
        self.height = HEIGHT

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'
