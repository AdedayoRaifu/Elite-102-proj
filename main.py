#In progress

#imports tkinter/customtkinter
import customtkinter
import tkinter
import mysql.connector
from tkinter import messagebox
 


# Creates UI app
app = customtkinter.CTk()
customtkinter.set_appearance_mode('dark')
app.title('Banking app')
app.geometry("400x150")


# cretes new account
def newAcct():
    name = customtkinter.CTkInputDialog(text="Enter Username: ", title="Account Creation")
    name = name.get_input()
    email = customtkinter.CTkInputDialog(text="Enter Email: ", title="Account Creation")
    email = email.get_input()
    password = customtkinter.CTkInputDialog(text="Enter Password(Must contain Symbols and must be 8 characters long): ", title="Account Creation")
    password = password.get_input() 
    if len(password) < 8:
        messagebox.showinfo("Password", "Need to be longer. Try again")
        
    # Puts inputs into SQL
    connection = mysql.connector.connect(user = 'root', database = 'banking', password = 'SQLroot@23096')

    cursor = connection.cursor()

    addData = ("INSERT INTO userAcc(name, email, password) VALUES ('"+ name +"', '"+ email +"', '"+ password +"')")
    cursor.execute(addData)
    connection.commit()
    cursor.close()
    connection.close()
    
# deposits money

def deposit():
    deposit = customtkinter.CTkInputDialog(text="How much would you like to deposit? :", title="Deposit")
    deposit = deposit.get_input()
    messagebox.showinfo("Information", "You have deposited $" + deposit)

    connection = mysql.connector.connect(user = 'root', database = 'banking', password = 'SQLroot@23096')

    cursor = connection.cursor()

    addData = ("INSERT INTO money(Balance) VALUES ('"+ deposit +"')")
    cursor.execute(addData)
    connection.commit()
    cursor.close()
    connection.close() 

# widtrawls money
def widthrawl():
    widthrawl = customtkinter.CTkInputDialog(text="How much would you like to widthdraw? :", title="Widthrawl")
    widthrawl = widthrawl.get_input()
    messagebox.showinfo("Information", "You have widthdrawn $" + widthrawl)

    connection = mysql.connector.connect(user = 'root', database = 'banking', password = 'SQLroot@23096')

    cursor = connection.cursor()

    addData = ("INSERT INTO money(Widthrawl) VALUES ('" + widthrawl +"')")
    cursor.execute(addData)
    connection.commit()
    cursor.close()
    connection.close() 

# gives user their balance
# def checkBal():
#     connection = mysql.connector.connect(user = 'root', database = 'banking', password = 'SQLroot@23096')
#     cursor = connection.cursor()
#     messagebox.showinfo("Information", "Your Balance is " + )
#     cursor.execute()
#     connection.commit()
#     cursor.close()
#     connection.close() 
    

# creates buttons 
newAcctbutton = customtkinter.CTkButton(app, text="Create Account", command=newAcct)
depositButton = customtkinter.CTkButton(app, text="Deposit", command=deposit)
widthrawlButton = customtkinter.CTkButton(app, text="Widtrawl", command=widthrawl)
# checkBalButton = customtkinter.CTkButton(app, text="Check Balance", command=checkBal)
newAcctbutton.grid(row=0, column=0, padx=20, pady=20, )
depositButton.grid(row=1, column=0, padx=15, pady=15)
widthrawlButton.grid(row=2, column=0, padx=10, pady=10)
# checkBalButton.grid(row=3, column=0, padx=5, pady=5)

app.grid_columnconfigure(0, weight=1)

app.mainloop()

     

# def newAcct(userInput):
#   if userInput == 'create account':
#     print('Username:')
#     newAccount = input()
#     print()
#     print('Password(Must contain symbols and numbers):')
#     newAccountPas = input()
#     print(newAccountPas)
#     if len(newAccountPas) < 8:
#       print('Weak Password, Try again')
#       newAccountPas = input()
#     print()
#     print('Email: ')
#     accEmail = input()
#     print()
#     # add more inputs 
#     print('Account created.')
# if userInput == 'deposit':
#   print()
#   deposit(userInput)

# if userInput == 'withdrawl':
#   print()
#   withdrawl(userInput)

# if userInput == 'check balance':
#   print()
#   checkBal(userInput)

# if userInput == 'create account':
#   print()
#   newAcct(userInput)
  
# if userInput == 'account info':
#   print('Username: ' + newAccount)
#   print('Email ' + accEmail)



