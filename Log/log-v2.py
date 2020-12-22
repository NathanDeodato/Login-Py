# Libs
from tkinter import Event
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED


# Layout Window
def winLog():
    # Theme window
    sg.theme("DarkTeal9")

    # Layout
    layout = [
        [sg.Text("User ", size=(8, 0)), sg.Input(size=(22, 2), key="user", border_width=2)],
        [sg.Text("Password ", size=(8, 0)), sg.Input(size=(22, 2), key="password", border_width=2, password_char="*")],
        [sg.Button("OK", size=(5, 1), border_width=2)],

        [sg.Output(size=(30, 4))],
        [sg.Text(" " * 12), sg.Text("(C) NT Developer")]
    ]
    return sg.Window("Nt-Log", layout=layout)


window = winLog()

# Window loop 
while True:
    event, values = window.Read()

    # Close window
    if window == sg.WINDOW_CLOSED:
        break

    # Lib
    from time import sleep

    # Inputs
    user = values["user"]
    password = values["password"]

    # Credecis correct
    user_ok = "NT"
    password_ok = "Deodato12"

    if event == "OK":
        print("-- Processing... --".center(45))
    
        sleep(2)

        if user == user_ok:
            print("User: Correct")
        else:
            print("User: Incorrect")

        sleep(2)

        if password == password_ok:
            print("Password: Correct")
        else:
            print("Password: Incorrect")

