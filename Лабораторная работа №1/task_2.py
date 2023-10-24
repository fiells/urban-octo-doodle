# TODO Найдите количество книг, которое можно разместить на дискете
storage = 1.44
pages = 100
str_ = 50
symbols = 25
one_symbol = 4

size_book = pages * str_ * symbols * one_symbol / 1024
storage_kilobytes = storage * 1024
amount_books = int(storage_kilobytes//size_book)

print("Количество книг, помещающихся на дискету:", amount_books)
