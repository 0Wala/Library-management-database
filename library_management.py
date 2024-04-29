import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@beth-53#",
    database = "library"
    )

c = mydb.cursor()
# services that the teacher can perform function
def lecturer_session():
            while 1:
                print("*****OUR SERVICES*****")
                print("-----------------------")
                print("1.   Borrowing section ")
                print("2.  Return section    ")
                print("3. Log out           ")
                #among the choices the teacher should choose one in numerics
                insert_option = input(str("Please choose a service: "))
                if insert_option == "1":
                    print("======================PLEASE NOTE================================")
                    print("               A BOOK CAN ONLY BE BORROWED FOR 10 DAYS           ")
                    print("=================================================================")
                    print("Above that it will be counted overdue  and will be penalised upon returning")
                    print("===========================================================================")

                    c.execute("SELECT * FROM bookrecord; ")
                    for x in c:
                        print(x)
                        print("-----------------------------------------------")
                    print("")
                    print("")
                    Bno=input(str("Book code: "))
                    book = input(("Book tittle: "))
                    Author = input(("Author of the book: "))
                    Year = input(("Year of publication: "))


                    days = input(str("Days for borrowing: "))
                    query_values=(Bno,book,Author)
                    query_values1=(book,Author,Year,days)
                    query_values2=(book,Author)
                    c.execute("SELECT Bno FROM bookrecord WHERE Bno = %s AND title = %s and author = %s", query_values)
                    book_check = c.fetchall()
                    if book_check:
                      try:#the borrowed book is recorded in the issued books table as an issued book
                        c.execute("INSERT INTO issue (title,author,year,Days) VALUES(%s,%s,%s,%s)",query_values1)         
                        mydb.commit()
                        if c.rowcount < 1:
                          print("that book is out of stock")
                        else:
                          c.execute("DELETE FROM bookrecord WHERE  title = %s AND author = %s",query_values2)
                          mydb.commit()
                          if c.rowcount<1:
                            print("___________________________________") 
                            print("that book cannot be borrowed") 
                            print("___________________________________")  
                          else:
                            print("Get the book at the front desk of the library") 
                      except mysql.connector.Error as error:
                         print("a book can only be borrowed for a maximum of 10 days")              
                    else:
                        print("______________________________________________")
                        print("sorry, the book is currently not available or check if you've entered the spelling correctly")
                        print("______________________________________________")
         
                elif insert_option == "2":
                    Tittle = input(str("Enter book tittle: "))
                    Author = input(str("Enter book Author name: "))
                    Year = input(str("Enter book year published: "))
                    School = input(str("Enter book department: "))
                    Genre = input(str("Enter book type: "))
                    query_values=(Tittle,Author,Year,School,Genre)
                    query_values1 = (Tittle,Author,Year)
                    #query to return the borrowed book to the book records
                    # query to remove the retrned book from the issued books
                    c.execute("DELETE FROM issue WHERE title = %s AND author = %s AND year = %s",query_values1)         
                    mydb.commit() 
                    if c.rowcount < 1:
                        print("______________________________________________________________________________________________________________________________")          
                        print("the book was either removed from the shelves due to overdue thus you have to  pay the penalty or confirm the details correctly")
                        print("______________________________________________________________________________________________________________________________")
                    else:
                     c.execute("INSERT INTO bookrecord(title,author,year,school,type) VALUES(%s,%s,%s,%s,%s)",query_values)
                     mydb.commit()
                     print("book returned")    
                elif insert_option == "3":
                    break
                else:
                    print("invalid service") 
                    #services that can be accessed  the student function 
def student_session():
            while 1:
                print("---OUR LIBRARY SERVICES ----")
                print("____________________________")
                print("1.Borrow book(s)   ")
                print("2.Return a book    ")
                print("3.log out          ")
                print("----------------------------")
                insert_option = input(str("choose service: "))
                print("..........................")
                if insert_option == "1":
                    print("--------------------------------PLEASE NOTE------------------------------------------")
                    print("               A BOOK CAN ONLY BE BORROWED FOR 10 DAYS           ")
                    print("_____________________________________________________________________________________")
                    print("Above that it will be counted overdue  and will be penalised upon returning")
                    print("_____________________________________________________________________________________")

                    c.execute("SELECT * FROM bookrecord; ")
                    for x in c:
                        print(x)
                        print("___________________________________________________________")
                    print("")
                    print("")
                    Bno=input(str("Search the book code: "))
                    book = input(("Search for the book tittle: "))
                    Author = input(("Search for the author: "))
                    Year = input(("Year of publication: "))
                    days = input(str("enter number of days: "))
                    query_values=(Bno,book,Author)
                    query_values1=(book,Author,Year,days)
                    query_values2=(book,Author)
                    c.execute("SELECT Bno FROM bookrecord WHERE Bno = %s AND title = %s and author = %s", query_values)
                    book_check = c.fetchall()
                    if book_check:
                      try:#the borrowed book is recorded in the issued books table as an issued book
                        c.execute("INSERT INTO issue (title,author,year,Days) VALUES(%s,%s,%s,%s)",query_values1)         
                        mydb.commit()
                        if c.rowcount < 1:
                          print("that book is out of stock")
                        else:
                          c.execute("DELETE FROM bookrecord WHERE  title = %s AND author = %s",query_values2)
                          mydb.commit()
                          if c.rowcount<1:
                            print("___________________________________") 
                            print("that book cannot be borrowed") 
                            print("___________________________________")  
                          else:
                            print("Get the book at the front desk of the library") 
                      except mysql.connector.Error as error:
                         print("A book can only be borrowed for a maximum of 10 days")              
                    else:
                        print("______________________________________________")
                        print("Sorry, the book is currently not available or check if you've entered the spelling correctly")
                        print("______________________________________________")

                elif insert_option == "2":
                    print(".................................")
                    Tittle = input(str("Enter book tittle: "))
                    Author = input(str("Enter book Author name: "))
                    Year = input(str("Enter book year published: "))
                    #School = input(str("Enter book department: "))
                    Genre = input(str("Enter book type: "))
                    query_values=(Tittle,Author,Year,Genre)
                    query_values1 = (Tittle,Author,Year)
                    #query to add the records of the returned book into the book records shelve
                    c.execute("DELETE FROM issue WHERE title = %s AND author = %s AND year = %s",query_values1)         
                    mydb.commit() 
                    if c.rowcount < 1:
                        print("______________________________________________________________________________________________________________________________")          
                        print("the book was either removed from the shelves due to overdue thus you have to  pay the penalty or confirm the details correctly")
                        print("______________________________________________________________________________________________________________________________")
                    else:
                     c.execute("INSERT INTO bookecord(title,author,year,school,type) VALUES(%s,%s,%s,%s,%s)",query_values)
                     mydb.commit()
                     print("book returned")  
                elif insert_option == "3":
                    break
                else:
                    print("invalid service")  
                    #an authetication function for the teacher if his/her password exists in the library database
def auth_lecturer():
    print("LOGIN")
    print("-----------------")
    username = input(str("username: "))
    password = input(str("password: "))
    query_value1 = (username,password)
    #query to confirm availabilty of password and username
    c.execute("SELECT username FROM lecturer WHERE username = %s and password = %s", query_value1)
    user_check = c.fetchall()
    if user_check:
      lecturer_session()
    else:
        print("invalid username or password")
        print("....................................")
        print("SIGN UP")
        print("''''''''''''''''''''''''''''''''''''")

        username = input(str("lecturer username: "))
        password = input(str("lecturer password: "))
        query_values=(username,password)
        #query for self registration into the library system
        c.execute("INSERT INTO lecturer(username,password,role) VALUES(%s,%s,'lecturer')",query_values)
        mydb.commit()
        print("-------------------------------------------------")
        print(" You have been registered succesfully! ")
        print("You can now log in")
        print("-------------------------------------------------")
     
#an authetication function for the teacher if his/her password exists in the library database
def auth_student():
    print("--------------------------------------")
    print("login as a registered student")
    print("--------------------------------------")
    regno = input(str("regno: "))
    password = input(str("password: "))
    query_value1 = (regno,password)
    #query to confirm availabilty of password and username
    c.execute("SELECT regno FROM student WHERE regno = %s and password = %s", query_value1)
    user_check = c.fetchall()
    if user_check:
      student_session()
    else:
        print("invalid or sign up ")
        
        print("--------------------------------")
        print("SIGN UP")
        print("................................")
        regno = input(str("student regno: "))
        password = input(str("student password: "))
        query_values=(regno,password)
     #query for self registration into the library system
        c.execute("INSERT INTO student(regno,password,role) VALUES(%s,%s,'student')",query_values)
        mydb.commit()
        print("-------------------------------------------------")
        print(" You have been registered succesfully! ")
        print("You can now log in")
        print("-------------------------------------------------")
#a function for the servisec that can be accessed by the admin
def admin_session():
    while 1:
        print("Actions")
        print("----------")
        print("1. register new student")
        print("2. register new lecturer")
        print("3. view registered members")
        print("4. remove existing student")
        print("5. remove existing lecturer")
        print("6. view available books")
        print("7. add new books")
        print("8. view issued books")
        print("9. remove unreturned and overdue books from issued books records")
        print("10. exit")
        user_option = input(str("Select: "))
        if user_option == "1":
            print("")
            print("register new student int the library")
            regno= input(str("student regno: "))
            password = input(str("student password: "))
            query_values=(regno,password)
            #query to add a student to the library system
            c.execute("INSERT INTO student(regno,password,role) VALUES(%s,%s,'student')",query_values)
            mydb.commit()
            print("--------------------------------------")
            print(regno +" has been registered as a student")
        elif user_option == "2":
            print("")
            print("Sign up a new Lecturer")
            username = input(str("Lecturer username: "))
            password = input(str("Lecturer password: "))
            query_values=(username,password)
           
            #query to add a student to the library system
            c.execute("INSERT INTO lecturer(username,password,role) VALUES(%s,%s,'lecturer')",query_values)
            mydb.commit()
            print("--------------------------------------")
            print(username +" has been registered as a lecturer")
        elif user_option == "3":
            print("STUDENTS")
            print("--------------------------------------")
            c.execute("SELECT * FROM library_management_system.student;")

            for x in c:
                print(x)
                print("_____________________________________")

            print("LECTURERS")
            print("--------------------------------------")
            c.execute("SELECT * FROM library_management_system.lecturer;")

            for x in c:
                print(x)
                print("____________________________________")
        elif user_option =="4":
            print("")
            print("Diregister existing student")
            regno = input(str("Student regno: "))
            query_values = (regno,"student")
            #query to remove a student from the library system
            c.execute("DELETE FROM student WHERE regno = %s AND role = %s",query_values)
            mydb.commit()
            print("--------------------------------------")
            if c.rowcount < 1:
                print("user does notexist")
            else:
                print(regno + " has been diregistered")
        elif user_option =="5":
            print("")
            print("Diregister existing lecturer")
            username = input(str("lecturer username: "))
            query_values = (username,"lecturer")
                        
            #query to remove a student from the library system
            c.execute("DELETE FROM lecturer WHERE lecturer = %s AND role = %s",query_values)
            mydb.commit()
            print("--------------------------------------")            
            if c.rowcount < 1:
                print("user does notexist")
            else:
                print(username + " has been diregistered")
        elif user_option =="6":
            print("*********************** AVAILABLE BOOKS*****************************")
            c.execute("SELECT * FROM library_management_system.bookrecord;")
            for x in c:
                print(x)
                print("_________________________________________________________________________________________")                        
        elif user_option =="7":
            print("")
            print("Add the delivered book")
            Tittle = input(str("Book Tittle: "))
            Author = input(str("Author's name: "))
            Year = input(str("Year published: "))
            School = input(str("Department: "))
            Genre = input(str("Book type: "))
            query_values=(Tittle,Author,Year,School,Genre)
            #query to add a book to the book Records
            c.execute("INSERT INTO bookRecord(title,author,year,school,type) VALUES(%s,%s,%s,%s,%s)",query_values)
            mydb.commit()
            print("-------------------------------------------")
            if c.rowcount < 1:
                print("The book record has not been added")
            else:
                print(Tittle + " By " + Author + " has been Recorded")
                print("----------------------------------------")
        elif user_option =="8":
            print("***********************ISSUED BOOKS*****************************")
            c.execute("SELECT * FROM library_management_system.issue;")
            for x in c:
                print(x)
                print("_________________________________________________________________________________________")             
        elif user_option == "9":
            print("")  
            print("remove unreturned and are overdue books from issued book records ") 
 
            c.execute("DELETE FROM issue WHERE days > 10")
            mydb.commit()
            print("------------------------------------------")
            if c.rowcount < 1:
                print("The book does not exist in the records")
            else:
                print("Overdue books have been removed from the book records")
                print("-------------------------------------------")

        elif user_option == "10":
            break
        else:
            print("invalid option")
# an authentication function for the admin
def auth_librarian():
    print("*********************")
    print("***LIBRARIAN LOGIN")
    print("*********************")
    password = input(str("password: "))
    if password == "Pass123":
            admin_session()
    else:
            print("incorrect password")
    

def main():
    while 1:
       print("WELCOME TO OUR LIBRARY")
       print("______________________")
       print("LOGIN AS")
       print("**********************")
       print("1.STUDENT     ")
       print("2.LECTURER    ")
       print("3.LIBRARIAN   ")
       #print("*  4  LOG OUT           *")
       print("**********************")
       insert_choice = input(str("SELECT A CHOICE: "))
  
       if insert_choice == "1":
#calling the function for student auntication
          auth_student()
       elif insert_choice == "2":
 #calling the function for teacher auntication
          auth_lecturer()
       elif insert_choice =="3":
#calling the function for library manager auntication
           auth_librarian()
       elif insert_choice == "4":
           break
       else:
             print("invalid choice")

main()