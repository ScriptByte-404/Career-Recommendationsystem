import tkinter as tk
from database import Database
from welcome import WelcomePage
from login import LoginPage
from dashboard import DashboardPage
from admin_page import AdminPage
from signup import SignupPage
from evaluation_steps import (
    EvaluationOverviewPage,
    PersonalInfoPage,
    EducationPage,
    InterestsSkillsPage,
    RecommendationPage,
)
from thank_you import ThankYouPage


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Career Recommendation System")
        self.geometry("1200x800")
        self.configure(bg="#203A43")
        self.db = Database()
        self.current_student_id = None
        self.current_username = "User"
        self.temp_data = {}
        self.pages = {}
        self.show_page("Welcome")

    def reset_evaluation_flow(self):
        self.temp_data = {}
        self.current_student_id = None

        evaluation_pages = [
            "EvaluationOverview",
            "PersonalInfo",
            "Education",
            "InterestsSkills",
            "Recommendation",
            "ThankYou",
        ]
        for page_name in evaluation_pages:
            page = self.pages.pop(page_name, None)
            if page is not None and page.winfo_exists():
                page.destroy()

    def show_page(self, page_name, *args):
        for page in self.pages.values():
            page.pack_forget()
        if page_name == "Recommendation":
            existing_page = self.pages.pop(page_name, None)
            if existing_page is not None and existing_page.winfo_exists():
                existing_page.destroy()
        if page_name not in self.pages:
            if page_name == "Welcome":
                self.pages[page_name] = WelcomePage(self, self.db)
            elif page_name == "Login":
                self.pages[page_name] = LoginPage(self, self.db)
            elif page_name == "Dashboard":
                self.pages[page_name] = DashboardPage(self, self.db)
            elif page_name == "Admin":
                self.pages[page_name] = AdminPage(self, self.db)
            elif page_name == "Signup":
                self.pages[page_name] = SignupPage(self, self.db)
            elif page_name == "EvaluationOverview":
                self.pages[page_name] = EvaluationOverviewPage(self, self.db)
            elif page_name == "PersonalInfo":
                self.pages[page_name] = PersonalInfoPage(self, self.db)
            elif page_name == "Education":
                self.pages[page_name] = EducationPage(self, self.db)
            elif page_name == "InterestsSkills":
                self.pages[page_name] = InterestsSkillsPage(self, self.db)
            elif page_name == "Recommendation":
                self.pages[page_name] = RecommendationPage(self, self.db, *args)
            elif page_name == "ThankYou":
                self.pages[page_name] = ThankYouPage(self, self.db)
        if page_name == "Login":
            login_page = self.pages.get("Login")
            if login_page and hasattr(login_page, "clear_fields"):
                login_page.clear_fields()
        self.pages[page_name].pack(fill="both", expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()
