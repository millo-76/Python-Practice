### wrestling stats tracker

class Wrestler:
    def __init__(self, name, weight_class):
        self.name = name
        self.weight_class = weight_class
        self.matches = []
    
    def add_match(self, opponent, result, score):
        match = {
            'opponent': opponent,
            'result': result,
            'score': score
        }
        self.matches.append(match)
    
    def get_record(self):
        wins = sum(1 for match in self.matches if match['result'] == 'win')
        losses = sum(1 for match in self.matches if match['result'] == 'loss')
        return wins, losses
    
    def display_stats(self):
        wins, losses = self.get_record()
        print(f"Wrestler: {self.name}, Weight Class: {self.weight_class}")
        print(f"Record: {wins} Wins - {losses} Losses")
        print("Matches:")
        for match in self.matches:
            print(f"  Opponent: {match['opponent']}, Result: {match['result']}, Score: {match['score']}")

# Example usage
if __name__ == "__main__":
    wrestler1 = Wrestler("John Doe", "Heavyweight")
    wrestler1.add_match("Opponent A", "win", 5)
    wrestler1.add_match("Opponent B", "loss", 3)
    wrestler1.display_stats()