'''
Code by

Ghulam Sidique
BS Software Engineering
UBIT University of Karachi, Pakistan
Email: gsidique37@gmail.com
LinkedIn: https://www.linkedin.com/in/ghulamsidique/
'''


# following library will be used to get the date time 
from datetime import datetime
# following will be used to hide the input characters
import getpass
# pands to convert results into dataframe and perform required operations
import pandas as pd


# ***************************************************************************************************************************
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class library_management_system:

    # following function is used to initialize the variables that will be used in this system
    def __init__(self):
        # to initialize the password that is provided by the organization
        self.provided_pass="letmein"

        # to initailze the number of books through user input
        self.num_books=input

        # initialize the total number of books as 0
        self.total_books=0

        # initialize an empty list for the books 
        self.books={}

        # to cath the issue date and save it
        self.issue_book_date={}

        # initializing the list of the books
        self.book_list=[]

        # issue books list
        self.issued_books={}

        # list of issued books
        self.issued_book_list=[]


# ***************************************************************************************************************************
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # following function will hold the admin information
    def admin(self):

        # to take the user name as input 
        self.name=input("Kindly enter your full name.\n\tName: ")
        print("\nKindly enter the provided password to log in the system.\nYou have 3 attempts to enter the password correctly.\n***** For security reason the characters of input password will remain hidden *****")

        # initialize the attempts variable 
        attempts=0

        # following loop will run 3 times in case the user enters wrong password
        while(attempts < 3):

            # take password as input from the user
            # here getpass.getpass is used to get user input without displaying the characters on the screen
            self.password=getpass.getpass("\tPassword: ")

            # condition to check if the password is correct
            if self.password==self.provided_pass:

                # following line of code will catch the current date and time when user enters the right password
                # .strftime("-----") is used to get the format of date and time in our specified manner
                login_time=datetime.now().strftime("%H:%M:%S %Y-%m-%d")

                # this will inform the user above its login to the system
                print(f"\nHello {self.name} welcome to the portal.\nYou logged in the system at {login_time} after {attempts + 1} attempt(s)")
                
                # when user enters the correct password, the loop will be broken to proceed to the next condition
                break

            # thos will run in case the user enetrs the wrong password
            else:
                print(f"\nYou have entered wrong password.\nKindly re-enter the password again")
                
            # increment the attempts by 1 to make sure the user has only 3 attempts     
            attempts+=1
        
        if self.password!=self.provided_pass:
            print(f"\n\tSorry you cannot access this system as you are not a verified user\n\tYou entered wrong password {attempts} times")


# ***************************************************************************************************************************
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # following function wil be used to change the password
    def change_pass(self):

        # ask user whether to change the password or not
        self.ask=str(input("\nWould you like to change the password?\nType Y or y for Yes and N or n for No.\n\tChoice: "))

        # condition to check yes 
        if self.ask.lower() =='y':

            # the user will be asked to enter the new password
            self.new_password=input("\nKindly enter new password of length at least 7. \n\tNew password: ")
            
            # to get the length of the input password
            self.get_len_new_password=len(self.new_password)

            # condition to check the character length of the password, it should be of 7
            if self.get_len_new_password >= 7:

                # get the current date and time when user changes the password
                pass_change_time=datetime.now().strftime("%H:%M:%S %Y-%m-%d")

                # to update the previous password with the new one
                self.provided_pass=self.new_password

                # to print the information when the user successfully changes the password
                print(f"\nThe password has been changed at {pass_change_time} successfully\nYou are requested to kindly login again with the new password\n")

                # calling admin function to log in with new password
                self.admin()
            
            # in case the character length of new password is less than 7
            else:
                print("\nThe length of the inserted password is less than 7\nThe password is not changed")

        # in case the user does not want to change the password  
        elif self.ask.lower()=='n':
            print("\nIt's okay to go with your old password")

        # this will run when user neither enters y nor n    
        else:
            print("You have entered the different choice")


# ***************************************************************************************************************************
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # # the follwoing function will include all the needed functionalities.
    def add_books(self):
        # ask the number of books to add
        self.num_books = int(input("\nHow many books would you like to enter\n\tNum_books: "))

        # check if user has entered 0 or less than it mistakenly
        if self.num_books > 0:
            # this will add the serial number
            self.serial_num = 1
            print("\nNow add the books")

            # loop to add the books equal to the number of books
            while self.serial_num <= self.num_books:
                # take user input to add books
                self.book_name = str(input("\tBook name: "))

                # condition to check if a book is not already present in the list
                if self.book_name not in self.books:

                    # this will add book along with its quantity
                    self.books[self.book_name] = {"Serial num": [self.serial_num], "Quantity": 1}

                # in case the book already exists in the list
                else:
                    # to append the book along with its serial number
                    self.books[self.book_name]['Serial num'].append(self.serial_num)

                    # this will increment in the quantity by the value of 1
                    self.books[self.book_name]['Quantity'] += 1

                # increment the serial_num variable
                self.serial_num += 1

        else:
            print(f"\nSorry you have entered {self.num_books} number of books which is not possible\nkindly enter a number 1 or greater than 1")


# ***************************************************************************************************************************
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # function to print the books
    def print_books(self):
        # clear the list in order to append the new values in the edit_book() function
        self.book_list.clear() 

        print("\nTotal number of books present are:")

        # loop to access all the elements
        for self.name, self.info in self.books.items():

            # join the result and map it
            self.serial_numbers = ', '.join(map(str, self.info['Serial num']))
            
            # append the results into data
            self.book_list.append([self.name, self.info['Quantity']])

        # convert the output into the pandas dataframe
        # following columns will be displayed on the screen
        self.coulmns=['Book name', 'Quantity']

        # now convert in pandas
        self.result=pd.DataFrame(self.book_list, columns=self.coulmns)
        print(self.result)

    
# ***************************************************************************************************************************
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # function to search a book
    def search_book(self):
        # ask the number of books to search
        self.num_to_search=int(input("\nEnter the number of books to search\n\tNumber of books: "))

        #message
        print('\nEnter the name of the book(s) to search')

        #condition to check 0 input
        if self.num_to_search!=0:
            # dummy variable to be used for while loop
            self.start=0
            #loop to search till the number of books
            while self.start<self.num_to_search : 
                #ask for name of the book(s)
                self.name_to_search=str(input("\tBook name: "))

                #check the books
                if self.name_to_search not in self.books:
                    #message
                    print(f"The book(s) {self.name_to_search} is not present in the list.")
                else:
                    # message
                    print(f"the book(s) {self.name_to_search} is present in the list with quanity {self.books[self.name_to_search]['Quantity']}")

                # increment in start
                self.start+=1
        else:
            #message
            print(f"You have entered wrong number {self.num_to_search} of books")

# ***************************************************************************************************************************
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # function to edit the books 
    def edit_books(self):
        # printing the books so as to provide ease to the users to find the books
        self.print_books()  # this will print the books
        print("\n\tAbove are the books present in the library.\n\tYou can edit any of the books from there")

        # ask user what does he want to edit?
        self.ask_to_edit = int(input("\nTo edit book or quantity, press 1 or 2 to edit\n1) To edit a book \n2) To edit the quantity of books\n\tChoice: "))

        # condition to check what to edit
        if self.ask_to_edit == 1:
            # ask user to enter the name of the book
            self.name_to_edit = str(input("\nEnter the name of the book.\n\tExisting book name: "))

            if self.name_to_edit in self.books:
                # enter the name of the new book here
                self.new_book_name = str(input("\nEnter new book name.\n\tNew book name: "))

                # add the new book in place of the old one
                self.books[self.new_book_name]=self.books.pop(self.name_to_edit)

                # catch the time
                changing_time=datetime.now().strftime("%H:%M:%S %Y-%m-%d")

                # meassge
                print(f"The book {self.name_to_edit} has been changed with new book {self.new_book_name} at time {changing_time}")

            # in case the book is not present in the list    
            else:
                print(f"\nThe book {self.name_to_edit} is not present in the library")

        # if the user wants to edit the quantity of the books
        elif self.ask_to_edit==2:        
            # ask the user to enter the book name to change its quantity
            self.ask_book_name = str(input("\nEnter the name of the book to change its quantity\n\tName of book: "))

            # check if the book is present or not
            if self.ask_book_name in self.books:
                # now ask the user to enter the updated value of the quantity
                self.ask_quantity = int(input(f"\nEnter the new value of the quantity of book not less than 1 for {self.ask_book_name} book.\n\tNew Quantity: "))

                # check if the user has entered the valid value of quantity
                if self.ask_quantity > 0:
                    # now add the updated quantity
                    self.books[self.ask_book_name]['Quantity'] = self.ask_quantity
                    
                    # catch time
                    change_time=datetime.now().strftime("%H:%M:%S %Y-%m-%d")

                    # message
                    print(f"The quantity of the book {self.ask_book_name} has be updated at time {change_time}")
                
                # in case if the user has entered the wrong number
                else:
                    print(f"Sorry! You have entered the wrong number i.e {self.ask_quantity}.\nKindly re-enter the correct number.")
            
            # in case the book is not present in the list
            else:
                print(f"\nThe book {self.ask_book_name} is not present in the library")
        
        # incase user enters a wrong key
        else:
            print(f"\nSorry! you have enterd worng number i.e {self.ask_to_edit}.\nKindly re-enter the number")


# ***************************************************************************************************************************
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # function will be used to issue the books to the users
    def issue_book(self):
        # message to the user
        print('\nYou have following list of books from which you can chose any three books')
        
        # following line will print the list of books 
        self.print_books()

        # ask how many books he needs
        self.ask_for_num_books=int(input('\nHow many books you want to get issued?\nYou can issue upto 3 books only.\n\tNumber of books to issue: '))

        # check if user has entered 0 or less than it mistakenly
        if self.ask_for_num_books > 0:
            # this will add the serial number
            self.serial_num = 1
            print("\nNow enter the name(s) of book(s).")

            # loop to add the books equal to the number of books
            while self.serial_num <= self.ask_for_num_books:
                # take user input to add books
                self.ask_book_name = str(input("\tBook name(s): "))

                # condition to check if a book is not already present in the list
                if self.ask_book_name in self.books:

                    # decrement in the quantity of the book
                    self.books[self.ask_book_name]['Quantity']-=1

                    # catch time and date of issue books
                    self.issue_time=datetime.now().strftime("%H:%M:%S %Y-%m-%d")

                    # record the current date and time for calculating the fine charges later on
                    # self.issue_book_date[self.ask_book_name] = datetime.now()

                    # message
                    print(f"The book(s) {self.ask_book_name} has/have been issued to {self.name} at time {self.issue_time}")

                    # check if the issue book list if the book is not present in the iuuse list
                    if self.ask_book_name not in self.issued_books:

                        # this will add book along with its quantity
                        self.issued_books[self.ask_book_name] = {"Serial num": [self.serial_num], "Quantity": 1}

                    # in case the book already exists in the list
                    else:
                        # to append the book along with its serial number
                        self.issued_books[self.ask_book_name]['Serial num'].append(self.serial_num)

                        # this will increment in the quantity by the value of 1
                        self.issued_books[self.ask_book_name]['Quantity'] += 1

                    # increment the serial_num variable
                    self.serial_num += 1
                else:
                    print(f"The book {self.ask_book_name} is not present in the above books list")
        else:
            print("You have entered wrong number of books")


# ***************************************************************************************************************************
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # function to print the issued books
    def print_issued_books(self):
        #Clear the issued book list to avoid duplicate prints
        self.issued_book_list.clear()

        print("\nTotal number of issued books present is:")

        # Loop to access all the elements
        for issue_book_name, issue_book_info in self.issued_books.items():
            # Join the result and map it
            serial_numbers = ', '.join(map(str, issue_book_info['Serial num']))

            # Append the results into data
            self.issued_book_list.append([issue_book_name, issue_book_info['Quantity']])

        # Convert the output into the pandas dataframe
        # Following columns will be displayed on the screen
        columns = ['Book name', 'Quantity']

        # Now convert in pandas
        self.issued_result = pd.DataFrame(self.issued_book_list, columns=columns)
        print(self.issued_result)

# ***************************************************************************************************************************
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # function to return books back to library
    def return_book(self):
        # message to the user
        print('\nYou can select any book from following list.')
        
        # following line will print the list of books 
        self.print_issued_books()

        # ask how many books he needs
        self.ask_num_books_return=int(input('\nHow many books you want to return?\n\tNumber of books to return: '))

        # check if user has entered 0 or less than it mistakenly
        if self.ask_num_books_return > 0:
            # this will add the serial number
            self.serial_num = 1
            print("\nNow enter the name(s) of book(s).")

            # loop to add the books equal to the number of books
            while self.serial_num <= self.ask_num_books_return:
                # take user input to add books
                self.book_name_to_return = str(input("\tBook name(s): "))

                # condition to check if a book is not already present in the list
                if self.book_name_to_return in self.issued_books:

                    # decrement in the quantity of the book
                    self.issued_books[self.book_name_to_return]['Quantity']-=1

                    # catch time and date of issue books
                    self.return_time=datetime.now().strftime("%H:%M:%S %Y-%m-%d")

                    # message
                    print(f"The book(s) {self.book_name_to_return} has/have been returned by {self.name} at time {self.return_time}")

                    # check if the issue book list if the book is not present in the iuuse list
                    if self.book_name_to_return not in self.books:

                        # this will add book along with its quantity
                        self.books[self.book_name_to_return] = {"Serial num": [self.serial_num], "Quantity": 1}

                    # in case the book already exists in the list
                    else:
                        # to append the book along with its serial number
                        self.books[self.book_name_to_return]['Serial num'].append(self.serial_num)

                        # this will increment in the quantity by the value of 1
                        self.books[self.book_name_to_return]['Quantity'] += 1

                    # increment the serial_num variable
                    self.serial_num += 1
                else:
                    print(f"The book {self.book_name_to_return} is not present in the above books list")
        else:
            print("You have entered wrong number of books")


# ***************************************************************************************************************************
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # function to check fine chargess
    def check_fine(self):
        # check if the books are issued
        if not self.issued_books:
            # message
            print("\nNo Books are issued yet")
        else:
            # print the list of issued books to check fine for each book
            self.print_issued_books()
        
        # ask user number of books to check fine for
        self.num_books_fine=int(input("\nEnter number of books to check fine charges for\n\tNumber of books: "))

        # message
        print("\nNow enter the names of the book(s) by looking at above issued book list")
        # loop
        while self.num_books_fine:
            # ask user for the name of book(s)
            self.name_to_fine=str(input("\n\tEnter name of book: "))
            
            # check if the book is present in the issued book list
            if self.name_to_fine not in self.issued_books:
                # message
                print(f"\nThe book {self.name_to_fine} is not present in the issued book list")
            else:
                # catch the issue date
                self.issue_date=datetime.strptime(self.issue_time,  "%H:%M:%S %Y-%m-%d")

                # catch the return time 
                self.return_date=datetime.strptime(self.return_time,  "%H:%M:%S %Y-%m-%d")

                # catch the time exceeded 
                self.time_exceed=(self.return_date-self.issue_date).days

                # fine charges per day are
                self.fine_charges=50

                # total fine charges will be
                self.total_fine_charges=max(0, self.time_exceed-7)*self.fine_charges

                # printing some information related to the fine charges
                print(f"\nThe book {self.name_to_fine} was issued on {self.issue_time} and returned on {self.return_time}")
                print(f"\nThe total fine charges are {self.total_fine_charges}")
                break


# ***************************************************************************************************************************
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # function to delete book(s)
    def delete_books(self):
        #message
        print("\nDelete any book from following list")

        #print the list of books for user
        self.print_books()

        # ask user the number of books to delete
        self.num_to_delete=int(input("\nEnter the number of books to delete\n\tNumber to delete: "))

        # check 0 input
        if self.num_to_delete !=0:
            # message
            print("Now enter the name of book(s) to delete")

            # dummy
            self.start=0

            #loop
            while self.start<self.num_to_delete:
                # ask user for name
                self.name_to_delete=str(input("Enter book name: "))

                # check the presence of the book in the list
                if self.name_to_delete not in self.books:
                    #message
                    print(f"The book {self.name_to_delete} is not present in the list")
                else:
                    self.books.pop(self.name_to_delete)
                    # message
                    print(f"The book {self.name_to_delete} has been deleted successfully from the list")
                self.start+=1
        else:
            print(f"You have entered the wrong number {self.num_to_delete}")


# ***************************************************************************************************************************
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# this is the main function in which we will run all above functions at one place
def main():
    # class object
    sys=library_management_system()
    
    # message 
    print("\n\t\t\t***** Welcome to the library management system *****")
    # ask user to enter in the system or not
    choice=str(input("\nWould you like to enter in Library management system.\nPress any of the given keys.\n\t1)Press Y or y to enter\n\t2)Press N or n to not to enter\n\t\tChoice:  "))

    # check condition
    if choice.lower()=='y':
        # run the admin function to verify the users
        sys.admin()

        # check the verification 
        if sys.password==sys.provided_pass:
            # welcome message
            print("\n________________________________________\n\t\tDashboard\n________________________________________\n\nYou are welcome to library management system")

            # now running functions according to given conditions
            while True:
                # ask for desired operations from dashboard
                operations=int(input("\nIn order to perform desired operations press any of the following numbers\n\t1--> To add books\n\t2--> To print the list of books\n\t3--> To search book(s)\n\t4--> To edit books\n\t5--> To delete books\n\t6--> To issue book(s)\n\t7--> To print the list of issued books\n\t8--> To return books\n\t9--> Calculate fine charges if applicable\n\t10--> To change password\n\t11--> To log out\n\t\tOperation: "))

                # conditions according to the input numbers defined above
                if operations==1:
                    sys.add_books()
                
                elif operations==2:
                    sys.print_books()
                
                elif operations==3:
                    sys.search_book()

                elif operations==4:
                    sys.edit_books()

                elif operations==5:
                    sys.delete_books()

                elif operations==6:
                    sys.issue_book()

                elif operations==7:
                    sys.print_issued_books()

                elif operations==8:
                    sys.return_book()

                elif operations==9:
                    sys.check_fine()
                    
                elif operations==10:
                    sys.change_pass()

                elif operations==11:
                    # message
                    print("\n\nYou have successfully logged out")
                    break
            
            # important message
            print("\n\t\t**************************************************\n\t\t**************************************************\n\n\t\tThnaks for using this library management system\n\t\tFor any query related to code mail on following email address\n\t\tgsidique37@gmail.com\n\t\tAlso do not forget to connect with me on my following linkedin account\n\t\thttps://www.linkedin.com/in/ghulamsidique/\n\n\t\t**************************************************\n\t\t**************************************************")

        else:
            print('\tTry again by inserting correct password')

    else:
        print("\nIt's okay if you do not want to enter in the system")

main()
