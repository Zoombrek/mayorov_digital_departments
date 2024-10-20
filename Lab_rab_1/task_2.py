# TODO Найдите количество книг, которое можно разместить на дискете
disk_size_in_mb = 1.44
disk_size_in_b = disk_size_in_mb * 2**20
pages = 100
strings = 50
symbols = 25
symbol_size_in_b = 4

books = int(disk_size_in_b // (pages * strings * symbols * symbol_size_in_b))

print("Количество книг, помещающихся на дискету:", books)