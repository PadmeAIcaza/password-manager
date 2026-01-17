# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import messagebox

BG = "#FFD8DF"
L_FONT = ('Times New Roman', 12, 'bold')
B_FONT = ('Times New Roman', 12, 'normal')

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BG)

def add_clicked():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website == '' or email == '' or password =='':
        messagebox.showerror(title='Empty Fields', message='Please fill every field')
        return

    is_ok = messagebox.askokcancel(title='Confirm', message=f'These are the details entered: \nEmail: {email}\nPassword: {password}\nIs this ok to save?')
    if is_ok:
        with open('../data.txt', mode='a') as file:
            file.write(f'{website} | {email} | {password}\n')
            website_entry.delete(0, END)
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
generate_button = Button(window, text="Generate Password", font=B_FONT)
generate_button.grid(row=3, column=2, sticky="w")

add_button = Button(window, text="Add", font=B_FONT, width=36, command=add_clicked)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()



