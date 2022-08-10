import tkinter.messagebox as messagebox
from tkinter import *
import functions


# Worked on by -Charan
def login(event):
    # THIS FUNCTION IS CALLED WHEN LOGIN BUTTON IS CLICKED AFTER USERNAME AND PASSWORD IS ENTERED
    global Username, password
    user = Username.get()
    passe = password.get()
    pass_file = open("TrainingImageLabel\psd.txt", "r")
    pass_from_file = pass_file.read()

    if passe == pass_from_file:
        login_window.destroy()  # DESTROYS THE LOGIN WINDOW IN ORDER TO MAKE WAY FOR THE MAIN MENU IF USERNAME AND PASSWORD
        # ARE CORRECT
        functions.gui()
    else:
        messagebox.showinfo("Invalid Username or Password!",
                            "You have entered a Invalid Username or Password.Try Again")
    # ------------------------------------------------------------------------------#
    ################################################################################
    ################################################################################
    # ------------------------------------------------------------------------------#


###############################################################################
# -----------------------------------------------------------------------------#
# GUI
# THIS IS THE FIRST WINDOW THAT APPEARS WHEN WE RUN THE PROGRAM
# THIS IS THE ADMIN LOGIN WINDOW WHERE WE HAVE TO ENTER THE USERNAME AND PASSWORD OF ADMIN
login_window = Tk()
# this code snippet is used to place the window in the center of the screen
screen_width = login_window.winfo_screenwidth()
screen_height = login_window.winfo_screenheight()
x_cord = int((screen_width / 2) - (626 / 2))
y_cord = int((screen_height / 2) - (417 / 2))
login_window.geometry(f"626x417+{x_cord}+{y_cord}")

login_window.title("Attendance Logger Login Page")
login_window.resizable(False, False)
# ### WE HAVE USED CANVAS METHOD HERE IN ORDER TO USE TRANSPARENT LABELS (PNG IMAGES SUCH AS THE ADMIN LOGIN
# WORD-ART, USERNAME LABEL AND PASSWORD LABEL)
db_canvas = Canvas(login_window, width=626, height=417)
db_canvas.place(x=0, y=0)
background_image = PhotoImage(file="ProjectImages/neon.png")
db_canvas.create_image((0, 0), anchor="nw", image=background_image)

button_image = PhotoImage(file="ProjectImages/button.png")

main_image = PhotoImage(file='ProjectImages/login1.png')
###
top_label = db_canvas.create_image((220, 25), anchor="nw", image=main_image)

###
username_label = db_canvas.create_text((340, 157), fill='#E4FBFF', text="Username", font=('arial', 20, 'normal'),
                                       anchor="nw")

Username = Entry(db_canvas, bd=3, width=15, font=('arial', 13, 'normal'))
Username.insert(0, "admin")

db_canvas.create_window((480, 160), window=Username, anchor="nw")

password_label = db_canvas.create_text((340, 212), fill='#E4FBFF', text="Password", font=('arial', 20, 'normal'),
                                       anchor="nw")

password = Entry(db_canvas, show="*", bd=3, width=15, font=('arial', 13, 'normal'))
password.focus()  # ensures that the password entry is in focus as soon as the window opens and we can type straight
# away without having to click over the entry widget
db_canvas.create_window((480, 215), window=password, anchor="nw")

submit_button = db_canvas.create_image((420, 300), anchor="nw", image=button_image)
place = db_canvas.tag_bind(submit_button, '<Button-1>', login)
login_window.bind('<Return>', login)  # initiates login function if enter key is pressed

login_window.mainloop()
