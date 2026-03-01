"""All evaluation flow pages in one module.

Contains:
- EvaluationOverviewPage
- PersonalInfoPage
- EducationPage
- InterestsSkillsPage
- RecommendationPage
"""
import tkinter as tk

from ui_utils import AnimatedBubbleBackground, create_navbar, create_step_tracker


class EvaluationOverviewPage(tk.Frame):
    def __init__(self, parent, db):
        super().__init__(parent, bg="#F4F6FB")
        self.parent = parent
        self.db = db

        self.bubble_bg = AnimatedBubbleBackground(self, bg_color="#F4F6FB")
        create_navbar(self, "Evaluation Steps - Begin Your Journey")

        main_frame = tk.Frame(self, bg="#F4F6FB")
        main_frame.pack(fill="both", expand=True, padx=20, pady=16)

        title_card = tk.Frame(main_frame, bg="#FFFFFF", padx=20, pady=14, relief="ridge", bd=1)
        title_card.pack(fill="x", pady=(0, 12))
        tk.Label(
            title_card,
            text="Evaluation Process Overview",
            font=("Segoe UI", 22, "bold"),
            fg="#1E293B",
            bg="#FFFFFF",
        ).pack()
        tk.Label(
            title_card,
            text="Follow the steps below to get your career recommendation.",
            font=("Segoe UI", 11),
            fg="#475569",
            bg="#FFFFFF",
        ).pack(pady=(4, 0))

        steps_frame = tk.Frame(main_frame, bg="#F4F6FB")
        steps_frame.pack(fill="x", pady=(0, 10))

        steps = [
            ("Step 1", "Personal Information", "Enter name, age, gender, and contact details."),
            ("Step 2", "Educational Details", "Add stream, performance, and grade."),
            ("Step 3", "Interests & Skills", "Select your interests and your strongest skills."),
            ("Step 4", "Recommendation", "Get a career path based on your full profile."),
        ]

        for idx, (step_num, title, desc) in enumerate(steps):
            card = tk.Frame(steps_frame, bg="#FFFFFF", padx=16, pady=14, relief="ridge", bd=1)
            card.grid(row=idx // 2, column=idx % 2, padx=6, pady=6, sticky="nsew")

            tk.Label(
                card,
                text=step_num,
                font=("Segoe UI", 10, "bold"),
                fg="#0F6CBD",
                bg="#E8F1FA",
                padx=8,
                pady=4,
            ).pack(anchor="w", pady=(0, 8))

            tk.Label(
                card,
                text=title,
                font=("Segoe UI", 14, "bold"),
                fg="#1E293B",
                bg="#FFFFFF",
            ).pack(anchor="w")

            tk.Label(
                card,
                text=desc,
                font=("Segoe UI", 10),
                fg="#475569",
                bg="#FFFFFF",
                wraplength=420,
                justify="left",
            ).pack(anchor="w", pady=(6, 0))

        steps_frame.grid_columnconfigure(0, weight=1)
        steps_frame.grid_columnconfigure(1, weight=1)

        info_frame = tk.Frame(main_frame, bg="#FFFFFF", padx=12, pady=10, relief="ridge", bd=1)
        info_frame.pack(fill="x")
        tk.Label(
            info_frame,
            text="Each step takes 1-2 minutes. Complete the form sections to move forward.",
            font=("Segoe UI", 10),
            fg="#475569",
            bg="#FFFFFF",
        ).pack(anchor="w")

        actions_row = tk.Frame(main_frame, bg="#F4F6FB")
        actions_row.pack(fill="x", pady=(10, 0))

        back_btn = tk.Button(
            actions_row,
            text="Back",
            font=("Segoe UI", 15, "bold"),
            bg="#E5E7EB",
            fg="#475569",
            activebackground="#D1D5DB",
            activeforeground="#334155",
            padx=28,
            pady=10,
            relief="flat",
            command=lambda: self.parent.show_page("Dashboard"),
            cursor="hand2",
        )
        back_btn.pack(side="left")

        start_btn = tk.Button(
            actions_row,
            text="Start Now",
            font=("Segoe UI", 15, "bold"),
            bg="#0F6CBD",
            fg="#FFFFFF",
            activebackground="#0C5A9F",
            activeforeground="#FFFFFF",
            padx=28,
            pady=10,
            relief="flat",
            command=lambda: self.parent.show_page("PersonalInfo"),
            cursor="hand2",
        )
        start_btn.pack(side="right")


import tkinter as tk
from tkinter import ttk, messagebox
from ui_utils import AnimatedBubbleBackground, create_navbar, create_step_tracker

class PersonalInfoPage(tk.Frame):
    def __init__(self, parent, db):
        super().__init__(parent, bg="#F4F6FB")  # Page Background
        self.parent = parent
        self.db = db

        # Add animated bubble background
        self.bubble_bg = AnimatedBubbleBackground(self, bg_color="#F4F6FB")

        # Create navbar
        create_navbar(self, "Step 1 - Personal Information")
        create_step_tracker(self, 1, ["Personal Info", "Education", "Interests & Skills", "Recommendation"])

        # Main content
        main_frame = tk.Frame(self, bg="#F4F6FB")
        main_frame.pack(fill="both", expand=True, padx=16, pady=(10, 10))

        # Title in rectangular box
        title_frame = tk.Frame(main_frame, bg="#FFFFFF", padx=30, pady=20, relief="raised", bd=2)
        title_frame.pack(fill="x", pady=(0,30))

        tk.Label(title_frame, text="👤 First Step to Know Your Future", font=("Segoe UI", 24, "bold"), fg="#1E293B", bg="#FFFFFF").pack()
        tk.Label(title_frame, text="Let's start by getting to know you better", font=("Segoe UI", 14), fg="#475569", bg="#FFFFFF").pack(pady=(5,0))

        # Form card
        card = tk.Frame(main_frame, bg="#FFFFFF", padx=40, pady=15, relief="raised", bd=1)
        card.pack(fill="both", expand=True)

        # Form title
        form_header = tk.Frame(card, bg="#FFFFFF")
        form_header.pack(fill="x", pady=(0, 25))
        tk.Label(form_header, text="Personal Information", font=("Segoe UI", 22, "bold"), fg="#1E293B", bg="#FFFFFF").pack(side="left")

        # Form fields in two columns
        form_frame = tk.Frame(card, bg="#FFFFFF")
        form_frame.pack(fill="x")

        # Left column
        left_frame = tk.Frame(form_frame, bg="#FFFFFF")
        left_frame.pack(side="left", fill="both", expand=True, padx=(0, 20))

        # Full Name
        name_frame = tk.Frame(left_frame, bg="#FFFFFF")
        name_frame.pack(fill="x", pady=(0, 20))
        tk.Label(name_frame, text="Full Name", font=("Segoe UI", 14, "bold"), fg="#1E293B", bg="#FFFFFF").pack(anchor="w", pady=(0, 5))
        self.name = tk.Entry(name_frame, font=("Segoe UI", 14), relief="flat", bd=1, bg="#F4F6FB", width=30)
        self.name.pack(fill="x")

        # Age
        age_frame = tk.Frame(left_frame, bg="#FFFFFF")
        age_frame.pack(fill="x", pady=(0, 20))
        tk.Label(age_frame, text="Age", font=("Segoe UI", 14, "bold"), fg="#1E293B", bg="#FFFFFF").pack(anchor="w", pady=(0, 5))
        self.age = tk.Entry(age_frame, font=("Segoe UI", 14), relief="flat", bd=1, bg="#F4F6FB", width=30)
        self.age.pack(fill="x")

        # Gender
        gender_frame = tk.Frame(left_frame, bg="#FFFFFF")
        gender_frame.pack(fill="x", pady=(0, 20))
        tk.Label(gender_frame, text="Gender", font=("Segoe UI", 14, "bold"), fg="#1E293B", bg="#FFFFFF").pack(anchor="w", pady=(0, 5))
        self.gender = ttk.Combobox(gender_frame, values=["Male", "Female", "Other"], font=("Segoe UI", 14), state="readonly")
        self.gender.set("Select Gender")
        self.gender.pack(fill="x")

        # Right column
        right_frame = tk.Frame(form_frame, bg="#FFFFFF")
        right_frame.pack(side="right", fill="both", expand=True)

        # Contact
        contact_frame = tk.Frame(right_frame, bg="#FFFFFF")
        contact_frame.pack(fill="x", pady=(0, 20))
        tk.Label(contact_frame, text="Contact (Optional)", font=("Segoe UI", 14, "bold"), fg="#1E293B", bg="#FFFFFF").pack(anchor="w", pady=(0, 5))
        self.contact = tk.Entry(contact_frame, font=("Segoe UI", 14), relief="flat", bd=1, bg="#F4F6FB", width=30)
        self.contact.pack(fill="x")

        # Navigation footer in main frame so buttons are always visible.
        btn_frame = tk.Frame(main_frame, bg="#F4F6FB")
        btn_frame.pack(side="bottom", fill="x", pady=(6, 0))

        prev_btn = tk.Button(
            btn_frame,
            text="Previous",
            font=("Segoe UI", 22, "bold"),
            bg="#E5E7EB",
            fg="#475569",
            padx=52,
            pady=18,
            width=16,
            relief="flat",
            cursor="hand2",
            command=self.previous,
        )
        prev_btn.pack(side="left", padx=20)
        prev_btn.bind("<Enter>", lambda e: prev_btn.config(bg="#D1D5DB"))
        prev_btn.bind("<Leave>", lambda e: prev_btn.config(bg="#E5E7EB"))

        next_btn = tk.Button(
            btn_frame,
            text="Next",
            font=("Segoe UI", 22, "bold"),
            bg="#0284C7",
            fg="white",
            padx=52,
            pady=18,
            width=16,
            relief="flat",
            cursor="hand2",
            command=self.next_page,
        )
        next_btn.pack(side="right", padx=20)
        next_btn.bind("<Enter>", lambda e: next_btn.config(bg="#0EA5E9"))
        next_btn.bind("<Leave>", lambda e: next_btn.config(bg="#0284C7"))

    def validate(self):
        """Validate form inputs"""
        if not self.name.get().strip() or not self.name.get().isalpha():
            messagebox.showerror("Error", "Please enter your valid name")
            return False
        if not self.age.get().strip() or not self.age.get().isdigit or not len(self.age.get())==2:
            messagebox.showerror("Error", "Please enter your valid age")
            return False
        if self.gender.get() == "Select Gender":
            messagebox.showerror("Error", "Please select your gender")
            return False
        return True
    def previous(self):
        """Navigate to previous page"""
        self.save_data()
        self.parent.show_page("EvaluationOverview")

    def next_page(self):
        """Navigate to next page"""
        if self.validate():
            if self.save_data():
                self.parent.show_page("Education")

    def save_data(self):
        """Save personal info for later steps."""
        data = {
            "name": self.name.get().strip(),
            "age": self.age.get().strip(),
            "gender": self.gender.get(),
            "contact": self.contact.get().strip(),
        }
        self.parent.temp_data.update(data)
        return True



import tkinter as tk
from tkinter import ttk, messagebox
from ui_utils import AnimatedBubbleBackground, create_navbar, create_step_tracker

class EducationPage(tk.Frame):
    def __init__(self, parent, db):
        super().__init__(parent, bg="#F4F6FB")  # Page Background
        self.parent = parent
        self.db = db

        # Add animated bubble background
        self.bubble_bg = AnimatedBubbleBackground(self, bg_color="#F4F6FB")

        # Create navbar
        create_navbar(self, "Step 2 - Educational Details")
        create_step_tracker(self, 2, ["Personal Info", "Education", "Interests & Skills", "Recommendation"])

        # Main content
        main_frame = tk.Frame(self, bg="#F4F6FB")
        main_frame.pack(fill="both", expand=True, padx=16, pady=(10, 10))

        # Reserve footer space first so navigation buttons stay visible.
        btn_frame = tk.Frame(main_frame, bg="#F4F6FB")
        btn_frame.pack(side="bottom", fill="x", pady=(8, 0))

        prev_btn = tk.Button(
            btn_frame,
            text="Previous",
            font=("Segoe UI", 22, "bold"),
            bg="#E5E7EB",
            fg="#475569",
            padx=52,
            pady=18,
            width=16,
            relief="flat",
            cursor="hand2",
            command=self.previous,
        )
        prev_btn.pack(side="left", padx=20)
        prev_btn.bind("<Enter>", lambda e: prev_btn.config(bg="#D1D5DB"))
        prev_btn.bind("<Leave>", lambda e: prev_btn.config(bg="#E5E7EB"))

        next_btn = tk.Button(
            btn_frame,
            text="Next",
            font=("Segoe UI", 22, "bold"),
            bg="#0284C7",
            fg="white",
            padx=52,
            pady=18,
            width=16,
            relief="flat",
            cursor="hand2",
            command=self.next_page,
        )
        next_btn.pack(side="right", padx=20)
        next_btn.bind("<Enter>", lambda e: next_btn.config(bg="#0EA5E9"))
        next_btn.bind("<Leave>", lambda e: next_btn.config(bg="#0284C7"))

        # Title in rectangular box
        title_frame = tk.Frame(main_frame, bg="#FFFFFF", padx=30, pady=20, relief="raised", bd=2)
        title_frame.pack(fill="x", pady=(0,30))

        tk.Label(title_frame, text="🎓 Second Step - Educational Background", font=("Segoe UI", 24, "bold"), fg="#1E293B", bg="#FFFFFF").pack()
        tk.Label(title_frame, text="Tell us about your academic journey", font=("Segoe UI", 14), fg="#475569", bg="#FFFFFF").pack(pady=(5,0))

        # Form card
        card = tk.Frame(main_frame, bg="#FFFFFF", padx=40, pady=40, relief="raised", bd=1)
        card.pack(fill="both", expand=True)

        # Form title with icon
        form_header = tk.Frame(card, bg="#FFFFFF")
        form_header.pack(fill="x", pady=(0,25))

        tk.Label(form_header, text="📚", font=("Segoe UI", 28), bg="#FFFFFF").pack(side="left")
        tk.Label(form_header, text="Academic Information", font=("Segoe UI", 22, "bold"), fg="#1E293B", bg="#FFFFFF").pack(side="left", padx=(15,0))

        # Form fields in two columns
        form_frame = tk.Frame(card, bg="#FFFFFF")
        form_frame.pack(fill="x")

        # Left column
        left_frame = tk.Frame(form_frame, bg="#FFFFFF")
        left_frame.pack(side="left", fill="both", expand=True, padx=(0,40))

        # Stream selection
        stream_frame = tk.Frame(left_frame, bg="#FFFFFF")
        stream_frame.pack(fill="x", pady=(0,20))
        tk.Label(stream_frame, text="🎯 Academic Stream", font=("Segoe UI", 14, "bold"), fg="#1E293B", bg="#FFFFFF").pack(anchor="w", pady=(0,5))
        self.stream = ttk.Combobox(stream_frame, values=["Science", "Management", "Humanities", "Arts"], font=("Segoe UI", 14), state="readonly")
        self.stream.pack(fill="x")

        # Right column
        right_frame = tk.Frame(form_frame, bg="#FFFFFF")
        right_frame.pack(side="right", fill="both", expand=True)

        # Percentage/GPA
        percentage_frame = tk.Frame(right_frame, bg="#FFFFFF")
        percentage_frame.pack(fill="x", pady=(0,20))
        tk.Label(percentage_frame, text="📊 Academic Performance", font=("Segoe UI", 14, "bold"), fg="#1E293B", bg="#FFFFFF").pack(anchor="w", pady=(0,5))
        self.percentage = tk.Entry(percentage_frame, font=("Segoe UI", 14), relief="flat", bd=1, bg="#F4F6FB", width=30)
        self.percentage.pack(fill="x")
        tk.Label(percentage_frame, text="(Percentage )", font=("Segoe UI", 10), fg="#FB923C", bg="#FFFFFF").pack(anchor="w", pady=(2,0))

        # Grade/Year
        grade_frame = tk.Frame(right_frame, bg="#FFFFFF")
        grade_frame.pack(fill="x", pady=(0,20))
        tk.Label(grade_frame, text="📅 Grade ", font=("Segoe UI", 14, "bold"), fg="#1E293B", bg="#FFFFFF").pack(anchor="w", pady=(0,5))
        self.grade = tk.Entry(grade_frame, font=("Segoe UI", 14), relief="flat", bd=1, bg="#F4F6FB", width=30)
        self.grade.pack(fill="x")
        tk.Label(grade_frame, text="", font=("Segoe UI", 10), fg="#FB923C", bg="#FFFFFF").pack(anchor="w", pady=(2,0))
    def next_page(self):
        if not self.stream.get():
            messagebox.showerror("Error", "Please select your academic stream")
            return
        if not self.percentage.get().strip() or float(self.percentage.get())>100 or not self.percentage.get().isdigit():
            messagebox.showerror("Error", "Please enter your academic percentage")
            return
        if not self.grade.get().strip() or not self.grade.get().isdigit() or len(self.grade.get())!=2:
            messagebox.showerror("Error", "Please enter your valid grade")
            return

        self.parent.temp_data.update({
            "stream": self.stream.get(),
            "percentage": self.percentage.get().strip(),
            "grade": self.grade.get().strip()
        })
        self.parent.show_page("InterestsSkills")

    def previous(self):
        self.parent.show_page("PersonalInfo")



import tkinter as tk
from tkinter import messagebox
from logic import get_recommendation
from PIL import Image, ImageTk
from ui_utils import AnimatedBubbleBackground, create_navbar, create_step_tracker

class InterestsSkillsPage(tk.Frame):
    def __init__(self, parent, db):
        super().__init__(parent, bg="#F4F6FB")  # Page Background
        self.parent = parent
        self.db = db

        # Add animated bubble background
        self.bubble_bg = AnimatedBubbleBackground(self, bg_color="#F4F6FB")

        # Create navbar
        create_navbar(self, "Step 3 - Interests & Skills")
        create_step_tracker(self, 3, ["Personal Info", "Education", "Interests & Skills", "Recommendation"])

        # Main content
        main_frame = tk.Frame(self, bg="#F4F6FB")
        main_frame.pack(fill="both", expand=True, padx=24, pady=(14,18))

        # Title
        title_frame = tk.Frame(main_frame, bg="#FFFFFF", padx=30, pady=20, relief="raised", bd=2)
        title_frame.pack(fill="x", pady=(0,30))

        tk.Label(title_frame, text="🎯 Select Your Interests & Skills", font=("Segoe UI", 24, "bold"), fg="#1E293B", bg="#FFFFFF").pack()
        tk.Label(title_frame, text="Choose what excites you and what you're good at", font=("Segoe UI", 14), fg="#475569", bg="#FFFFFF").pack(pady=(5,0))

        # Content in two rectangular boxes
        content_frame = tk.Frame(main_frame, bg="#F4F6FB")
        content_frame.pack(fill="both", expand=True)

        # Interests section
        interests_card = tk.Frame(content_frame, bg="#FFFFFF", padx=18, pady=16, relief="raised", bd=1)
        interests_card.pack(side="left", fill="both", expand=True, padx=(0,15))

        # Interests header
        interests_header = tk.Frame(interests_card, bg="#FFFFFF")
        interests_header.pack(fill="x", pady=(0,10))

        tk.Label(interests_header, text="🎨", font=("Segoe UI", 36), bg="#FFFFFF").pack(side="left")
        tk.Label(interests_header, text="Interests", font=("Segoe UI", 20, "bold"), fg="#1E293B", bg="#FFFFFF").pack(side="left", padx=(15,0))

        tk.Label(interests_card, text="What activities excite you?", font=("Segoe UI", 11), fg="#475569", bg="#FFFFFF").pack(anchor="w", pady=(0,10))

        # Interests options in a grid
        interests_options = [
            ("🎨 Arts & Design", "Creative expression and visual arts"),
            ("🔬 Science & Research", "Exploring natural phenomena"),
            ("💻 Technology", "Working with computers and gadgets"),
            ("⚽ Sports & Fitness", "Physical activities and games"),
            ("💼 Business & Finance", "Entrepreneurship and management"),
            ("📚 Literature & Writing", "Reading and creative writing"),
            ("🎵 Music & Entertainment", "Performing arts and media"),
            ("🌍 Social & Community", "Helping others and community work")
        ]

        self.interests = []
        interests_grid = tk.Frame(interests_card, bg="#FFFFFF")
        interests_grid.pack(fill="both", expand=True)

        for i, (option, desc) in enumerate(interests_options):
            option_frame = tk.Frame(interests_grid, bg="#F4F6FB", padx=6, pady=4, relief="raised", bd=1)
            option_frame.grid(row=i//2, column=i%2, padx=4, pady=3, sticky="nsew")

            var = tk.BooleanVar()
            chk = tk.Checkbutton(option_frame, text=option, variable=var,
                               font=("Segoe UI", 9), bg="#F4F6FB", fg="#1E293B",
                               justify="left", anchor="w", padx=2, pady=1)
            chk.pack(fill="x")
            self.interests.append((option.split()[1] if len(option.split()) > 1 else option, var))

        # Skills section
        skills_card = tk.Frame(content_frame, bg="#FFFFFF", padx=18, pady=16, relief="raised", bd=1)
        skills_card.pack(side="right", fill="both", expand=True, padx=(15,0))

        # Skills header
        skills_header = tk.Frame(skills_card, bg="#FFFFFF")
        skills_header.pack(fill="x", pady=(0,10))

        tk.Label(skills_header, text="🛠️", font=("Segoe UI", 36), bg="#FFFFFF").pack(side="left")
        tk.Label(skills_header, text="Skills", font=("Segoe UI", 20, "bold"), fg="#1E293B", bg="#FFFFFF").pack(side="left", padx=(15,0))

        tk.Label(skills_card, text="What are you good at?", font=("Segoe UI", 11), fg="#475569", bg="#FFFFFF").pack(anchor="w", pady=(0,10))

        # Skills options in a grid
        skills_options = [
            ("🧠 Problem Solving", "Finding solutions to challenges"),
            ("💬 Communication", "Expressing ideas clearly"),
            ("🎨 Creativity", "Thinking outside the box"),
            ("👥 Leadership", "Guiding and motivating others"),
            ("🔧 Technical Skills", "Working with tools and systems"),
            ("📊 Analytical Thinking", "Breaking down complex information"),
            ("⏰ Time Management", "Organizing tasks efficiently"),
            ("🤝 Teamwork", "Collaborating with others")
        ]

        self.skills = []
        skills_grid = tk.Frame(skills_card, bg="#FFFFFF")
        skills_grid.pack(fill="both", expand=True)

        for i, (option, desc) in enumerate(skills_options):
            option_frame = tk.Frame(skills_grid, bg="#F4F6FB", padx=6, pady=4, relief="raised", bd=1)
            option_frame.grid(row=i//2, column=i%2, padx=4, pady=3, sticky="nsew")

            var = tk.BooleanVar()
            chk = tk.Checkbutton(option_frame, text=option, variable=var,
                               font=("Segoe UI", 9), bg="#F4F6FB", fg="#1E293B",
                               justify="left", anchor="w", padx=2, pady=1)
            chk.pack(fill="x")
            self.skills.append((option.split()[1] if len(option.split()) > 1 else option, var))

        # Configure grids
        interests_grid.grid_columnconfigure(0, weight=1)
        interests_grid.grid_columnconfigure(1, weight=1)
        skills_grid.grid_columnconfigure(0, weight=1)
        skills_grid.grid_columnconfigure(1, weight=1)

        # Navigation buttons - larger size
        btn_frame = tk.Frame(main_frame, bg="#F4F6FB")
        btn_frame.pack(side="bottom", fill="x", pady=(8, 0))

        prev_btn = tk.Button(btn_frame, text="Previous", font=("Segoe UI", 20, "bold"), bg="#E5E7EB", fg="#475569", padx=40, pady=16, width=14, command=self.previous)
        prev_btn.pack(side="left", padx=20)
        prev_btn.bind("<Enter>", lambda e: prev_btn.config(bg="#D1D5DB"))
        prev_btn.bind("<Leave>", lambda e: prev_btn.config(bg="#E5E7EB"))

        next_btn = tk.Button(btn_frame, text="Next", font=("Segoe UI", 20, "bold"), bg="#0284C7", fg="white", padx=40, pady=16, width=14, command=self.next_page)
        next_btn.pack(side="right", padx=20)
        next_btn.bind("<Enter>", lambda e: next_btn.config(bg="#0EA5E9"))
        next_btn.bind("<Leave>", lambda e: next_btn.config(bg="#0284C7"))

    def next_page(self):
        interests = [i[0] for i in self.interests if i[1].get()]
        skills = [s[0] for s in self.skills if s[1].get()]

        if not interests:
            messagebox.showwarning("Selection Required", "Please select at least one interest")
            return
        if not skills:
            messagebox.showwarning("Selection Required", "Please select at least one skill")
            return

        self.parent.temp_data.update({
            "interests": ", ".join(interests),
            "skills": ", ".join(skills)
        })

        # Insert into db
        data = self.parent.temp_data
        student_id = self.db.insert_student(
            data["name"], data["age"], data["gender"], data["contact"],
            data["stream"], data["percentage"], data["grade"],
            data["interests"], data["skills"]
        )
        self.parent.current_student_id = student_id
        rec = get_recommendation(
            data["stream"],
            interests,
            skills,
            data.get("percentage"),
            data.get("grade"),
        )
        self.parent.show_page("Recommendation", rec)

    def previous(self):
        self.parent.show_page("Education")


import tkinter as tk
from PIL import Image, ImageTk
from ui_utils import AnimatedBubbleBackground, create_navbar, create_step_tracker

class RecommendationPage(tk.Frame):
    def __init__(self, parent, db, rec):
        super().__init__(parent, bg="#F4F6FB")  # Page Background
        self.parent = parent
        self.db = db
        self.rec = rec
        data = self.parent.temp_data

        # Add animated bubble background
        self.bubble_bg = AnimatedBubbleBackground(self, bg_color="#F4F6FB")

        # Create navbar
        create_navbar(self, "Step 4 - Career Recommendation")
        create_step_tracker(self, 4, ["Personal Info", "Education", "Interests & Skills", "Recommendation"])

        # Main content
        main_frame = tk.Frame(self, bg="#F4F6FB")
        main_frame.pack(fill="both", expand=True, padx=16, pady=(10, 10))

        # Title
        title = tk.Label(main_frame, text="🎯 Your Career Recommendation", font=("Segoe UI", 22, "bold"), fg="#1E293B", bg="#F4F6FB")
        title.pack(pady=(0, 10))
        # Persistent action footer so buttons stay visible.
        btn_frame = tk.Frame(main_frame, bg="#F4F6FB")
        btn_frame.pack(side="bottom", fill="x", pady=(6, 0))

        re_eval_btn = tk.Button(
            btn_frame,
            text="Re-evaluate",
            font=("Segoe UI", 10, "bold"),
            bg="#FB923C",
            fg="white",
            padx=12,
            pady=6,
            command=lambda: self.parent.show_page("InterestsSkills"),
        )
        re_eval_btn.pack(side="left", padx=10)
        re_eval_btn.bind("<Enter>", lambda e: re_eval_btn.config(bg="#F97316"))
        re_eval_btn.bind("<Leave>", lambda e: re_eval_btn.config(bg="#FB923C"))

        end_btn = tk.Button(
            btn_frame,
            text="End",
            font=("Segoe UI", 10, "bold"),
            bg="#EF4444",
            fg="white",
            padx=14,
            pady=6,
            command=lambda: self.parent.show_page("ThankYou"),
        )
        end_btn.pack(side="left", padx=10)
        end_btn.bind("<Enter>", lambda e: end_btn.config(bg="#DC2626"))
        end_btn.bind("<Leave>", lambda e: end_btn.config(bg="#EF4444"))
        # Profile section - rectangular box with user image in middle
        profile_frame = tk.Frame(main_frame, bg="#FFFFFF", padx=14, pady=12, relief="raised", bd=2)
        profile_frame.pack(fill="x", pady=(0, 10))

        # Profile title
        tk.Label(profile_frame, text="Your Profile Summary", font=("Segoe UI", 16, "bold"), fg="#1E293B", bg="#FFFFFF").pack(pady=(0,12))

        # Profile content in horizontal layout
        profile_content = tk.Frame(profile_frame, bg="#FFFFFF")
        profile_content.pack(fill="x")

        # Left side - Image and basic info
        left_frame = tk.Frame(profile_content, bg="#FFFFFF")
        left_frame.pack(side="left", padx=(0, 12))

        # User image in center
        image_frame = tk.Frame(left_frame, bg="#F4F6FB", width=88, height=88, relief="solid", bd=1)
        image_frame.pack(pady=(0, 8))
        image_frame.pack_propagate(False)

        if data.get("image"):
            try:
                img = Image.open(data["image"])
                img = img.resize((78, 78))
                photo = ImageTk.PhotoImage(img)
                img_label = tk.Label(image_frame, image=photo, bg="#F4F6FB")
                img_label.image = photo
                img_label.pack(expand=True)
            except:
                tk.Label(image_frame, text="📷", font=("Segoe UI", 44), bg="#F4F6FB", fg="#5B5BD6").pack(expand=True)
        else:
            tk.Label(image_frame, text="👤", font=("Segoe UI", 44), bg="#F4F6FB", fg="#5B5BD6").pack(expand=True)

        # Basic info below image
        tk.Label(left_frame, text=f"Name: {data['name']}", font=("Segoe UI", 10, "bold"), fg="#1E293B", bg="#FFFFFF").pack(anchor="w", pady=1)
        tk.Label(left_frame, text=f"Age: {data['age']} years", font=("Segoe UI", 9), fg="#475569", bg="#FFFFFF").pack(anchor="w", pady=1)
        tk.Label(left_frame, text=f"Stream: {data['stream']}", font=("Segoe UI", 9), fg="#475569", bg="#FFFFFF").pack(anchor="w", pady=1)

        # Right side - Detailed info
        right_frame = tk.Frame(profile_content, bg="#FFFFFF")
        right_frame.pack(side="right", fill="both", expand=True)

        # Academic info
        academic_frame = tk.Frame(right_frame, bg="#F4F6FB", padx=10, pady=8, relief="raised", bd=1)
        academic_frame.pack(fill="x", pady=(0, 6))

        tk.Label(academic_frame, text="🎓 Academic Performance", font=("Segoe UI", 13, "bold"), fg="#1E293B", bg="#F4F6FB").pack(anchor="w", pady=(0,6))

        tk.Label(academic_frame, text=f"Percentage: {data['percentage']}%", font=("Segoe UI", 9), fg="#22C55E", bg="#F4F6FB").pack(anchor="w", pady=1)
        tk.Label(academic_frame, text=f"Grade: {data.get('grade', 'N/A')}", font=("Segoe UI", 9), fg="#475569", bg="#F4F6FB").pack(anchor="w", pady=1)

        # Interests and skills
        interests_frame = tk.Frame(right_frame, bg="#F4F6FB", padx=10, pady=8, relief="raised", bd=1)
        interests_frame.pack(fill="x", pady=(0, 6))

        tk.Label(interests_frame, text="🎯 Interests & Skills", font=("Segoe UI", 13, "bold"), fg="#1E293B", bg="#F4F6FB").pack(anchor="w", pady=(0,6))

        tk.Label(interests_frame, text=f"Interests: {data['interests']}", font=("Segoe UI", 9), fg="#FB923C", bg="#F4F6FB", wraplength=280, justify="left").pack(anchor="w", pady=1)
        tk.Label(interests_frame, text=f"Skills: {data['skills']}", font=("Segoe UI", 9), fg="#0284C7", bg="#F4F6FB", wraplength=280, justify="left").pack(anchor="w", pady=1)

        # Recommendation section
        rec_frame = tk.Frame(main_frame, bg="#FFFFFF", padx=14, pady=10, relief="raised", bd=2)
        rec_frame.pack(fill="both", expand=True)

        # Career recommendation header
        rec_header = tk.Frame(rec_frame, bg="#FFFFFF")
        rec_header.pack(fill="x", pady=(0, 8))

        tk.Label(rec_header, text="🚀", font=("Segoe UI", 28), bg="#FFFFFF").pack(side="left")
        tk.Label(rec_header, text="Recommended Career Path", font=("Segoe UI", 15, "bold"), fg="#1E293B", bg="#FFFFFF").pack(side="left", padx=(8, 0))

        # Career content in two columns
        career_content = tk.Frame(rec_frame, bg="#FFFFFF")
        career_content.pack(fill="x")

        # Left: Career image and title
        career_left = tk.Frame(career_content, bg="#FFFFFF")
        career_left.pack(side="left", padx=(0, 10))

        # Faculty/stream image
        faculty_img = self.get_faculty_image(data['stream'])
        if faculty_img:
            try:
                img = Image.open(faculty_img)
                img = img.resize((72, 72))
                photo = ImageTk.PhotoImage(img)
                faculty_label = tk.Label(career_left, image=photo, bg="#FFFFFF")
                faculty_label.image = photo
                faculty_label.pack(pady=(0,8))
            except:
                tk.Label(career_left, text=self.get_stream_icon(data['stream']), font=("Segoe UI", 44), bg="#FFFFFF").pack(pady=(0,8))

        # Career title
        tk.Label(career_left, text=self.rec["title"], font=("Segoe UI", 13, "bold"), fg="#0284C7", bg="#FFFFFF", wraplength=150, justify="center").pack()

        # Right: Career details
        career_right = tk.Frame(career_content, bg="#FFFFFF")
        career_right.pack(side="right", fill="both", expand=True)

        # Description
        desc_frame = tk.Frame(career_right, bg="#F4F6FB", padx=10, pady=8, relief="raised", bd=1)
        desc_frame.pack(fill="x", pady=(0, 6))

        tk.Label(desc_frame, text="📋 Career Description", font=("Segoe UI", 13, "bold"), fg="#1E293B", bg="#F4F6FB").pack(anchor="w", pady=(0,6))
        tk.Label(desc_frame, text=self.rec["description"], font=("Segoe UI", 9), fg="#475569", bg="#F4F6FB", wraplength=300, justify="left").pack(anchor="w")

        # Salary and future study
        details_frame = tk.Frame(career_right, bg="#FFFFFF")
        details_frame.pack(fill="x")

        # Salary info
        salary_frame = tk.Frame(details_frame, bg="#22C55E", padx=10, pady=8, relief="raised", bd=1)
        salary_frame.pack(side="left", fill="x", expand=True, padx=(0,6))

        tk.Label(salary_frame, text="💰 Expected Salary", font=("Segoe UI", 12, "bold"), fg="white", bg="#22C55E").pack(anchor="w")
        tk.Label(salary_frame, text=self.rec['salary'], font=("Segoe UI", 11, "bold"), fg="white", bg="#22C55E").pack(anchor="w", pady=(4, 0))

        # Future study info
        study_frame = tk.Frame(details_frame, bg="#FB923C", padx=10, pady=8, relief="raised", bd=1)
        study_frame.pack(side="right", fill="x", expand=True, padx=(6,0))

        tk.Label(study_frame, text="📚 Future Study", font=("Segoe UI", 12, "bold"), fg="white", bg="#FB923C").pack(anchor="w")
        tk.Label(study_frame, text=self.rec['future_study'], font=("Segoe UI", 10, "bold"), fg="white", bg="#FB923C").pack(anchor="w", pady=(4, 0))

    def get_faculty_image(self, stream):
        images = {
            "Science": "images/science.png",
            "Management": "images/management.png",
            "Humanities": "images/humanities.png",
            "Arts": "images/arts.png"
        }
        return images.get(stream)

    def get_stream_icon(self, stream):
        icons = {
            "Science": "🔬",
            "Management": "💼",
            "Humanities": "📚",
            "Arts": "🎨"
        }
        return icons.get(stream, "🎓")

    def get_faculty_image(self, stream):
        images = {
            "Science": "images/science.png",
            "Management": "images/management.png",
            "Humanities": "images/humanities.png",
            "Arts": "images/arts.png"
        }
        return images.get(stream)













