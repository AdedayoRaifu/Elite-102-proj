import customtkinter as ctk
import tkinter as tk



def button_event():
    print('button pressed')

button = ctk.CTkButton(app, text='CTkButton', width=140, height=28)
button.place(x=10, y=10)