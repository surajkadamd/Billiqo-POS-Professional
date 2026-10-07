import tkinter as tk
from tkinter import ttk

from theme import COLORS, FONTS


class DashboardScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=COLORS["bg"])

        self.header = tk.Label(
            self,
            text="Overview",
            bg=COLORS["bg"],
            fg=COLORS["text"],
            font=FONTS["title"]
        )
        self.header.pack(anchor="w", pady=(0, 16))

        cards = [
            ("Net Sales", "₹18,450", "+18% vs last week", COLORS["primary"]),
            ("Transactions", "214", "+22 today", COLORS["accent"]),
            ("Inventory Value", "₹86,320", "12 low stock alerts", COLORS["warning"]),
            ("Refunds", "₹1,420", "-5% vs last week", COLORS["danger"]),
        ]

        self.card_holder = tk.Frame(self, bg=COLORS["bg"])
        self.card_holder.pack(fill="x")

        for idx, (title, value, delta, color) in enumerate(cards):
            card = tk.Frame(self.card_holder, bg=COLORS["card"], padx=18, pady=18, highlightbackground=COLORS["border"], highlightthickness=1)
            card.grid(row=0, column=idx, sticky="nsew", padx=8, pady=4)
            self.card_holder.columnconfigure(idx, weight=1)

            tk.Label(card, text=title, fg=COLORS["muted"], bg=COLORS["card"], font=FONTS["small_bold"]).pack(anchor="w")
            tk.Label(card, text=value, fg=color, bg=COLORS["card"], font=("Segoe UI", 22, "bold")).pack(anchor="w", pady=(8, 6))
            tk.Label(card, text=delta, fg=COLORS["muted"], bg=COLORS["card"], font=FONTS["small"]).pack(anchor="w")

        self.content = tk.Frame(self, bg=COLORS["bg"], pady=20)
        self.content.pack(fill="both", expand=True)

        left = tk.Frame(self.content, bg=COLORS["card"], highlightbackground=COLORS["border"], highlightthickness=1)
        left.pack(side="left", fill="both", expand=True, padx=(0, 10))
        tk.Label(left, text="Sales Trend", bg=COLORS["card"], fg=COLORS["text"], font=FONTS["subtitle"]).pack(anchor="w", padx=16, pady=(16, 8))

        canvas = tk.Canvas(left, bg=COLORS["card"], height=250, highlightthickness=0)
        canvas.pack(fill="both", expand=True, padx=12, pady=(0, 12))

        vals = [70, 120, 95, 150, 170, 130, 220]
        max_value = max(vals)
        width = 520
        height = 220
        area_x = 40
        area_y = 20
        step = (width - 80) / (len(vals) - 1)

        canvas.create_line(area_x, area_y, area_x, height - 30, fill=COLORS["border"])
        canvas.create_line(area_x, height - 30, width - 20, height - 30, fill=COLORS["border"])

        for index, value in enumerate(vals):
            x = area_x + step * index
            y = height - 30 - (value / max_value) * 150
            canvas.create_rectangle(x - 8, y, x + 8, height - 30, fill=COLORS["primary"], outline="")

        right = tk.Frame(self.content, bg=COLORS["card"], highlightbackground=COLORS["border"], highlightthickness=1)
        right.pack(side="right", fill="y", padx=(10, 0))
        tk.Label(right, text="Top Products", bg=COLORS["card"], fg=COLORS["text"], font=FONTS["subtitle"]).pack(anchor="w", padx=16, pady=(16, 8))

        items = [
            ("Milk Powder 1kg", "120"),
            ("Rice 10kg", "96"),
            ("Soap Pack", "88"),
            ("Cookies Box", "74"),
            ("Tea Leaves", "62"),
        ]

        for name, qty in items:
            row = tk.Frame(right, bg=COLORS["card"])
            row.pack(fill="x", padx=16, pady=8)
            tk.Label(row, text=name, bg=COLORS["card"], fg=COLORS["text"], font=FONTS["small"]).pack(side="left")
            tk.Label(row, text=qty, bg=COLORS["card"], fg=COLORS["primary"], font=FONTS["small_bold"]).pack(side="right")
