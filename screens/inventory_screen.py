import tkinter as tk
from tkinter import ttk

from theme import COLORS, FONTS


class PosScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=COLORS["bg"])

        self.search_bar = tk.Frame(self, bg=COLORS["card"], highlightbackground=COLORS["border"], highlightthickness=1)
        self.search_bar.pack(fill="x", pady=(0, 12))

        tk.Label(self.search_bar, text="Search Product", bg=COLORS["card"], fg=COLORS["text"], font=FONTS["small_bold"]).pack(side="left", padx=16, pady=12)
        self.search_entry = tk.Entry(self.search_bar, width=30, font=FONTS["body"], relief="solid", bd=1)
        self.search_entry.pack(side="left", padx=8, pady=10, ipady=6)

        tk.Button(self.search_bar, text="Scan", bg=COLORS["primary"], fg=COLORS["white"], relief="flat", bd=0, font=FONTS["small_bold"], padx=18, pady=7).pack(side="left", padx=8)
        tk.Button(self.search_bar, text="Add Item", bg=COLORS["accent"], fg=COLORS["white"], relief="flat", bd=0, font=FONTS["small_bold"], padx=18, pady=7).pack(side="left", padx=8)

        self.main = tk.Frame(self, bg=COLORS["bg"])
        self.main.pack(fill="both", expand=True)

        self.left = tk.Frame(self.main, bg=COLORS["card"], highlightbackground=COLORS["border"], highlightthickness=1)
        self.left.pack(side="left", fill="both", expand=True, padx=(0, 10))

        tk.Label(self.left, text="Cart", bg=COLORS["card"], fg=COLORS["text"], font=FONTS["subtitle"]).pack(anchor="w", padx=16, pady=(16, 4))

        columns = ("Item", "Qty", "Price", "Total")
        self.table = ttk.Treeview(self.left, columns=columns, show="headings", height=14)
        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=140, anchor="center")
        self.table.pack(fill="both", expand=True, padx=12, pady=(8, 12))

        sample_items = [
            ("Milk Powder 1kg", "2", "₹230.00", "₹460.00"),
            ("Rice 10kg", "1", "₹560.00", "₹560.00"),
            ("Soap Pack", "3", "₹80.00", "₹240.00"),
        ]
        for row in sample_items:
            self.table.insert("", "end", values=row)

        self.right = tk.Frame(self.main, bg=COLORS["card"], width=340, highlightbackground=COLORS["border"], highlightthickness=1)
        self.right.pack(side="right", fill="y")
        self.right.pack_propagate(False)

        tk.Label(self.right, text="Payment Summary", bg=COLORS["card"], fg=COLORS["text"], font=FONTS["subtitle"]).pack(anchor="w", padx=16, pady=(16, 10))

        summary = [
            ("Subtotal", "₹1,260.00"),
            ("Tax", "₹75.60"),
            ("Discount", "₹0.00"),
            ("Total", "₹1,335.60"),
        ]

        for label, value in summary:
            row = tk.Frame(self.right, bg=COLORS["card"])
            row.pack(fill="x", padx=18, pady=8)
            tk.Label(row, text=label, bg=COLORS["card"], fg=COLORS["muted"], font=FONTS["small"]).pack(side="left")
            tk.Label(row, text=value, bg=COLORS["card"], fg=COLORS["text"], font=FONTS["small_bold"]).pack(side="right")

        btn_bar = tk.Frame(self.right, bg=COLORS["card"])
        btn_bar.pack(fill="x", padx=18, pady=(18, 10))

        tk.Button(btn_bar, text="Cash Payment", bg=COLORS["accent"], fg=COLORS["white"], relief="flat", bd=0, font=FONTS["small_bold"], padx=12, pady=9, width=14).pack(fill="x")
        tk.Button(btn_bar, text="Card Payment", bg=COLORS["primary"], fg=COLORS["white"], relief="flat", bd=0, font=FONTS["small_bold"], padx=12, pady=9, width=14).pack(fill="x", pady=(8, 0))
        tk.Button(btn_bar, text="Hold Bill", bg=COLORS["warning"], fg=COLORS["white"], relief="flat", bd=0, font=FONTS["small_bold"], padx=12, pady=9, width=14).pack(fill="x", pady=(8, 0))
