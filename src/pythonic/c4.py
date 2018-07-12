# 列表、元组、集合

# 可迭代对象(iterable)、迭代器(iterator)

# for in iterable

# 对象 class

class Book:
    pass


class BookCollection:
    def __init__(self):
        self.data = ["《往事》", "《只能》", "《回味》"]
        self.cur = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur >= len(self.data):
            raise StopIteration()
        r = self.data[self.cur]
        self.cur += 1
        return r


books = BookCollection()

for book in books:
    print(book)

# 一次性
for book in books:
    print(book)
