import tkinter as tk
from tkinter import ttk

from theme import COLORS, FONTS, apply_theme
from screens.login_screen import LoginScreen


class BilliqoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Billiqo POS Professional")
        self.geometry("1500x900")
        self.minsize(1200, 760)
        self.configure(bg=COLORS["bg"])

        self.after_id = None

        apply_theme(self)
        self._build_login()

    def _build_login(self):
        self.login_screen = LoginScreen(self, on_login=self._on_login)
        self.login_screen.pack(fill="both", expand=True)

    def _on_login(self, username):
        self.login_screen.pack_forget()
        self.login_screen.destroy()

        self.user_label = username
        self._build_shell()

    def _build_shell(self):
        self.configure(bg=COLORS["bg"])

        self.sidebar = tk.Frame(self, bg=COLORS["sidebar"], width=220)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        self.brand = tk.Label(
            self.sidebar,
            text="BILLIQO",
            bg=COLORS["sidebar"],
            fg=COLORS["white"],
            font=FONTS["heading"]
        )
        self.brand.pack(anchor="w", padx=22, pady=(18, 10))

        self.user_chip = tk.Label(
            self.sidebar,
            text=f"User: {self.user_label}",
            bg=COLORS["nav_alt"],
            fg=COLORS["white"],
            font=FONTS["small_bold"],
            padx=14,
            pady=8
        )
        self.user_chip.pack(fill="x", padx=14, pady=(0, 20))

        self.nav_items = [
            ("Dashboard", "dashboard"),
            ("POS", "pos"),
            ("Inventory", "inventory"),
            ("Reports", "reports"),
            ("Logout", "logout"),
        ]

        self.nav_buttons = {}
        for label, key in self.nav_items:
            button = tk.Button(
                self.sidebar,
                text=label,
                bg=COLORS["sidebar"],
                fg=COLORS["white"],
                activebackground=COLORS["nav_alt"],
                activeforeground=COLORS["white"],
                relief="flat",
                bd=0,
                font=FONTS["small_bold"],
                anchor="w",
                justify="left",
                padx=20,
                pady=12,
                command=lambda k=key: self.switch_screen(k)
            )
            button.pack(fill="x")
            self.nav_buttons[key] = button

        self.main = tk.Frame(self, bg=COLORS["bg"])
        self.main.pack(side="left", fill="both", expand=True)

        self.topbar = tk.Frame(self.main, bg=COLORS["card"], height=72)
        self.topbar.pack(fill="x")
        self.topbar.pack_propagate(False)

        self.title_label = tk.Label(
            self.topbar,
            text="Dashboard",
            bg=COLORS["card"],
            fg=COLORS["text"],
            font=FONTS["title"]
        )
        self.title_label.pack(anchor="w", padx=24, pady=(16, 0))

        self.content = tk.Frame(self.main, bg=COLORS["bg"])
        self.content.pack(fill="both", expand=True, padx=18, pady=18)

        from screens.dashboard_screen import DashboardScreen
        from screens.pos_screen import PosScreen
        from screens.inventory_screen import InventoryScreen
        from screens.reports_screen import ReportsScreen

        self.screens = {
            "dashboard": DashboardScreen(self.content),
            "pos": PosScreen(self.content),
            "inventory": InventoryScreen(self.content),
            "reports": ReportsScreen(self.content),
        }

        self.switch_screen("dashboard")

    def switch_screen(self, key):
        for name, frame in self.screens.items():
            frame.pack_forget()

        if key == "logout":
            self.destroy()
            return

        if key in self.screens:
            self.screens[key].pack(fill="both", expand=True)
            self.title_label.config(text={
                "dashboard": "Dashboard",
                "pos": "Point of Sale",
                "inventory": "Inventory",
                "reports": "Reports"
            }[key])

        for nav_key, button in self.nav_buttons.items():
            if nav_key == key:
                button.configure(bg=COLORS["nav_alt"], fg=COLORS["white"])
            else:
                button.configure(bg=COLORS["sidebar"], fg=COLORS["white"])


def main():
    app = BilliqoApp()
    app.mainloop()


if __name__ == "__main__":
    main()
