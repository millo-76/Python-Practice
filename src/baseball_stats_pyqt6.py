import sys
import json
import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QMessageBox, QHeaderView
)

FILE_NAME = "players.json"


def load_players():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    return {}


def save_players(players):
    with open(FILE_NAME, 'w') as f:
        json.dump(players, f, indent=4)


class BaseballStatsApp(QWidget):
    def __init__(self):
        super().__init__()
        self.players = load_players()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Baseball Stats Tracker (PyQt6)")
        self.resize(700, 400)

        layout = QVBoxLayout()

        # --- Input fields ---
        form_layout = QHBoxLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Player Name")
        self.hits_input = QLineEdit()
        self.hits_input.setPlaceholderText("Hits")
        self.ab_input = QLineEdit()
        self.ab_input.setPlaceholderText("At Bats")
        self.walks_input = QLineEdit()
        self.walks_input.setPlaceholderText("Walks")
        self.runs_input = QLineEdit()
        self.runs_input.setPlaceholderText("Runs")

        form_layout.addWidget(self.name_input)
        form_layout.addWidget(self.hits_input)
        form_layout.addWidget(self.ab_input)
        form_layout.addWidget(self.walks_input)
        form_layout.addWidget(self.runs_input)

        layout.addLayout(form_layout)

        # --- Buttons ---
        btn_layout = QHBoxLayout()
        add_btn = QPushButton("Add / Update Player")
        add_btn.clicked.connect(self.add_update_player)
        del_btn = QPushButton("Delete Player")
        del_btn.clicked.connect(self.delete_player)

        btn_layout.addWidget(add_btn)
        btn_layout.addWidget(del_btn)
        layout.addLayout(btn_layout)

        # --- Table ---
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["Name", "Hits", "At Bats", "Walks", "Runs", "Average"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        layout.addWidget(self.table)

        self.setLayout(layout)
        self.update_table()

    def add_update_player(self):
        name = self.name_input.text().strip().lower()
        if not name:
            QMessageBox.warning(self, "Error", "Player name cannot be empty.")
            return

        try:
            hits = int(self.hits_input.text())
            at_bats = int(self.ab_input.text())
            walks = int(self.walks_input.text())
            runs = int(self.runs_input.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid integers for stats.")
            return

        if at_bats < hits:
            QMessageBox.warning(self, "Error", "At Bats cannot be less than Hits.")
            return

        # Incremental update if exists
        if name in self.players:
            self.players[name]['hits'] += hits
            self.players[name]['at_bats'] += at_bats
            self.players[name]['walks'] += walks
            self.players[name]['runs'] += runs
        else:
            self.players[name] = {
                "hits": hits,
                "at_bats": at_bats,
                "walks": walks,
                "runs": runs
            }

        # Recalculate average
        self.players[name]['average'] = round(
            self.players[name]['hits'] / self.players[name]['at_bats'], 3
        ) if self.players[name]['at_bats'] > 0 else 0.0

        save_players(self.players)
        self.update_table()
        self.clear_inputs()

    def delete_player(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, "Error", "Please select a player to delete.")
            return

        name = self.table.item(selected, 0).text().lower()
        del self.players[name]
        save_players(self.players)
        self.update_table()

    def update_table(self):
        self.table.setRowCount(0)
        for name, stats in sorted(self.players.items()):
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(str(stats["hits"])))
            self.table.setItem(row, 2, QTableWidgetItem(str(stats["at_bats"])))
            self.table.setItem(row, 3, QTableWidgetItem(str(stats["walks"])))
            self.table.setItem(row, 4, QTableWidgetItem(str(stats["runs"])))
            self.table.setItem(row, 5, QTableWidgetItem(f"{stats['average']:.3f}"))

    def clear_inputs(self):
        self.name_input.clear()
        self.hits_input.clear()
        self.ab_input.clear()
        self.walks_input.clear()
        self.runs_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BaseballStatsApp()
    window.show()
    sys.exit(app.exec())
