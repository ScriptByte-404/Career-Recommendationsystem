import tkinter as tk
from tkinter import messagebox
import hashlib
from PIL import Image, ImageTk
from ui_utils import AnimatedBubbleBackground, create_navbar

class LoginPage(tk.Frame):
    def __init__(self, parent, db):
        super().__init__(parent, bg="#F4F6FB")  # Page Background
        self.parent = parent
        self.db = db

        # Add animated bubble background
        self.bubble_bg = AnimatedBubbleBackground(self, bg_color="#F4F6FB")

        # Create navbar
        create_navbar(self, "Login - Access Your Account")

        # Card
        card = tk.Frame(self, bg="#FFFFFF", padx=30, pady=30, relief="raised", bd=2)
        card.place(relx=0.5, rely=0.5, anchor="center", width=400)

        title = tk.Label(card, text="🔐 Welcome Back", font=("Segoe UI", 26, "bold"), fg="#1E293B", bg="#FFFFFF")
        title.pack(pady=15)

        # Image
        try:
            img = Image.open("images/login.png")
            img = img.resize((80,80))
            photo = ImageTk.PhotoImage(img)
            img_label = tk.Label(card, image=photo, bg="#FFFFFF")
            img_label.image = photo
            img_label.pack(pady=10)
        except:
            pass

        tk.Label(card, text="Sign in to continue", font=("Segoe UI", 12), fg="#475569", bg="#FFFFFF").pack(pady=(0,20))

        tk.Label(card, text="👤 Username", font=("Segoe UI", 13, "bold"), fg="#1E293B", bg="#FFFFFF").pack(anchor="w", pady=(5,2), padx=15)
        self.username = tk.Entry(card, font=("Segoe UI", 12), relief="flat", bd=1, bg="#F4F6FB", width=30)
        self.username.pack(pady=5, fill="x", padx=15)

        tk.Label(card, text="🔒 Password", font=("Segoe UI", 13, "bold"), fg="#1E293B", bg="#FFFFFF").pack(anchor="w", pady=(10,2), padx=15)
        self.password = tk.Entry(card, show="*", font=("Segoe UI", 12), relief="flat", bd=1, bg="#F4F6FB", width=30)
        self.password.pack(pady=5, fill="x", padx=15)

        login_btn = tk.Button(card, text="🔓 Login", font=("Segoe UI", 16, "bold"), bg="#0284C7", fg="white", padx=20, pady=11, command=self.login)
        login_btn.pack(pady=25)
        login_btn.bind("<Enter>", lambda e: login_btn.config(bg="#0EA5E9"))
        login_btn.bind("<Leave>", lambda e: login_btn.config(bg="#0284C7"))

        back_btn = tk.Button(card, text="← Back", bg="#FFFFFF", fg="#0B3C6D", relief="flat", command=lambda: self.parent.show_page("Welcome"))
        back_btn.pack(pady=(8,0))

    def clear_fields(self):
        self.username.delete(0, tk.END)
        self.password.delete(0, tk.END)

    def login(self):
        raw_username = self.username.get().strip()
        username = raw_username.lower()
        password = self.password.get()
        # admin demo credentials (kept for quick access)
        if username == "admin" and password == "1234":
            self.parent.current_username = raw_username or "Admin"
            self.parent.show_page("Admin")
            return

        # check users table
        user_row = self.db.get_user(username)
        if not user_row:
            messagebox.showerror("❌ Error", "Invalid credentials or no such user.")
            return
        stored_hash = user_row[2]
        entered_hash = hashlib.sha256(password.encode()).hexdigest()
        if entered_hash == stored_hash:
            self.parent.current_username = raw_username or user_row[1]
            # if user is admin flag set in DB, route to Admin otherwise Dashboard
            is_admin = bool(user_row[3])
            if is_admin:
                self.parent.show_page("Admin")
            else:
                self.parent.show_page("Dashboard")
        else:
            messagebox.showerror("❌ Error", "Invalid credentials")
