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