import mysql.connector
import datetime
from datetime import date
con = mysql.connector.connect(host = "localhost",
                              username = "root",
                              password = "YOUR_MYSQL_PASSWORD",
                              database = "librarymanagementsystem")
cursor = con.cursor()


def ReadLibraryInventory():
    Query = "SELECT * FROM LibraryInventory";
    cursor.execute(Query)
    Data = cursor.fetchall()
    print("-----Library Inventory-----")
    print("(Book Id, Book Name, Author, Publisher, Genre, Availability)")
    for i in Data:
        print(i)
        

def ReadBorrowedRegister(): 
    Query = "SELECT * FROM BorrowedRegister ORDER BY IssueDate";
    cursor.execute(Query)
    Data = cursor.fetchall()
    print("-----Borrowed Register-----")
    print("(Student Id, Student Name, Class, Book Id, Issued Date, Returned(Yes/No), Return Date)")
    for i in Data:
        if i[5] == "Yes":
            issue_d = i[4].strftime('%y-%m-%d')
            return_d = i[6].strftime('%y-%m-%d')
            print("(",i[0],",",i[1],",",i[2],",",i[3],",",issue_d,",",i[5],",",return_d,")")
        else:
            issue_d = i[4].strftime('%y-%m-%d')
            print("(",i[0],",",i[1],",",i[2],",",i[3],",",issue_d,",",i[5],",",i[6],")")


def RegisterBook():
    print("-----Welcome to Book Registration Tab-----")
    no = int(input("Enter number of book(s) to be registered: "))
    i = 0
    while (i<no):
        i = i+1
        BookId = int(input("Book Id : "))
        Query1 = "SELECT * FROM LibraryInventory WHERE BookId ="+str(BookId)+"";
        cursor.execute(Query1)
        Data = cursor.fetchone()
        if Data != None:
            print("!!!Book Id already taken!!!  -->  Choose another id.")
            no = no+1
        else:
            BookName = input("Book Name : ")
            Author = input("Author : ")
            Publisher = input("Publisher : ")
            Genre = input("Genre : ")
            Availability = input("Availability (A/B): ").upper()
            if Availability not in ['A', 'B']:
                print("---Invalid Availability. Enter A or B---")
                continue
            Query2 = "INSERT into LibraryInventory values("+str(BookId)+", '"+BookName+"', '"+Author+"', '"+Publisher+"', '"+Genre+"', '"+Availability+"')";
            cursor.execute(Query2)
            con.commit()
            print("---Record Stored---")


def SearchBook(): 
    print("-----Welcome to Searching Tab-----")
    field = input("On what basis do you want to search for the book? (BookId, BookName, Author, Publisher, Genre, Availability) ")
    if field.lower() == "bookid":
        id = int(input("Enter Book Id to be searched: "))
        Query = "SELECT * FROM LibraryInventory WHERE BookId = "+str(id)+"";
        cursor.execute(Query)
        Data = cursor.fetchall()
        if Data == []:
            print("---No Record Found---")
        else:
            print("(Book Id, Book Name, Author, Publisher, Genre, Availability)")
            for i in Data:
                print(i)
        
    elif field.lower() == "bookname":
        name = input("Enter Book Name to be searched: ")
        Query = "SELECT * FROM LibraryInventory WHERE BookName = '"+name+"'";
        cursor.execute(Query)
        Data = cursor.fetchall()
        if Data == []:
            print("---No Record Found---")
        else:
            print("(Book Id, Book Name, Author, Publisher, Genre, Availability)")
            for i in Data:
                print(i)
            
    elif field.lower() == "author":
        author = input("Enter Author to be searched: ")
        Query = "SELECT * FROM LibraryInventory WHERE Author = '"+author+"'";
        cursor.execute(Query)
        Data = cursor.fetchall()
        if Data == []:
            print("---No Record Found---")
        else:
            print("(Book Id, Book Name, Author, Publisher, Genre, Availability)")
            for i in Data:
                print(i)
            
    elif field.lower() == "publisher":
        pub = input("Enter Publisher to be searched: ")
        Query = "SELECT * FROM LibraryInventory WHERE Publisher = '"+pub+"'";
        cursor.execute(Query)
        Data = cursor.fetchall()
        if Data == []:
            print("---No Record Found---")
        else:
            print("(Book Id, Book Name, Author, Publisher, Genre, Availability)")
            for i in Data:
                print(i)
            
    elif field.lower() == "genre":
        genre = input("Enter Genre to be searched: ")
        Query = "SELECT * FROM LibraryInventory WHERE Genre = '"+genre+"'";
        cursor.execute(Query)
        Data = cursor.fetchall()
        if Data == []:
            print("---No Record Found---")
        else:
            print("(Book Id, Book Name, Author, Publisher, Genre, Availability)")
            for i in Data:
                print(i)
            
    elif field.lower() == "availability":
        avail = input("Enter Availability to be searched(A/B): ")
        Query = "SELECT * FROM LibraryInventory WHERE Availability = '"+avail+"'";
        cursor.execute(Query)
        Data = cursor.fetchall()
        if Data == []:
            print("---No Record Found---")
        else:
            print("(Book Id, Book Name, Author, Publisher, Genre, Availability)")
            for i in Data:
                print(i)
            
    else:
        print("---Invalid Input---")


def DeleteBook(): 
    print("-----Welcome to Book Deletion Tab-----")
    no = int(input("How many book(s) do you want to delete? "))
    for i in range(0,no):
        id = int(input("Enter Book Id to be deleted: "))
        Query1 = "SELECT * FROM LibraryInventory WHERE BookId = "+str(id)+"";
        cursor.execute(Query1)
        Data = cursor.fetchone()
        if Data == None:
            print("---No Record Found---")
        else:
            Query2 = "DELETE FROM LibraryInventory WHERE BookId = "+str(id)+"";
            cursor.execute(Query2)
            con.commit()
            print("---Record Deleted---")


def UpdateBook(): 
    print("-----Welcome to Book Updation Tab-----")
    F = True
    while F == True:
        id = int(input("Enter Book Id to be updated: "))
        Query1 = "SELECT * FROM LibraryInventory WHERE BookId = "+str(id)+"";
        cursor.execute(Query1)
        Data = cursor.fetchone()
        if Data == None:
            print("---No Record Found---")
            F = False
        else:
            print("Current information of Book Id",id,"is\n",Data)
            field = input("What do you want to update? (Book Name, Author, Publisher, Genre) ")
            if field.lower() == "book name":
                name = input("Update Book Name : ")
                Query2 = "UPDATE LibraryInventory SET BookName = '"+name+"' WHERE BookId = "+str(id)+"";
                cursor.execute(Query2)
                con.commit()
                cursor.execute(Query1)
                U_Data = cursor.fetchone()
                print("---Book Updated---")
                print("Updated information of Book Id",id,"is\n",U_Data)
            
            elif field.lower() == "author":
                author = input("Update Author : ")
                Query2 = "UPDATE LibraryInventory SET Author = '"+author+"' WHERE BookId = "+str(id)+"";
                cursor.execute(Query2)
                con.commit()
                cursor.execute(Query1)
                U_Data = cursor.fetchone()
                print("---Book Updated---")
                print("Updated information of Book Id",id,"is\n",U_Data)

            elif field.lower() == "publisher":
                pub = input("Update Publisher : ")
                Query2 = "UPDATE LibraryInventory SET Publisher = '"+pub+"' WHERE BookId = "+str(id)+"";
                cursor.execute(Query2)
                con.commit()
                cursor.execute(Query1)
                U_Data = cursor.fetchone()
                print("---Book Updated---")
                print("Updated information of Book Id",id,"is\n",U_Data)

            elif field.lower() == "genre":
                genre = input("Update Genre : ")
                Query2 = "UPDATE LibraryInventory SET Genre = '"+genre+"' WHERE BookId = "+str(id)+"";
                cursor.execute(Query2)
                con.commit()
                cursor.execute(Query1)
                U_Data = cursor.fetchone()
                print("---Book Updated---")
                print("Updated information of Book Id",id,"is\n",U_Data)
            
            else:
                print("---Invalid Input---")
                break
            opt = input("\nDo you want to update more books? (Y/N) ")
            if opt.upper() == 'N':
                break


def IssueBook(): 
    print("-----Welcome to Book Issue Tab-----")
    id = int(input("Enter Book Id to be issued: "))
    Query1 = "SELECT Availability FROM LibraryInventory WHERE BookId = "+str(id)+"";
    cursor.execute(Query1)
    Data = cursor.fetchone()
    if Data == None:
        print("---No Record Found---")
    else:
        if Data[0] == 'B':
            print("This book is currently borrowed by some other student.\n---Issue Request: Denied---")
        else:
            print("---Issue Request: Accepted---\nEnter following information:-")
            std_id = int(input("Student Id : "))
            name = input("Student Name : ")
            cls = int(input("Class (1-12) : "))
            if cls < 1 or cls > 12:
                print("---Invalid Class. Enter a value between 1 and 12---")
                return
            issue_date = str(date.today())
            Query2 = "INSERT into BorrowedRegister values("+str(std_id)+",'"+name+"',"+str(cls)+","+str(id)+",'"+issue_date+"','No',NULL)";
            cursor.execute(Query2)
            con.commit()
            Query3 = "UPDATE LibraryInventory SET Availability = 'B' WHERE BookId = "+str(id)+"";
            cursor.execute(Query3)
            con.commit()
            print("---Book Issued---")


def ReturnBook():
    print("-----Welcome to Book Return Tab-----")
    std_id = int(input("Enter Student Id : "))
    id = int(input("Enter Book Id : "))
    issue_date = input("Enter Issue Date(YYYY-MM-DD) : ")
    Query1 = "SELECT * FROM BorrowedRegister WHERE StudentId = "+str(std_id)+" AND BookId = "+str(id)+" AND IssueDate = '"+issue_date+"'";
    cursor.execute(Query1)
    Data = cursor.fetchone()
    if Data == None:
        print("---Entry Not Found---")
    else:
        print("---Entry Found---")
        if Data[5] == "Yes":
            print("---This book has already been returned---")
            return
        print("(Student Id, Student Name, Class, Book Id, Issued Date, Returned(Yes/No), Return Date)")
        if Data[5] == "Yes":
            issue_d = Data[4].strftime('%y-%m-%d')
            return_d = Data[6].strftime('%y-%m-%d')
            print("(",Data[0],",",Data[1],",",Data[2],",",Data[3],",",issue_d,",",Data[5],",",return_d,")")
        else:
            issue_d = Data[4].strftime('%y-%m-%d')
            print("(",Data[0],",",Data[1],",",Data[2],",",Data[3],",",issue_d,",",Data[5],",",Data[6],")")
        return_date = str(date.today())
        Query2 = "UPDATE BorrowedRegister SET Returned = 'Yes', ReturnDate = '"+return_date+"' WHERE StudentId = "+str(std_id)+" AND BookId = "+str(id)+" AND IssueDate = '"+issue_date+"'";
        cursor.execute(Query2)
        con.commit()
        Query3 = "UPDATE LibraryInventory SET Availability = 'A' WHERE BookId = "+str(id)+"";
        cursor.execute(Query3)
        con.commit()
        print("---Book",id,"Returned---")


def StudentHistory(): 
    print("-----Students' Library History-----")
    std_id = int(input("Enter Student Id to be searched: "))
    Query1 = "SELECT * FROM BorrowedRegister WHERE StudentId = '"+str(std_id)+"' ORDER BY IssueDate";
    cursor.execute(Query1)
    Data = cursor.fetchall()
    if Data == []:
        print("---Student Id",std_id,"has no Library History---")
    else:
        print("---Library History of Student Id",std_id,"found---")
        print("(Student Id, Student Name, Class, Book Id, Issued Date, Returned(Yes/No), Return Date)")
        for i in Data:
            if i[5] == "Yes":
                issue_d = i[4].strftime('%y-%m-%d')
                return_d = i[6].strftime('%y-%m-%d')
                print("(",i[0],",",i[1],",",i[2],",",i[3],",",issue_d,",",i[5],",",return_d,")")
            else:
                issue_d = i[4].strftime('%y-%m-%d')
                print("(",i[0],",",i[1],",",i[2],",",i[3],",",issue_d,",",i[5],",",i[6],")")
        

print("----------WELCOME TO THE LIBRARY----------")        
Access = input("Are you Admin(A) or Student(S)?\nTo Exit, press E: ")
if Access.upper() == 'A':
    print("To view Library Inventory: Press 1\nTo view Borrowed Register: Press 2\nTo register new books: Press 3\nTo search for a particular book: Press 4\nTo delete book: Press 5\nTo update book information: Press 6\nTo issue book: Press 7\nTo return book: Press 8\nTo view Students' Library History: Press 9\nTo exit: Press 10")
    while True:
        try:
            Ch = int(input("\nEnter Action: "))
        except ValueError:
            print("---Please enter a number---")
            continue
        if Ch == 1:
            ReadLibraryInventory()
        elif Ch == 2:
            ReadBorrowedRegister()
        elif Ch == 3:
            RegisterBook()
        elif Ch == 4:
            SearchBook()
        elif Ch == 5:
            DeleteBook()
        elif Ch == 6:
            UpdateBook()
        elif Ch == 7:
            IssueBook()
        elif Ch == 8:
            ReturnBook()
        elif Ch == 9:
            StudentHistory()
        else:
            print("-----System Closed-----")
            con.close()
            break
        
elif Access.upper() == 'S':
    print("To view Library Inventory: Press 1\nTo search for a particular book: Press 2\nTo exit: Press 3")
    while True:
        try:
            Ch = int(input("\nEnter Action: "))
        except ValueError:
            print("---Please enter a number---")
            continue
        if Ch == 1:
            ReadLibraryInventory()
        elif Ch == 2:
            SearchBook()
        else:
            con.close()
            print("-----System Closed-----")
            break

elif Access.upper() == 'E':
    print("-----System Closed-----")
    con.close()    

else:
    print("!! INVALID INPUT !!")
    con.close()
