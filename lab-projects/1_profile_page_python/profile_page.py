"""Profile Page with Dark / Light mode toggle (Python + Tkinter)."""
import tkinter as tk

THEMES = {
    "light": {"bg": "#f5f5f5", "fg": "#222222", "card": "#ffffff", "accent": "#2563eb"},
    "dark":  {"bg": "#1e1e2e", "fg": "#e5e5e5", "card": "#2a2a3c", "accent": "#60a5fa"},
}

# Apni details yahan change karo
PROFILE = {
    "name": "Your Name",
    "course": "BCA - Semester III",
    "university": "JECRC University",
    "email": "yourname@example.com",
    "skills": "Python, C, C++, Java, HTML/CSS",
}


class ProfileApp:
    def __init__(self, root):
        self.root = root
        self.mode = "light"
        root.title("Profile Page")
        root.geometry("420x380")

        self.card = tk.Frame(root, padx=20, pady=20)
        self.card.pack(expand=True, padx=20, pady=20, fill="both")

        self.title = tk.Label(self.card, text=PROFILE["name"], font=("Arial", 20, "bold"))
        self.title.pack(pady=(0, 10))

        self.labels = []
        for key in ("course", "university", "email", "skills"):
            lbl = tk.Label(self.card, text=f"{key.title()}: {PROFILE[key]}", font=("Arial", 12))
            lbl.pack(anchor="w", pady=4)
            self.labels.append(lbl)

        self.btn = tk.Button(self.card, text="Switch to Dark Mode",
                             command=self.toggle, relief="flat", padx=10, pady=6)
        self.btn.pack(pady=20)
        self.apply_theme()

    def toggle(self):
        self.mode = "dark" if self.mode == "light" else "light"
        self.apply_theme()

    def apply_theme(self):
        t = THEMES[self.mode]
        self.root.configure(bg=t["bg"])
        self.card.configure(bg=t["card"])
        self.title.configure(bg=t["card"], fg=t["accent"])
        for lbl in self.labels:
            lbl.configure(bg=t["card"], fg=t["fg"])
        other = "Dark" if self.mode == "light" else "Light"
        self.btn.configure(text=f"Switch to {other} Mode", bg=t["accent"], fg="#ffffff")


if __name__ == "__main__":
    root = tk.Tk()
    ProfileApp(root)
    root.mainloop()
