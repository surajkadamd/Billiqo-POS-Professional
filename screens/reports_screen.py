import tkinter as tk
from tkinter import ttk

from theme import COLORS, FONTS


class InventoryScreen(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=COLORS["bg"])

        self.top = tk.Frame(self, bg=COLORS["bg"])
        self.top.pack(fill="x", pady=(0, 12))

        tk.Label(self.top, text="Inventory", bg=COLORS["bg"], fg=COLORS["text"], font=("Segoe UI", 18, "bold")).pack(side="left")
        tk.Button(self.top, text="Add Product", bg=COLORS["primary"], fg=COLORS["white"], relief="flat", bd=0, font=FONTS["small_bold"], padx=16, pady=8).pack(side="right")

        search = tk.Frame(self, bg=COLORS["card"], highlightbackground=COLORS["border"], highlightthickness=1)
        search.pack(fill="x", pady=(0, 12))
        tk.Label(search, text="Search Items", bg=COLORS["card"], fg=COLORS["text"], font=FONTS["small_bold"]).pack(side="left", padx=16, pady=12)
        tk.Entry(search, width=34, font=FONTS["body"], relief="solid", bd=1).pack(side="left", padx=8, ipady=5)

        tree_frame = tk.Frame(self, bg=COLORS["card"], highlightbackground=COLORS["border"], highlightthickness=1)
        tree_frame.pack(fill="both", expand=True)

        columns = ("Barcode", "Item Name", "Category", "Qty", "Price", "Status")
        self.table = ttk.Treeview(tree_frame, columns=columns, show="headings", height=18)
        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=160, anchor="center")

        self.table.pack(fill="both", expand=True, padx=12, pady=12)

        sample_rows = [
            ("BQ-1001", "Milk Powder 1kg", "Groceries", "28", "₹230", "In Stock"),
            ("BQ-1002", "Rice 10kg", "Groceries", "12", "₹560", "Low Stock"),
            ("BQ-1003", "Soap Pack", "Household", "47", "₹80", "In Stock"),
            ("BQ-1004", "Tea Leaves", "Groceries", "5", "₹190", "Critical"),
        ]

        for row in sample_rows:
            self.table.insert("", "end", values=row)
