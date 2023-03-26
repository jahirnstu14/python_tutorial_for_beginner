class library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailabeBooks(self):
        print("present books in this library are : ")
        for num, items in enumerate(self.books):
            print(f"{num+1}.{items}")


    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"you have been issued {bookName}.please,it safe and return this books within 30 days")
            self.books.remove(bookName) 
            return True
        else:
            print("sorry, This books have been isseued other. so , wait untill taker of book from library returned books ") 
            return False

    def returnBook(self, bookName):
        self.books.append(bookName) 
        print("Thanks for returing books and i hope you enjoys the books most and hope for the best for future and go ahead!")

class Student:
    def requestBook(self):
        self.book = input("Enter the books name that you wanto borrow : ")
        return self.book
    
    def returnBook(self):
        self.book = input("Enter the books name that you want to return : ")
        return self.book
     



if __name__=="__main__":

    centralibrary = library(["alogrithms","Django","clrs","Python notes"])
    student = Student()
    #centralibrary.displayAvailabeBooks()
    while(True):
        welcomMsg = '''
        ====== Welcome to central library ======
        Please choose an option :
        1. List all the books
        2.request for a books
        3.add/return a books
        4.Exit the library
        
        '''     
        print(welcomMsg)
        a = int(input("Enter a choice :"))
        if a == 1:
            centralibrary.displayAvailabeBooks() 
        elif a == 2:
            centralibrary.borrowBook(student.requestBook())
        
        elif a == 3:
            centralibrary.returnBook(student.returnBook())

        elif a == 4:
            print("Thanks for chosssing central library . Have a great day ahead!")
            exit()
        else:
            print("invalid choice")

        