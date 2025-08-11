import os
import json

FILE_NAME = 'player_stats.json'

def main():
    players = load_players()
    if not players:
        print("No player data found. Starting with an empty list.")
    else:
        print(f"Loaded {len(players)} players from {FILE_NAME}.")

    while True:
        print("Batter Statistics Tracker")
        print("1. Add Player")
        print("2. Update Player")
        print("3. Display Players")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            enter_stats(players)
        elif choice == '2':
            if not players:
                print("No players available to update.")
                continue
            name = input("Enter player's name to update: ").strip().lower()
            if name not in players:
                print("Player not found.")
            else:
                update_stats(players, name)
        elif choice == '3':
            display_players(players)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


def enter_stats(players):
    name = input("Enter player's name: ").strip().lower()
    if name in players:
        print("Player already exists.")
        return

    try:
        hits = int(input("Enter number of hits: "))
        at_bats = int(input("Enter number of at-bats: "))
        walks = int(input("Enter number of walks: "))
        runs = int(input("Enter number of runs: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for hits, at-bats, walks, and runs.")
        return
    
    if at_bats < hits:
        print("At-bats cannot be less than hits.")
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

    save_players(players)
    print(f"Player {name} added.")

def update_stats(players, name):

    if name not in players:
        print("Player not found.")
        return
    
    print(f"Updating stats for {name}.")

    try:
        hits = int(input("Enter number of hits: "))
        at_bats = int(input("Enter number of at-bats: "))
        walks = int(input("Enter number of walks: "))
        runs = int(input("Enter number of runs: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for hits, at-bats, walks, and runs.")
        return
    
    if at_bats < hits:
        print("At-bats cannot be less than hits.")
        return
    
    avg = round(hits / at_bats, 3) if at_bats > 0 else 0.0

    players[name]['hits'] += hits
    players[name]['at_bats'] += at_bats
    players[name]['walks'] += walks
    players[name]['runs'] += runs
    players[name]['average'] = round((players[name]['hits'] / players[name]['at_bats']), 3) if players[name]['at_bats'] > 0 else 0 

    save_players(players)
    print(f"Player {name}'s stats updated.")

def display_players(players):
    if not players:
        print("No players to display.")
        return

    print("\nPlayer Statistics:")
    for name, stats in players.items():
        print(f"Name: {name}, Hits: {stats['hits']}, At-Bats: {stats['at_bats']}, Walks: {stats['walks']}, Runs: {stats['runs']}, Average: {stats['average']:.3f}")
    print()

def load_players():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return {}

def save_players(players):
    with open(FILE_NAME, 'w') as file:
        json.dump(players, file, indent=4)
    print(f"Player data saved to {FILE_NAME}.")

if __name__ == "__main__":
    main()