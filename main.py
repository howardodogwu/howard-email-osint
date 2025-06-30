import os
from dotenv import load_dotenv
from email_api import check_email_breach
from utils import validate_email

# Add these imports for Tkinter
import tkinter as tk
from tkinter import messagebox, simpledialog

load_dotenv()  # Load environment variables from .env

def check_email():
    api_key = os.getenv("EMAIL_API_KEY")
    if not api_key:
        messagebox.showerror("Error", "API key not found. Please set the EMAIL_API_KEY environment variable.")
        return

    email = email_entry.get()
    if not validate_email(email):
        messagebox.showerror("Invalid Email", "Invalid email format. Please enter a valid email.")
        return

    result = check_email_breach(api_key, email)
    if isinstance(result, list):
        breaches = "\n\n".join(
            f"{b['Title']} ({b['BreachDate']}):\n{b['Description']}" for b in result
        )
        messagebox.showwarning(
            "Breaches Found",
            f"The email address {email} was found in the following breaches:\n\n{breaches}\n\nRecommendations: Change your passwords and enable MFA!"
        )
    elif result is None:
        messagebox.showinfo("No Breaches", f"Good news! The email address {email} was not found in any known breaches.")
    else:
        messagebox.showerror("Error", f"An error occurred: {result}")

# GUI setup
root = tk.Tk()
root.title("OSINT Email Security Tool")

tk.Label(root, text="Enter an email address to check:").pack(pady=10)
email_entry = tk.Entry(root, width=40)
email_entry.pack(pady=5)

tk.Button(root, text="Check Email", command=check_email).pack(pady=10)

root.mainloop()
