import tkinter as tk
from PIL import Image, ImageTk
from ui_utils import AnimatedBubbleBackground, create_navbar


class ThankYouPage(tk.Frame):
    def __init__(self, parent, db):
        super().__init__(parent, bg="#F4F6FB")  # Sky Blue Theme Background
        self.parent = parent
        self.db = db

        # Add animated bubble background
        self.bubble_bg = AnimatedBubbleBackground(self, bg_color="#F4F6FB")

        # Create navbar
        create_navbar(self, "Success! Your Future Journey Begins")

        # Main content
        main_frame = tk.Frame(self, bg="#F4F6FB")
        main_frame.pack(fill="both", expand=True, padx=20, pady=16)

        # Success card
        success_card = tk.Frame(main_frame, bg="#FFFFFF", padx=24, pady=20, relief="raised", bd=2)
        success_card.pack(expand=True)

        # Success icon and title
        header_frame = tk.Frame(success_card, bg="#FFFFFF")
        header_frame.pack(pady=(0, 12))

        tk.Label(header_frame, text="\U0001F389", font=("Segoe UI", 36), bg="#FFFFFF").pack()
        tk.Label(
            success_card,
            text="Congratulations!",
            font=("Segoe UI", 22, "bold"),
            fg="#1E293B",
            bg="#FFFFFF",
        ).pack(pady=(0, 6))
        tk.Label(
            success_card,
            text="You've Reached the End of Step 4 - Know Your Future!",
            font=("Segoe UI", 14),
            fg="#0284C7",
            bg="#FFFFFF",
        ).pack(pady=(0, 14))

        # Success image
        try:
            img = Image.open("images/success.png")
            img = img.resize((130, 130))
            photo = ImageTk.PhotoImage(img)
            img_label = tk.Label(success_card, image=photo, bg="#FFFFFF")
            img_label.image = photo
            img_label.pack(pady=(0, 14))
        except Exception:
            tk.Label(
                success_card,
                text="\u2705",
                font=("Segoe UI", 62),
                bg="#FFFFFF",
                fg="#22C55E",
            ).pack(pady=(0, 14))

        # Message
        message_frame = tk.Frame(success_card, bg="#F4F6FB", padx=16, pady=12, relief="raised", bd=1)
        message_frame.pack(fill="x", pady=(0, 16))

        tk.Label(
            message_frame,
            text="\U0001F31F Your Career Path is Clear Now!",
            font=("Segoe UI", 13, "bold"),
            fg="#1E293B",
            bg="#F4F6FB",
        ).pack(pady=(0, 8))

        inspirational_text = """Many students face unemployment due to lack of direction. With dedication, education, and the right career choice, you can transform your future.

Education is the bridge from poverty to success. Your journey towards a fulfilling career starts today!

Remember: Success comes to those who are prepared and persistent. Keep learning, keep growing!"""

        tk.Label(
            message_frame,
            text=inspirational_text,
            font=("Segoe UI", 10),
            fg="#475569",
            bg="#F4F6FB",
            wraplength=520,
            justify="center",
        ).pack(pady=(0, 8))

        # Action buttons
        btn_frame = tk.Frame(success_card, bg="#FFFFFF")
        btn_frame.pack(pady=10)

        dashboard_btn = tk.Button(
            btn_frame,
            text="\U0001F3E0 Go to Dashboard",
            font=("Segoe UI", 11, "bold"),
            bg="#0284C7",
            fg="white",
            padx=12,
            pady=7,
            command=self.go_dashboard,
        )
        dashboard_btn.pack(side="left", padx=10)
        dashboard_btn.bind("<Enter>", lambda e: dashboard_btn.config(bg="#0369A1"))
        dashboard_btn.bind("<Leave>", lambda e: dashboard_btn.config(bg="#0284C7"))

        exit_btn = tk.Button(
            btn_frame,
            text="\U0001F6AA Exit",
            font=("Segoe UI", 12, "bold"),
            bg="#EF4444",
            fg="white",
            padx=14,
            pady=8,
            command=self.parent.destroy,
        )
        exit_btn.pack(side="left", padx=10)
        exit_btn.bind("<Enter>", lambda e: exit_btn.config(bg="#DC2626"))
        exit_btn.bind("<Leave>", lambda e: exit_btn.config(bg="#EF4444"))

    def new_evaluation(self):
        # Reset evaluation state and cached evaluation pages.
        self.parent.reset_evaluation_flow()
        self.parent.show_page("Dashboard")

    def go_dashboard(self):
        self.new_evaluation()
