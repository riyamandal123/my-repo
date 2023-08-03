from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    special_characters = ["@", "#", "$", "&", "*", "^"]
    password = []
    password.extend(random.sample(numbers, k=3))
    password.extend(random.sample(alphabets, k=6))
    password.extend(random.sample(special_characters, k=2))
    random.shuffle(password)
    Password = ''.join(password)
    password_input.insert(0, Password)
    pyperclip.copy(Password)




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    password_generator()
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if len(website) == 0 or len(password) ==0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")

    else:
        #to display the message box before saving the data inside our data_file.
        is_ok = messagebox.askokcancel(title=website, message=f"The details entered as follows: \nEmail: {email}\n"
                                                      f"Password:{password}\nIs it ok to save it?")
        if is_ok:
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"{website}|{email}|{password}\n")
                website_input.delete(0,END)
                password_input.delete(0,END)
                data_file.close()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

#labels.
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_label.focus()
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Entries.
website_input = Entry(width=36)
website_input.grid(column=1, row=1, columnspan=2)
email_input = Entry(width=36)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "riya@gmail.com")
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

#buttons
pass_generator = Button(text="generate password", command=password_generator)
pass_generator.grid(column=2, row=3)
add = Button(text="add", width=30, command=save_password)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
