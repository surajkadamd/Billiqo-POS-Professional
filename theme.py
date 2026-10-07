COLORS = {
    "bg": "#F3F6FB",
    "card": "#FFFFFF",
    "primary": "#1E3A8A",
    "primary_dark": "#0F172A",
    "primary_light": "#EAF2FF",
    "accent": "#10B981",
    "warning": "#F59E0B",
    "danger": "#EF4444",
    "muted": "#6B7280",
    "text": "#1F2937",
    "border": "#E5E7EB",
    "sidebar": "#111827",
    "nav_alt": "#1F2937",
    "white": "#FFFFFF",
    "success_bg": "#EAF7F0",
    "warning_bg": "#FFF7E5",
    "danger_bg": "#FCE7E7",
    "light_gray": "#F8FAFC",
}

FONTS = {
    "heading": ("Segoe UI", 22, "bold"),
    "title": ("Segoe UI", 18, "bold"),
    "subtitle": ("Segoe UI", 11, "bold"),
    "body": ("Segoe UI", 10),
    "small": ("Segoe UI", 9),
    "small_bold": ("Segoe UI", 9, "bold"),
}


def apply_theme(root):
    root.option_add("*Font", FONTS["body"])
    root.configure(bg=COLORS["bg"])

    style = ttk.Style(root)
    try:
        style.theme_use("clam")
    except Exception:
        pass

    style.configure("TFrame", background=COLORS["bg"])
    style.configure("TLabel", background=COLORS["bg"], foreground=COLORS["text"])
    style.configure("Card.TFrame", background=COLORS["card"])
    style.configure("TButton", padding=(10, 7), font=FONTS["small_bold"])
    style.configure("Primary.TButton", background=COLORS["primary"], foreground=COLORS["white"], padding=(12, 8))
    style.map("Primary.TButton", background=[("active", COLORS["primary_dark"])])
    style.configure("Success.TButton", background=COLORS["accent"], foreground=COLORS["white"], padding=(12, 8))
    style.map("Success.TButton", background=[("active", "#059669")])
    style.configure("Warning.TButton", background=COLORS["warning"], foreground=COLORS["white"], padding=(12, 8))
    style.map("Warning.TButton", background=[("active", "#D97706")])
    style.configure("TEntry", fieldbackground=COLORS["white"], foreground=COLORS["text"], padding=6)
    style.configure("Treeview", background=COLORS["white"], fieldbackground=COLORS["white"], foreground=COLORS["text"], rowheight=26)
    style.configure("Treeview.Heading", background=COLORS["light_gray"], foreground=COLORS["text"], font=FONTS["small_bold"])
