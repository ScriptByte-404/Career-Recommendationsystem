import tkinter as tk
from tkinter import messagebox
from ui_utils import create_navbar
import hashlib


class SignupPage(tk.Frame):
    def __init__(self, parent, db):
        super().__init__(parent, bg="#F4F6FB")
        self.parent = parent
        self.db = db

        create_navbar(self, "Sign Up - Create Account")

        card = tk.Frame(self, bg="#FFFFFF", padx=30, pady=30, relief="raised", bd=2)
        card.place(relx=0.5, rely=0.5, anchor="center", width=420, height=420)

        title = tk.Label(card, text="📝 Create Account", font=("Segoe UI", 20, "bold"), fg="#1E293B", bg="#FFFFFF")
        title.pack(pady=10)

        tk.Label(card, text="Username", bg="#FFFFFF").pack(anchor="w", padx=8, pady=(8,2))
        self.username = tk.Entry(card, font=("Segoe UI", 12), bg="#F4F6FB")
        self.username.pack(fill="x", padx=8)

        tk.Label(card, text="Password", bg="#FFFFFF").pack(anchor="w", padx=8, pady=(8,2))
        self.password = tk.Entry(card, show="*", font=("Segoe UI", 12), bg="#F4F6FB")
        self.password.pack(fill="x", padx=8)

        tk.Label(card, text="Confirm Password", bg="#FFFFFF").pack(anchor="w", padx=8, pady=(8,2))
        self.confirm = tk.Entry(card, show="*", font=("Segoe UI", 12), bg="#F4F6FB")
        self.confirm.pack(fill="x", padx=8)

        signup_btn = tk.Button(card, text="Create Account", bg="#10B981", fg="white", command=self.create_account)
        signup_btn.pack(pady=18)

        back_btn = tk.Button(card, text="Back to Login", command=lambda: self.parent.show_page("Login"))
        back_btn.pack()

    def create_account(self):
        uname = self.username.get().strip()
        pwd = self.password.get()
        conf = self.confirm.get()
        if not uname or not pwd:
            messagebox.showerror("Error", "Username and password required.")
            return
        if pwd != conf:
            messagebox.showerror("Error", "Passwords do not match.")
            return
        uname_key = uname.lower()
        if self.db.user_exists(uname_key):
            messagebox.showwarning("Exists", "Username already taken.")
            return
        pwd_hash = hashlib.sha256(pwd.encode()).hexdigest()
        res = self.db.add_user(uname_key, pwd_hash, is_admin=0)
        if res:
            # fetch what was stored for debugging/confirmation
            stored = self.db.get_user(uname_key)
            if stored:
                msg = f"Stored username: {stored[1]}\nAdmin flag: {stored[3]}"
            else:
                msg = "Account created but could not verify stored record."
            messagebox.showinfo("Success", "Account created. You can now login.\n\n")
            self.parent.show_page("Login")
        else:
            messagebox.showerror("Error", "Could not create account.")
