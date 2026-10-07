import tkinter as tk
from tkinter import ttk

from theme import COLORS, FONTS


class ReportsScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=COLORS["bg"])

        tk.Label(self, text="Reports", bg=COLORS["bg"], fg=COLORS["text"], font=("Segoe UI", 18, "bold")).pack(anchor="w", pady=(0, 16))

        cards = [
            ("Gross Sales", "₹64,500", COLORS["primary"]),
            ("Net Profit", "₹18,920", COLORS["accent"]),
            ("Refunds", "₹1,020", COLORS["danger"]),
            ("Avg. Order", "₹420", COLORS["warning"]),
        ]

        self.cards = tk.Frame(self, bg=COLORS["bg"])
        self.cards.pack(fill="x")

        for idx, (title, value, color) in enumerate(cards):
            card = tk.Frame(self.cards, bg=COLORS["card"], highlightbackground=COLORS["border"], highlightthickness=1, padx=18, pady=18)
            card.grid(row=0, column=idx, sticky="nsew", padx=8, pady=6)
            self.cards.columnconfigure(idx, weight=1)
            tk.Label(card, text=title, bg=COLORS["card"], fg=COLORS["muted"], font=FONTS["small_bold"]).pack(anchor="w")
            tk.Label(card, text=value, bg=COLORS["card"], fg=color, font=("Segoe UI", 22, "bold")).pack(anchor="w", pady=(8, 0))

        table_card = tk.Frame(self, bg=COLORS["card"], highlightbackground=COLORS["border"], highlightthickness=1)
        table_card.pack(fill="both", expand=True, pady=(18, 0))

        columns = ("Date", "Sales", "Transactions", "Profit")
        table = ttk.Treeview(table_card, columns=columns, show="headings", height=15)
        for col in columns:
            table.heading(col, text=col)
            table.column(col, width=180, anchor="center")

        sample = [
            ("2026-10-01", "₹9,420", "42", "₹2,980"),
            ("2026-10-02", "₹8,610", "38", "₹2,760"),
            ("2026-10-03", "₹11,820", "45", "₹3,210"),
            ("2026-10-04", "₹10,340", "40", "₹3,110"),
        ]
        for row in sample:
            table.insert("", "end", values=row)

        table.pack(fill="both", expand=True, padx=12, pady=12)
