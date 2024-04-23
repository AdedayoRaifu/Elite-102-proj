
# import mysql.connector

 

# connection = mysql.connector.connect(user = 'root@localhost', database = 'LocalinstanceMySQL80', password = 'SQlroot@23096')

 

# connection.close()




import customtkinter 

app = customtkinter.CTk()
app.geometry = ('600x500')
app.title = ('Banking app')

def button_event():
    print('button pressed')

button = customtkinter.CTkButton(app, text='Welcome', width=140, height=28)
button.place(x=10, y=10)

app.mainloop()



