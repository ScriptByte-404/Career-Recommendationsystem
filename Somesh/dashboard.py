import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

from ui_utils import create_navbar, create_stat_card


class DashboardPage(tk.Frame):
    def __init__(self, parent, db):
        super().__init__(parent, bg="#EAF3FB")
        self.parent = parent
        self.db = db
        self.hero_photo = None

        create_navbar(self, "Dashboard - Student Career System")

        self.main_container = tk.Frame(self, bg="#EAF3FB", padx=24, pady=20)
        self.main_container.pack(fill="both", expand=True)

        self._build_hero_section()
        self._build_stats_section()
        self._build_description_section()
        self._build_actions_section()
        self._build_footer_section()

    def _build_hero_section(self):
        hero = tk.Frame(self.main_container, bg="#FFFFFF", padx=24, pady=20, relief="ridge", bd=1)
        hero.pack(fill="x", pady=(0, 16))

        text_col = tk.Frame(hero, bg="#FFFFFF")
        text_col.pack(side="left", fill="both", expand=True)

        header_row = tk.Frame(text_col, bg="#FFFFFF")
        header_row.pack(fill="x")

        tk.Label(
            header_row,
            text="Build Your Future with Confidence",
            font=("Segoe UI", 26, "bold"),
            fg="#0B3C6D",
            bg="#FFFFFF",
            anchor="w",
            justify="left",
        ).pack(side="left", anchor="w")

        self._build_user_profile_block(hero)

        tk.Label(
            text_col,
            text=(
                "The Student Career System helps you choose a career path using your "
                "education, skills, and interests. Start your evaluation to receive a "
                "clear and practical recommendation."
            ),
            font=("Segoe UI", 12),
            fg="#3A4A5A",
            bg="#FFFFFF",
            wraplength=620,
            justify="left",
            anchor="w",
        ).pack(anchor="w", pady=(10, 0))

        image_col = tk.Frame(hero, bg="#FFFFFF")
        image_col.pack(side="right", padx=(16, 0))
        self._render_hero_image(image_col)

    def _build_user_profile_block(self, parent):
        profile = tk.Canvas(parent, width=250, height=74, bg="#FFFFFF", highlightthickness=0)
        profile.place(relx=1.0, x=-12, y=10, anchor="ne")

        profile.create_arc((4, 4, 22, 22), start=90, extent=90, fill="#F8FBFF", outline="#BFD7EE")
        profile.create_arc((228, 4, 246, 22), start=0, extent=90, fill="#F8FBFF", outline="#BFD7EE")
        profile.create_arc((4, 52, 22, 70), start=180, extent=90, fill="#F8FBFF", outline="#BFD7EE")
        profile.create_arc((228, 52, 246, 70), start=270, extent=90, fill="#F8FBFF", outline="#BFD7EE")
        profile.create_rectangle(13, 4, 237, 70, fill="#F8FBFF", outline="#BFD7EE")
        profile.create_rectangle(4, 13, 246, 61, fill="#F8FBFF", outline="#BFD7EE")

        username = getattr(self.parent, "current_username", "User")
        initial = username[0].upper() if username else "U"
        avatar = tk.Canvas(profile, width=40, height=40, bg="#F8FBFF", highlightthickness=0)
        avatar.create_oval(2, 2, 38, 38, fill="#DCEBFA", outline="#0F6CBD", width=2)
        avatar.create_text(20, 22, text=initial, fill="#0B3C6D", font=("Segoe UI", 12, "bold"))
        profile.create_window(24, 37, window=avatar)

        user_col = tk.Frame(profile, bg="#F8FBFF")
        tk.Label(
            user_col,
            text="Logged in as",
            font=("Segoe UI", 9),
            fg="#64748B",
            bg="#F8FBFF",
            anchor="w",
        ).pack(anchor="w")
        tk.Label(
            user_col,
            text=username,
            font=("Segoe UI", 12, "bold"),
            fg="#0B3C6D",
            bg="#F8FBFF",
            anchor="w",
        ).pack(anchor="w")
        profile.create_window(62, 37, anchor="w", window=user_col)

    def _render_hero_image(self, parent):
        image_path = os.path.join(os.path.dirname(__file__), "images", "student.png")

        try:
            img = Image.open(image_path).convert("RGB")
            img = img.resize((300, 220), Image.Resampling.LANCZOS)
            self.hero_photo = ImageTk.PhotoImage(img)
            tk.Label(parent, image=self.hero_photo, bg="#FFFFFF", relief="flat").pack()
        except Exception:
            tk.Label(
                parent,
                text="Student Career Image",
                font=("Segoe UI", 12, "bold"),
                fg="#0B3C6D",
                bg="#DCEBFA",
                width=30,
                height=12,
                relief="flat",
            ).pack()

    def _build_stats_section(self):
        stats_wrapper = tk.Frame(self.main_container, bg="#EAF3FB")
        stats_wrapper.pack(fill="x", pady=(0, 14))

        stats = [
            {"icon": "Students", "title": "High School Students", "value": "500K+", "description": "Across Nepal"},
            {"icon": "Risk", "title": "Youth Unemployment", "value": "25%", "description": "Needs guidance"},
            {"icon": "Success", "title": "Career Placement", "value": "75%", "description": "With proper planning"},
        ]

        for idx, stat in enumerate(stats):
            card = create_stat_card(
                stats_wrapper,
                stat["title"],
                stat["value"],
                stat["icon"],
            )
            card.grid(row=0, column=idx, padx=6, sticky="ew")
            tk.Label(
                card,
                text=stat["description"],
                font=("Segoe UI", 9),
                fg="#4E5D6C",
                bg="#FFFFFF",
            ).pack(pady=(2, 0))
            stats_wrapper.grid_columnconfigure(idx, weight=1)

    def _build_description_section(self):
        card = tk.Frame(self.main_container, bg="#FFFFFF", padx=20, pady=16, relief="ridge", bd=1)
        card.pack(fill="x", pady=(0, 14))

        tk.Label(
            card,
            text="Why This Dashboard Matters",
            font=("Segoe UI", 16, "bold"),
            fg="#0B3C6D",
            bg="#FFFFFF",
        ).pack(anchor="w")

        tk.Label(
            card,
            text=(
                "Many students face uncertainty after graduation. This dashboard gives you "
                "a simple path: complete the evaluation, review recommendations, and move "
                "forward with a stronger career plan."
            ),
            font=("Segoe UI", 11),
            fg="#3A4A5A",
            bg="#FFFFFF",
            wraplength=980,
            justify="left",
        ).pack(anchor="w", pady=(8, 0))

    def _build_actions_section(self):
        actions = tk.Frame(self.main_container, bg="#EAF3FB")
        actions.pack(fill="x", pady=(0, 14))

        logout_btn = tk.Button(
            actions,
            text="Logout",
            font=("Segoe UI", 12, "bold"),
            bg="#FFFFFF",
            fg="#0B3C6D",
            activebackground="#E8F1FA",
            activeforeground="#0B3C6D",
            relief="ridge",
            bd=1,
            padx=20,
            pady=10,
            command=self.logout,
            cursor="hand2",
        )
        logout_btn.pack(side="left")

        primary = tk.Button(
            actions,
            text="Get Started",
            font=("Segoe UI", 14, "bold"),
            bg="#0F6CBD",
            fg="#FFFFFF",
            activebackground="#0C5A9F",
            activeforeground="#FFFFFF",
            relief="flat",
            padx=28,
            pady=12,
            command=self.start_evaluation,
            cursor="hand2",
        )
        primary.pack(side="right")

    def _build_footer_section(self):
        footer = tk.Frame(self.main_container, bg="#EAF3FB")
        footer.pack(fill="x")

    def start_evaluation(self):
        self.parent.show_page("EvaluationOverview")

    def logout(self):
        if not messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?"):
            return
        self.parent.current_username = "User"
        self.parent.current_student_id = None
        self.parent.temp_data = {}
        login_page = self.parent.pages.get("Login")
        if login_page is not None and hasattr(login_page, "clear_fields"):
            login_page.clear_fields()
        self.parent.show_page("Login")
