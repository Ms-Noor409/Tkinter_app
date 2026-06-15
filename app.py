import tkinter as tk
from tkinter import messagebox
import re
from openpyxl import load_workbook
from tkinter.font import Font


root = tk.Tk()
root.title("Form")
root.geometry("1500x1500")
root.config(bg="#4F7C82")

frame = tk.Frame(root, bg="#0B2E33")
frame.pack(expand=True) 


title = tk.Label(frame, text="   Contact Form ",fg="#FCFCFC", bg= "#0B2E33", font=("Helvetica", 30, "bold"))
title.grid(row=0, column=0, pady=10)


name = tk.Label(frame, text="Username :", bg="#0B2E33", fg="#FCFCFC", font=("Arial", 16, "bold"))
name.grid(row=1, column=0, padx=10, pady=5,)

name_box = tk.Entry(frame, font=("Arial", 16))
name_box.grid(row=1, column=1, padx=10, pady=5)


number = tk.Label(frame, text="Contact Number :", bg="#0B2E33", fg="#FCFCFC", font=("Arial", 16, "bold"))
number.grid(row=2, column=0, padx=10, pady=5 )

num_box = tk.Entry(frame, font=("Arial", 16))
num_box.grid(row=2, column=1, padx=10, pady=5)

email_text= tk.Label(frame, text="Email :", bg="#0B2E33", fg="#FCFCFC", font=("Arial", 16, "bold"))
email_text.grid(row=3, column=0, padx=10, pady=5)

email_box = tk.Entry(frame, font=("Arial", 16))
email_box.grid(row=3, column=1, padx=10, pady=5)  

def submit_form():
    name = name_box.get()
    number = num_box.get()
    email_text = email_box.get()

    if not re.match(r"^[A-Za-z\s]+$", name):
        messagebox.showerror("Invalid", "Name must contain only letters")
        return
    
    if not number.isdigit() or len(number) != 11:
        messagebox.showerror("Invalid", "Contact number must be exactly 11 digits")
        return
    
    if not re.match(r"^\w+@(\w+\.)?\w+\.(com|edu|pk|gov|net)$", email_text , re.IGNORECASE):
        messagebox.showerror("Invalid", "Enter a valid email")
        return
    
    else:
        messagebox.showinfo("Valid!", "Form submitted successfully")


    with open("data.txt", "a") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Number: {number}\n")
        file.write(f"Email: {email_text}\n")
        file.write("-" * 30 + "\n")

    messagebox.showinfo("Success", "Info Stored successfully")

    name_box.delete(0, tk.END)
    num_box.delete(0, tk.END)
    email_box.delete(0, tk.END)
 

sub_button = tk.Button(frame, text="Submit",command=submit_form, bg="#3C391F", fg="#FCFCFC", font=("Arial", 16))
sub_button.grid(row=4, column=1, pady=20)

root.mainloop()
