Wrestler Tracker
=================

A small Tkinter GUI to record wrestler data (name, team, weight class, wins, losses, notes) and save to a CSV file `wrestlers.csv`.

Files
- `wrestler_tracker.py` — Main GUI application.
- `wrestlers.csv` — Created automatically when you save the first record.

Usage
1. Open a terminal and run the app with the workspace Python (or your chosen interpreter):

```powershell
"C:/Users/marja/OneDrive/Desktop/Code/Pyton Workspace/python.exe" "Personal Programs/wrestler-tracker/wrestler_tracker.py"
```

2. Fill the fields and click Save. Records are appended to `wrestlers.csv` in the same folder.
3. Click "Show records" to view saved entries. Click "Export CSV..." to save a copy elsewhere.

Notes
- The app uses only the Python standard library (Tkinter, csv).
- If you prefer another GUI toolkit (PyQt, wxPython), I can adapt the code.

License
MIT
