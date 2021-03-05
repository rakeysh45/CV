from tkinter import *
from tkinter import messagebox
import json
from random import choice, randint, shuffle
import pyperclip

BLUE = "#ccf2f4"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- Search ------------------------------- #
def search():
    website = website_entry.get()
    with open("data.json") as data_file:
        data = json.load(data_file)
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f'Email:{email}\n Password;{password}')


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="please make sure you haven't any field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg=BLUE)
canvas = Canvas(width=200, height=200, bg=BLUE, highlightthickness=0)
logo_img = PhotoImage(file="logoo.gif", )

canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website", bg=BLUE, highlightthickness=0)
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username", bg=BLUE, highlightthickness=0)
email_label.grid(column=0, row=2)
password_label = Label(text="Password", bg=BLUE, highlightthickness=0)
password_label.grid(column=0, row=3)

# entries
website_entry = Entry(width=35, )
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()

email_entry = Entry(width=30)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "rakeyshsingh45@gmail.com")
password_entry = Entry(width=20)
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons

search_button = Button(text="Search", width=14, command=search)
search_button.grid(column=2, row=1)

generate_password_button = Button(text="Generate Password",command= generate_password)
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, sticky="EW")

window.mainloop()
