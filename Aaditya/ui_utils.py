import tkinter as tk


class AnimatedBubbleBackground:
    """Set page background color."""

    def __init__(self, parent, bg_color="#F4F6FB"):
        parent.configure(bg=bg_color)


def create_navbar(parent, title="Career Recommendation System"):
    """Create top navigation bar."""
    navbar = tk.Frame(parent, bg="#075985", padx=16, pady=10)
    navbar.pack(fill="x", side="top")

    tk.Label(navbar, text="🎓", font=("Segoe UI", 18), bg="#075985", fg="white").pack(side="left", padx=(0, 8))
    tk.Label(navbar, text=title, font=("Segoe UI", 16, "bold"), bg="#075985", fg="white").pack(side="left")

    return navbar


def create_stat_card(parent, title, value, icon):
    """Create stat card with icon, title, and value."""
    card = tk.Frame(parent, bg="white", padx=20, pady=15, relief="raised", bd=1)

    tk.Label(card, text=icon, font=("Segoe UI", 24), bg="white").pack()
    tk.Label(card, text=title, font=("Segoe UI", 12, "bold"), fg="#1E293B", bg="white").pack()
    tk.Label(card, text=value, font=("Segoe UI", 20, "bold"), fg="#0284C7", bg="white").pack()

    return card


def create_step_tracker(parent, current_step, steps):
    """Create progress tracker showing current step."""
    tracker = tk.Frame(parent, bg="#FFFFFF", padx=10, pady=8, relief="ridge", bd=1)
    tracker.pack(fill="x", padx=16, pady=(8, 0))

    for idx, step_name in enumerate(steps, start=1):
        if idx == current_step:
            bg = "#0F6CBD"
            fg = "#FFFFFF"
        elif idx < current_step:
            bg = "#DCEBFA"
            fg = "#0B3C6D"
        else:
            bg = "#E5E7EB"
            fg = "#475569"

        step_box = tk.Frame(tracker, bg=bg, padx=10, pady=6, relief="flat", bd=0)
        step_box.pack(side="left", fill="x", expand=True, padx=3)

        tk.Label(
            step_box,
            text=f"{idx}. {step_name}",
            font=("Segoe UI", 9, "bold"),
            fg=fg,
            bg=bg,
        ).pack()

    return tracker
