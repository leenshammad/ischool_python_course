class Library :
    def __init__(self):
        self.books=[]
    def add_book(self,titel,author):
        book={'titel':titel,'author':author,'available':True}
        self.books.append(book)
    def remove_book (self,titel):
        for book in self.books:
            if book['titel']== titel:
                self.books.remove(book)
                break
    def display_availbale_books(self):
        for book in self.books:
            if book["available"]:
                print("titel :",book["titel"])
                print("auther:",book["auther"])
                print()
    