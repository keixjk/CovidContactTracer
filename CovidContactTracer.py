import tkinter as tk
from tkinter import messagebox
import json

def add_entry():
    # Get information from the user
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    date = date_entry.get()
    location = location_entry.get()

    # Create a dictionary with the collected information
    entry = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Date": date,
        "Location": location
    }

    # Write the entry to a JSON file
    with open("contacts.json", "a") as file:
        file.write(json.dumps(entry) + "\n")

    messagebox.showinfo("Success", "Entry added succesfully!")
    