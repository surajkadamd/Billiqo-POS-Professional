import tkinter as tk
from tkinter import ttk

from theme import COLORS, FONTS


class LoginScreen(tk.Frame):
    def __init__(self, parent, on_login):
        super().__init__(parent, bg=COLORS["bg"])
        self.on_login = on_login

        self.pack(fill="both", expand=True)

        self.main = tk.Frame(self, bg=COLORS["card"], padx=30, pady=30)
        self.main.place(relx=0.5, rely=0.5, anchor="center", width=500, height=430)

        self.brand = tk.Label(
            self.main,
            text="BILLIQO",
            bg=COLORS["card"],
            fg=COLORS["primary"],
            font=("Segoe UI", 26, "bold")
        )
        self.brand.pack(anchor="w", pady=(10, 5))

        self.subtitle = tk.Label(
            self.main,
            text="Retail POS & Inventory System",
            bg=COLORS["card"],
            fg=COLORS["muted"],
            font=FONTS["small_bold"]
        )
        self.subtitle.pack(anchor="w", pady=(0, 18))

        tk.Label(self.main, text="Username", bg=COLORS["card"], fg=COLORS["text"], font=FONTS["small_bold"]).pack(anchor="w", pady=(14, 4))
        self.username_var = tk.StringVar(value="admin")
        self.username_entry = tk.Entry(self.main, textvariable=self.username_var, font=FONTS["body"], relief="solid", bd=1)
        self.username_entry.pack(fill="x", ipady=8)

        tk.Label(self.main, text="Password", bg=COLORS["card"], fg=COLORS["text"], font=FONTS["small_bold"]).pack(anchor="w", pady=(18, 4))
        self.password_var = tk.StringVar(value="admin123")
        self.password_entry = tk.Entry(self.main, textvariable=self.password_var, show="*", font=FONTS["body"], relief="solid", bd=1)
        self.password_entry.pack(fill="x", ipady=8)

        self.status = tk.Label(self.main, text="", bg=COLORS["card"], fg=COLORS["danger"], font=FONTS["small"])
        self.status.pack(anchor="w", pady=(10, 0))

        self.login_button = tk.Button(
            self.main,
            text="Login",
            bg=COLORS["primary"],
            fg=COLORS["white"],
            activebackground=COLORS["primary_dark"],
            activeforeground=COLORS["white"],
            relief="flat",
            bd=0,
            font=FONTS["small_bold"],
            padx=20,
            pady=10,
            command=self._do_login
        )
        self.login_button.pack(fill="x", pady=(20, 0))

        self.password_entry.bind("<Return>", lambda e: self._do_login())

    def _do_login(self):
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()

        if username and password:
            self.status.config(text="Login successful", fg=COLORS["accent"])
            self.on_login(username)
        else:
            self.status.config(text="Please enter username and password.", fg=COLORS["danger"])
