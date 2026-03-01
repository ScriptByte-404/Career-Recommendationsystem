import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from ui_utils import AnimatedBubbleBackground, create_navbar

class WelcomePage(tk.Frame):
    def __init__(self, parent, db):
        super().__init__(parent, bg="#F4F6FB")  # Page Background
        self.parent = parent
        self.db = db

        # Add animated bubble background
        self.bubble_bg = AnimatedBubbleBackground(self, bg_color="#F4F6FB")

        # Create navbar
        create_navbar(self, "Welcome - Career Discovery System")

        # Main container
        main_frame = tk.Frame(self, bg="#F4F6FB")
        main_frame.pack(fill="both", expand=True, padx=40, pady=40)

        # Left side - Big image
        left_frame = tk.Frame(main_frame, bg="#F4F6FB")
        left_frame.pack(side="left", fill="y", padx=(0,40))

        try:
            img = Image.open("images/student.png")
            img = img.resize((380,450))
            photo = ImageTk.PhotoImage(img)
            img_label = tk.Label(left_frame, image=photo, bg="#F4F6FB")
            img_label.image = photo
            img_label.pack()
        except:
            tk.Label(left_frame, text="🎓", font=("Segoe UI", 160), bg="#F4F6FB", fg="#0284C7").pack()

        # Right side - Content
        right_frame = tk.Frame(main_frame, bg="#F4F6FB")
        right_frame.pack(side="right", fill="both", expand=True)

        # Title
        title = tk.Label(right_frame, text="🎓 Welcome to\nCareer Advisor", font=("Segoe UI", 40, "bold"), fg="#1E293B", bg="#F4F6FB", justify="left")
        title.pack(pady=(20,20), anchor="w")

        # Interactive description
        desc_frame = tk.Frame(right_frame, bg="#FFFFFF", padx=25, pady=25, relief="raised", bd=1)
        desc_frame.pack(fill="x", pady=(0,30))

        tk.Label(desc_frame, text="🚀 Your Future Starts Here!", font=("Segoe UI", 18, "bold"), fg="#0284C7", bg="#FFFFFF").pack(anchor="w", pady=(0,10))

        desc_text = """✨ Discover your perfect career path 
🔍 Get recommendations
🎯 Personalized guidance
📊 Market-based insights"""

        tk.Label(desc_frame, text=desc_text, font=("Segoe UI", 13), fg="#475569", bg="#FFFFFF", justify="left").pack(anchor="w")

        # Interactive buttons
        btn_frame = tk.Frame(right_frame, bg="#F4F6FB")
        btn_frame.pack(pady=25)

        # Main CTA button
        main_btn = tk.Button(btn_frame, text="🚀 Get Started Now", font=("Segoe UI", 18, "bold"), bg="#0284C7", fg="white", padx=25, pady=12, command=self.next_page)
        main_btn.pack(pady=(0,12))
        main_btn.bind("<Enter>", lambda e: main_btn.config(bg="#0EA5E9"))
        main_btn.bind("<Leave>", lambda e: main_btn.config(bg="#0284C7"))

        # Sign Up button
        signup_btn = tk.Button(btn_frame, text="✏️ Sign Up Here", font=("Segoe UI", 14, "bold"), bg="#075985", fg="white", padx=20, pady=10, command=self.sign_up)
        signup_btn.pack(pady=(0,12))
        signup_btn.bind("<Enter>", lambda e: signup_btn.config(bg="#0EA5E9"))
        signup_btn.bind("<Leave>", lambda e: signup_btn.config(bg="#075985"))

        # Secondary buttons  
        secondary_frame = tk.Frame(btn_frame, bg="#F4F6FB")
        secondary_frame.pack()

        learn_btn = tk.Button(secondary_frame, text="ℹ️ Learn More", font=("Segoe UI", 12), bg="#FFFFFF", fg="#0284C7", relief="solid", bd=1, padx=18, pady=6, command=self.show_info)
        learn_btn.pack(side="left", padx=8)
        learn_btn.bind("<Enter>", lambda e: learn_btn.config(bg="#E0F2FE"))
        learn_btn.bind("<Leave>", lambda e: learn_btn.config(bg="#FFFFFF"))

        contact_btn = tk.Button(secondary_frame, text="📞 Contact", font=("Segoe UI", 12), bg="#FFFFFF", fg="#0284C7", relief="solid", bd=1, padx=18, pady=6, command=self.show_contact)
        contact_btn.pack(side="left", padx=8)
        contact_btn.bind("<Enter>", lambda e: contact_btn.config(bg="#E0F2FE"))
        contact_btn.bind("<Leave>", lambda e: contact_btn.config(bg="#FFFFFF"))

        # Stats preview
        stats_frame = tk.Frame(right_frame, bg="#F4F6FB")
        stats_frame.pack(pady=(20,0))

        stats_data = [
            ("👥", "500K+", "Guided"),
            ("🎯", "95%", "Success"),
            ("💼", "50+", "Paths")
        ]

        for icon, number, text in stats_data:
            stat_card = tk.Frame(stats_frame, bg="#FFFFFF", padx=12, pady=8, relief="raised", bd=1)
            stat_card.pack(side="left", padx=4)
            tk.Label(stat_card, text=icon, font=("Segoe UI", 20), bg="#FFFFFF").pack()
            tk.Label(stat_card, text=number, font=("Segoe UI", 14, "bold"), fg="#0284C7", bg="#FFFFFF").pack()
            tk.Label(stat_card, text=text, font=("Segoe UI", 9), fg="#475569", bg="#FFFFFF").pack()

    def next_page(self):
        self.parent.show_page("Login")

    def sign_up(self):
        # Route to the app's Signup page which stores credentials in the DB
        self.parent.show_page("Signup")

    def show_info(self):
        info_window = tk.Toplevel(self)
        info_window.title("About Our System")
        info_window.geometry("500x400")
        info_window.configure(bg="#F4F6FB")

        tk.Label(info_window, text="🎓 About Career System", font=("Segoe UI", 18, "bold"), fg="#1E293B", bg="#F4F6FB").pack(pady=20)

        info_text = """Our system helps you:

• Discover perfect career paths
• Get personalized recommendations
• Understand market demands
• Plan your future growth

Join thousands finding success!"""

        tk.Label(info_window, text=info_text, font=("Segoe UI", 12), fg="#475569", bg="#F4F6FB", justify="left", wraplength=450).pack(pady=10)

        close_btn = tk.Button(info_window, text="Got it!", font=("Segoe UI", 14, "bold"), bg="#0284C7", fg="white", command=info_window.destroy)
        close_btn.pack(pady=20)
        close_btn.bind("<Enter>", lambda e: close_btn.config(bg="#0EA5E9"))
        close_btn.bind("<Leave>", lambda e: close_btn.config(bg="#0284C7"))

    def show_contact(self):
        contact_window = tk.Toplevel(self)
        contact_window.title("Contact Us")
        contact_window.geometry("400x300")
        contact_window.configure(bg="#F4F6FB")

        tk.Label(contact_window, text="📞 Get in Touch", font=("Segoe UI", 18, "bold"), fg="#1E293B", bg="#F4F6FB").pack(pady=20)

        contact_info = """📧 support@careerrec.com
📱 +977-123456789
🌐 careerrec.com

We're here to help!"""

        tk.Label(contact_window, text=contact_info, font=("Segoe UI", 12), fg="#475569", bg="#F4F6FB", justify="left").pack(pady=10)

        close_btn = tk.Button(contact_window, text="Close", font=("Segoe UI", 14, "bold"), bg="#0284C7", fg="white", command=contact_window.destroy)
        close_btn.pack(pady=20)
        close_btn.bind("<Enter>", lambda e: close_btn.config(bg="#0EA5E9"))
        close_btn.bind("<Leave>", lambda e: close_btn.config(bg="#0284C7"))
