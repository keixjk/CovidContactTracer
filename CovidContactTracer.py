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