books = []

book1 = input("Type your top favorite book and then press enter. ")
book2 = input("Type your second favorite book and then press enter. ")
book3 = input("Type your third favorite book and then press enter. ")

books.append(book1)
books.append(book2)
books.append(book3)
books.sort()

print(books)
