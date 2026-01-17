# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title('Password Generator')
window.config(padx=100, pady=50)

canvas = Canvas(width= 200, height= 224)
lock_img = PhotoImage(file='../assets/tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 35, 'bold'), fill='white')
canvas.grid(column=1, row=1)

window.mainloop()