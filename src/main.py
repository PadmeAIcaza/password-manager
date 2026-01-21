# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

BG = "#FFD8DF"
L_FONT = ('Times New Roman', 12, 'bold')
B_FONT = ('Times New Roman', 12, 'normal')

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BG)

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(0, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)

def add_clicked():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
    website: {
        'email': email,
        'password': password
        }
    }

    if website == '' or email == '' or password =='':
        messagebox.showerror(title='Empty Fields', message='Please fill every field')
    else:
        try:
            with open('../data.json', mode='r') as file:
                data = json.load(file) # reads old data
        except FileNotFoundError:
            with open('../data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data) # updates old data with new data

            with open('../data.json', 'w') as file:
                json.dump(data, file, indent=4) # saves updated data
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)


# LOGO
canvas = Canvas(window, width=200, height=200, bg=BG, highlightthickness=0)
logo_img = PhotoImage(file="../assets/logo.png")
logo_img = logo_img.subsample(3, 3)
canvas.create_image(100, 90, image=logo_img)  # center-ish
canvas.grid(row=0, column=1, pady=(0, 10))

# Labels
website_label = Label(window, text="Website:", font=L_FONT, bg=BG)
website_label.grid(row=1, column=0, sticky="e")

email_label = Label(window, text="Email/Username:", font=L_FONT, bg=BG)
email_label.grid(row=2, column=0, sticky="e")

password_label = Label(window, text="Password:", font=L_FONT, bg=BG)
password_label.grid(row=3, column=0, sticky="e")

# Entries
website_entry = Entry(window, width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
website_entry.focus()

email_entry = Entry(window, width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")

password_entry = Entry(window, width=21)
password_entry.grid(row=3, column=1, sticky="w")

# Buttons
generate_button = Button(window, text="Generate Password", font=B_FONT, command=generate_password)
generate_button.grid(row=3, column=2, sticky="w")

add_button = Button(window, text="Add", font=B_FONT, width=36, command=add_clicked)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()



