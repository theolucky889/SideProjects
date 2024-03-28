class Player:
    def __init__(self, name, dice):
        self.name = name
        self.dice = list(dice)

    def remove_number(self, number):
        while number in self.dice:
            self.dice.remove(number)
        print(f"{self.name}'s remaining numbers: {self.dice}")
    
    def has_dice(self):
        return bool(self.dice)
        
class DiceGame:
    def __init__(self, num_players):
        self.players = []
        self.initialize_players(num_players)
    def initializer_players(self, num_players):
        for