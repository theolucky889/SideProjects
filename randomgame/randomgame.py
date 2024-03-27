import random

class Player:
    def __init__(self, name, numbers):
        self.name = name
        self.numbers = set(numbers)
        
    def remove_number(self, number):
        if number in self.numbers:
            self.numbers.remove(number)
            
    def has_numbers(self):
        return bool(self.numbers)

class RandomNumberGame:
    def __init__(self, num_players, number_range=(1, 50)):
        self.players = []
        self.number_range = number_range
        self.initialize_players(num_players)
        
    def initialize_players(self, num_players):
        all_numbers = list(range(self.number_range[0], self.number_range[1] + 1))
        random.shuffle(all_numbers)
    
        for i in range(num_players):
            if len(all_numbers) < 6:
                raise ValueError('Not enough unique numbers available to assign to all players')
            
            chosen_numbers = [all_numbers.pop() for _ in range(6)]
            self.players.append(Player(f'Player {i + 1}', chosen_numbers))
    
    def start_game(self):
        while True:
            for player in self.players:
                if not player.has_numbers():
                    continue
            
            random_number = random.randint(self.number_range[0], self.number_range[1])
            print(f'Spinning the randomizer: {random_number}')

            for player in self.players:
                player.remove_number(random_number)
                if not player.has_numbers():
                    print(f'{player.name} has lost all numbers and is out of the game!!!')
            
            active_players = [p for p in self.players if p.has_numbers()]
            if len(active_players) <= 1:
                return active_players

game = RandomNumberGame(50)
winners = game.start_game()
if winners:
    print(f'{winners[0].name} is the winner!!!')
else:
    print('Draw!, No players have any numbers left!')