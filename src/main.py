# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# LOGO
canvas = Canvas(window, width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="../assets/logo.png")
logo_img = logo_img.subsample(3, 3)
canvas.create_image(100, 90, image=logo_img)  # center-ish
canvas.grid(row=0, column=1, pady=(0, 10))


window.mainloop()



