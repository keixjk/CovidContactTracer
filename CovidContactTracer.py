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

def search_entry():
    # Get the name to search for
    search_name = search_entry.get()

    # Search for the name in the file
    found_entries = []
    with open ("contacts.json", "r") as file:
        for line in file:
            entry = json.loads(line)
            if entry ["Name"] == search_name:
                found_entries.append(entry)

    # Display the search results
    if found_entries:
        messagebox.showinfo("Search Results", f"Found {len(found_entries)} entries:\n{found_entries}")
    else:
        messagebox.showinfo("Search Results", "No entries found.")

# GUI setup

# Setting app and app title
app = tk.Tk()
app.title("COVID Contact Tracing App")

# Set window size
app.geometry("400x400")

# Set background color
app.configure(bg="#f0f0f0")

# Styling for labels
label_style = {"bg": "f0f0f0", "fg": "#333333", "font": ("Helvetica", 14)}

name_label = tk.Label(app, text="Name:", **label_style)
name_label.pack()

name_entry = tk.Entry(app)
name_entry.pack()

phone_label = tk.Label(app, text="Phone:", **label_style)
phone_label.pack()

phone_entry = tk.Entry(app)
phone_entry.pack()

email_label = tk.Label(app, text="Email:", **label_style)
email_label.pack()

email_entry = tk.Entry(app)
email_entry.pack()

date_label = tk.Label(app, text="Date of Contact:", **label_style)
date_label.pack()

date_entry = tk.Entry(app)
date_entry.pack()

