import tkinter as tk
from tkinter import ttk, messagebox

from ui_utils import create_navbar


class AdminPage(tk.Frame):
    def __init__(self, parent, db):
        super().__init__(parent, bg="#F8FAFF")
        self.parent = parent
        self.db = db

        navbar = create_navbar(self, "Admin - Manage Students")
        logout_btn = tk.Button(
            navbar,
            text="Logout",
            font=("Segoe UI", 10, "bold"),
            bg="#DC2626",
            fg="white",
            activebackground="#B91C1C",
            activeforeground="white",
            relief="flat",
            padx=14,
            pady=4,
            cursor="hand2",
            command=lambda: self.parent.show_page("Login"),
        )
        logout_btn.pack(side="right")

        container = tk.Frame(self, bg="#F8FAFF", padx=16, pady=12)
        container.pack(fill="both", expand=True)

        control_row = tk.Frame(container, bg="#F8FAFF")
        control_row.pack(fill="x", pady=(0, 8))

        refresh_btn = tk.Button(control_row, text="Refresh", command=self.refresh_students)
        refresh_btn.pack(side="left")

        tk.Label(control_row, text="Delete student by ID:", bg="#F8FAFF").pack(side="left", padx=(10, 4))
        self.delete_entry = tk.Entry(control_row, width=8)
        self.delete_entry.pack(side="left")

        del_btn = tk.Button(control_row, text="Delete", bg="#EF4444", fg="white", command=self.delete_by_id)
        del_btn.pack(side="left", padx=(6, 0))

        tree_frame = tk.Frame(container, bg="#F8FAFF")
        tree_frame.pack(fill="both", expand=True)

        columns = ("id", "name", "age", "gender", "contact", "stream", "percentage", "grade")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col.title())
            self.tree.column(col, width=120, anchor="center")

        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True)

        self.tree.bind("<<TreeviewSelect>>", self.on_select)

        self.refresh_students()

    def refresh_students(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        students = self.db.get_all_students()
        for s in students:
            # s is a tuple aligned with table columns: (id, name, age, gender, contact, stream, percentage, grade, interests, skills)
            self.tree.insert("", "end", values=(s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7]))

    def on_select(self, event):
        sel = self.tree.selection()
        if sel:
            item = self.tree.item(sel[0])
            sid = item["values"][0]
            self.delete_entry.delete(0, tk.END)
            self.delete_entry.insert(0, str(sid))

    def delete_by_id(self):
        sid = self.delete_entry.get().strip()
        if not sid.isdigit():
            messagebox.showerror("Error", "Please enter a valid numeric student ID.")
            return
        sid = int(sid)
        if not messagebox.askyesno("Confirm Delete", f"Delete student ID {sid}?"):
            return
        deleted = self.db.delete_student(sid)
        if deleted:
            messagebox.showinfo("Deleted", f"Student ID {sid} deleted.")
            self.refresh_students()
        else:
            messagebox.showwarning("Not found", f"No student with ID {sid}.")
