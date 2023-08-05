from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
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
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")

    elif len(password) < 8:
        messagebox.showinfo(title="Oops", message="Password should be at least 8 characters long!")

    else:
        try:
            with open("final_data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("final_data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("final_data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
#-------------------------SEARCH PASSWORD-------------------------------#
def search():
    website = website_input.get()
    try:
        with open("final_data.json", mode="r") as data_file:
            data = json.load(data_file)
            new_data = data[website]
    except KeyError:
        messagebox.showinfo(title="Error",message="No data file found!")
    else:
        email = new_data["email"]
        password = new_data["password"]
        messagebox.showinfo(title=website, message=f"Email:{email}\nPassword:{password}")
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
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Entries.
website_input = Entry(width=31)
website_input.grid(column=1, row=1)
website_input.focus()
email_input = Entry(width=49)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "riya@gmail.com")
password_input = Entry(width=31)
password_input.grid(column=1, row=3)

#buttons
pass_generator = Button(text="generate password", command=password_generator, width=14)
pass_generator.grid(column=2, row=3)
add = Button(text="add", width=41, command=save_password)
add.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", width=14, command=search)
search_button.grid(column=2, row=1)

window.mainloop()
