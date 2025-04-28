import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200,height=200,highlightthickness=0)
canvas.create_image(100,95, image= logo)
canvas.grid(row=1,column=1)

#Password Generator
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for _ in range(nr_letters)]
    symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]
    number_list = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = letter_list + symbol_list + number_list
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)

#find password
def find_password():
    website_info = website_entry.get()
    try:
        with open("data.json", 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="File Error",message="No data file found.")
    else:
        if website_info in data:
            email = data[website_info]["Email"]
            password = data[website_info]["Password"]
            messagebox.showinfo(title="Website Info",message=f"Email/Username: {email}\n"
                                                             f"Password: {password}")
        else:
            messagebox.showerror(title="Data Error",message=f"No info found for {website_info}.")



#save entries
def save_info():
    website_info = website_entry.get()
    email_info = email_entry.get()
    password_info = password_entry.get()
    new_data = {
        website_info: {
            "Email": email_info,
            "Password": password_info,
        }
    }

    if len(website_info) <=0 or len(password_info) <= 0:
        messagebox.showerror(title="Attention!",message="Please don't leave any fields empty!")
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
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

#labels
website_label = Label(text="Website:")
website_label.grid(row=2,column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=3,column=0)
password_label = Label(text="Password:")
password_label.grid(row=4,column=0)

#entries
website_entry = Entry(width=35)
website_entry.grid(row=2,column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=3,column=1)
email_entry.insert(0,"andy@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=4,column=1)

#buttons
generate_password_button = Button(text="Generate Password",command=gen_password)
generate_password_button.grid(row=4,column=2)
add_button = Button(text="Add",width=20,command=save_info)
add_button.grid(row=5,column=1)
search_button = Button(text="Search",width=14,command=find_password)
search_button.grid(row=2,column=2)











window.mainloop()