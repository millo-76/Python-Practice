import csv
import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

DATA_FILE = os.path.join(os.path.dirname(__file__), "wrestlers.csv")


def ensure_csv_exists():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Team", "WeightClass", "Wins", "Losses", "Total Points Scored"])


class WrestlerTracker(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Wrestler Tracker")
        self.geometry("560x380")
        self.resizable(False, False)

        self.create_widgets()
        ensure_csv_exists()

    def create_widgets(self):
        frm = ttk.Frame(self, padding=12)
        frm.pack(fill=tk.BOTH, expand=True)

        # Labels and entries
        labels = ["Name", "Team", "Weight class", "Wins", "Losses", "Total Points Scored"]
        self.entries = {}
        for i, lbl in enumerate(labels):
            ttk.Label(frm, text=lbl).grid(row=i, column=0, sticky=tk.W, pady=4)
            entry = ttk.Entry(frm, width=40)
            entry.grid(row=i, column=1, sticky=tk.W, padx=6)
            self.entries[lbl] = entry

        # Buttons
        btn_frame = ttk.Frame(frm)
        btn_frame.grid(row=len(labels), column=0, columnspan=2, pady=(12, 0))

        save_btn = ttk.Button(btn_frame, text="Save", command=self.save_record)
        save_btn.grid(row=0, column=0, padx=6)

        show_btn = ttk.Button(btn_frame, text="Show records", command=self.show_records)
        show_btn.grid(row=0, column=1, padx=6)

        export_btn = ttk.Button(btn_frame, text="Export CSV...", command=self.export_csv)
        export_btn.grid(row=0, column=2, padx=6)

        clear_btn = ttk.Button(btn_frame, text="Clear fields", command=self.clear_fields)
        clear_btn.grid(row=0, column=3, padx=6)

    def save_record(self):
        # Gather values
        name = self.entries["Name"].get().strip()
        team = self.entries["Team"].get().strip()
        weight = self.entries["Weight class"].get().strip()
        wins = self.entries["Wins"].get().strip()
        losses = self.entries["Losses"].get().strip()
        ptsscored = self.entries["Total Points Scored"].get().strip()

        if not name:
            messagebox.showwarning("Missing data", "Please enter the wrestler's name.")
            return

        # Basic validation for numeric fields
        try:
            wins_val = int(wins) if wins else 0
            losses_val = int(losses) if losses else 0
        except ValueError:
            messagebox.showerror("Invalid number", "Wins and Losses must be integers.")
            return

        row = [name, team, weight, str(wins_val), str(losses_val), str(ptsscored)]
        try:
            with open(DATA_FILE, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(row)
            messagebox.showinfo("Saved", f"Saved {name} to records.")
            self.clear_fields()
        except Exception as e:
            messagebox.showerror("Save failed", str(e))

    def show_records(self):
        if not os.path.exists(DATA_FILE):
            messagebox.showinfo("No data", "No records found.")
            return

        win = tk.Toplevel(self)
        win.title("Saved Wrestlers")
        win.geometry("700x400")

        tree = ttk.Treeview(win, columns=("Team", "Weight", "Wins", "Losses", "Total Points Scored"), show="headings")
        tree.heading("Team", text="Team")
        tree.heading("Weight", text="Weight Class")
        tree.heading("Wins", text="Wins")
        tree.heading("Losses", text="Losses")
        tree.heading("Total Points Scored", text="Total Points Scored")
        tree.pack(fill=tk.BOTH, expand=True)

        # Add name as first column by inserting into values with a custom display
        tree.config(columns=("Name", "Team", "Weight", "Wins", "Losses", "Total Points Scored"))
        tree.heading("Name", text="Name")
        tree.heading("Weight", text="Weight Class")
        tree.heading("Wins", text="Wins")
        tree.heading("Losses", text="Losses")
        tree.heading("Total Points Scored", text="Total Points Scored")

        with open(DATA_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            headers = next(reader, None)
            for r in reader:
                # r expected: Name, Team, WeightClass, Wins, Losses, Total Points Scored
                tree.insert("", tk.END, values=r)

        # Add simple scrollbar
        sb = ttk.Scrollbar(win, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=sb.set)
        sb.pack(side=tk.RIGHT, fill=tk.Y)

    def export_csv(self):
        if not os.path.exists(DATA_FILE):
            messagebox.showinfo("No data", "No records to export.")
            return
        dest = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not dest:
            return
        try:
            with open(DATA_FILE, "r", newline="", encoding="utf-8") as src, open(dest, "w", newline="", encoding="utf-8") as dst:
                dst.write(src.read())
            messagebox.showinfo("Exported", f"Exported records to {dest}")
        except Exception as e:
            messagebox.showerror("Export failed", str(e))

    def clear_fields(self):
        for e in self.entries.values():
            e.delete(0, tk.END)


if __name__ == "__main__":
    app = WrestlerTracker()
    app.mainloop()