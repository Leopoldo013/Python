import json
from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gerar_password():
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'y',
              'w',
              'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
              'S',
              'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    simbolos = ['!', '@', '#', '$', '%', '&', '*', '(', ')']

    qt_letras = random.randint(8, 10)
    qt_simbolos = random.randint(2, 4)
    qt_numeros = random.randint(2, 4)

    pass_letra = [random.choice(letras) for _ in range(qt_letras)]
    pass_simbolo = [random.choice(simbolos) for _ in range(qt_simbolos)]
    pass_numero = [random.choice(numeros) for _ in range(qt_numeros)]

    password_list = pass_letra + pass_simbolo + pass_numero

    random.shuffle(password_list)

    password = ''.join(password_list)
    tem_pass = password_entry.get()
    if len(tem_pass) == 0:
        password_entry.insert(0, password)

    else:
        password_entry.delete(0, END)
        password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ops!!!", message="Todos os campos tem que ser preenchidos!!!")
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
            messagebox.showinfo(title="Dados ok!!!", message="Dados cadastrados com sucesso!!!")


def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Arquivo não encontrado!!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title=website, message=f"{website} não cadastrado!")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Gerenciador de Password")
window.config(pady=50, padx=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# LABELS

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/User: ")
email_label.grid(row=2, column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# ENTRIES

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=37)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "Digite seu e-mail")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# BUTTONS

search_button = Button(text="Procurar", width=12, command=find_password)
search_button.grid(row=1, column=2)
gerar_password_button = Button(text="Password", width=12, command=gerar_password)
gerar_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=37, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
