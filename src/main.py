# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

BG = "#F7F7F7"

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# LOGO
canvas = Canvas(window, width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="../assets/logo.png")
logo_img = logo_img.subsample(3, 3)
canvas.create_image(100, 90, image=logo_img)  # center-ish
canvas.grid(row=0, column=1, pady=(0, 10))

#  Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e")

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="e")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e")

#  Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()  # cursor starts here

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="w")

#  Buttons
generate_button = Button(text="Generate Password")
generate_button.grid(row=3, column=2, sticky="w")

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()



