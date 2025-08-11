import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

FILE_NAME = "players.json"

players = {}

def load_players():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return {}

players = load_players()

def save_players(players):
    with open(FILE_NAME, 'w') as file:
        json.dump(players, file, indent=4)

def submit():
    name = name_entry.get().strip().lower()
    if not name:
        messagebox.showerror("Input Error", "Player name cannot be empty.")
        return
    
    try:
        hits = int(hits_entry.get())
        at_bats = int(at_bats_entry.get())
        walks = int(walks_entry.get())
        runs = int(runs_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for hits, at-bats, walks, and runs.")
        return
    
    if at_bats < hits:
        messagebox.showerror("Input Error", "At-bats cannot be less than hits.")
        return
    
    avg = round(hits / at_bats, 3) if at_bats > 0 else 0.0

    if name in players:
        players[name]['hits'] += hits
        players[name]['at_bats'] += at_bats
        players[name]['walks'] += walks
        players[name]['runs'] += runs
        players[name]['average'] = round((players[name]['hits'] / players[name]['at_bats']), 3) if players[name]['at_bats'] > 0 else 0
    else:
        players[name] = {
            'hits': hits,
            'at_bats': at_bats,
            'walks': walks,
            'runs': runs,
            'average': avg
        }
    update_tree()
    clear_entries()
    save_players(players)
    messagebox.showinfo("Success", f"Player {name} added successfully.")

def update_tree():
    for row in tree.get_children():
        tree.delete(row)
    for name in sorted(players.keys()):
        stats = players[name]
        tree.insert("", "end", values=(name, stats['hits'], stats['at_bats'], stats['walks'], stats['runs'], f"{stats['average']:.3f}"))

def clear_entries():
    name_entry.delete(0, tk.END)
    hits_entry.delete(0, tk.END)
    at_bats_entry.delete(0, tk.END)
    walks_entry.delete(0, tk.END)
    runs_entry.delete(0, tk.END)

def delete_player():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a player to delete.")
        return
    name = tree.item(selected_item, 'values')[0]
    del players[name]
    update_tree()
    save_players(players)
    messagebox.showinfo("Success", f"Player {name} deleted successfully.")

root = tk.Tk()
root.title("Baseball Stats Tracker")

entry_frame = ttk.Frame(root)
entry_frame.pack(padx=10, pady=10)

tk.Label(entry_frame, text="Player Name:").grid(row=0, column=0, sticky=tk.W)
name_entry = ttk.Entry(entry_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Label(entry_frame, text="Hits:").grid(row=1, column=0, sticky=tk.W)
hits_entry = ttk.Entry(entry_frame)
hits_entry.grid(row=1, column=1, padx=5, pady=5)
tk.Label(entry_frame, text="At Bats:").grid(row=2, column=0, sticky=tk.W)
at_bats_entry = ttk.Entry(entry_frame)
at_bats_entry.grid(row=2, column=1, padx=5, pady=5)
tk.Label(entry_frame, text="Walks:").grid(row=3, column=0, sticky=tk.W)
walks_entry = ttk.Entry(entry_frame)
walks_entry.grid(row=3, column=1, padx=5, pady=5)
tk.Label(entry_frame, text="Runs:").grid(row=4, column=0, sticky=tk.W)
runs_entry = ttk.Entry(entry_frame)
runs_entry.grid(row=4, column=1, padx=5, pady=5)

submit_button = ttk.Button(entry_frame, text="Submit", command=submit)
submit_button.grid(row=5, columnspan=2, pady=10)

delete_button = ttk.Button(entry_frame, text="Delete Player", command=delete_player)
delete_button.grid(row=6, columnspan=2, pady=5)

tree = ttk.Treeview(root, columns=("Name", "Hits", "At Bats", "Walks", "Runs", "Average"), show='headings')
tree.heading("Name", text="Name")
tree.heading("Hits", text="Hits")
tree.heading("At Bats", text="At Bats")
tree.heading("Walks", text="Walks")
tree.heading("Runs", text="Runs")
tree.heading("Average", text="Average")
tree.column("Average", width=80, anchor='center')
tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
tree.bind("<Double-1>", lambda event: messagebox.showinfo("Player Info", "Double-click to view player details."))

root.mainloop()
save_players(players)