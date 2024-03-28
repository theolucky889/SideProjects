import random

class Player:
    def __init__(self, name, numbers):
        self.name = name
        self.numbers = list(numbers)
        
    def remove_number(self, number):
        if number in self.numbers:
            self.numbers.remove(number)
            print(f"{self.name}'s remaining numbers: {list(self.numbers)}")
            
    def has_numbers(self):
        return bool(self.numbers)

class RandomNumberGame:
    def __init__(self, num_players, numbers_per_player=6):
        self.players = []
        self.numbers_per_player = numbers_per_player
        self.min_number = 1
        self.max_number = num_players * numbers_per_player
        self.numbers_in_play = set()
        self.initialize_players(num_players)
        
    def initialize_players(self, num_players):
        all_numbers = list(range(self.min_number, self.max_number + 1))
        random.shuffle(all_numbers)

        for i in range(num_players):
            if len(all_numbers) < self.numbers_per_player:
                raise ValueError('Not enough unique numbers available to assign to all players')
            
            chosen_numbers = [all_numbers.pop() for _ in range(self.numbers_per_player)]
            player = (Player(f'Player {i + 1}', chosen_numbers))
            self.players.append(player)
            self.numbers_in_play.update(player.numbers)
    
    def show_numbers(self):
        for player in self.players:
            print(f'{player.name}: {list(player.numbers)}')
    
    def start_game(self):
        print('Starting the game')

        while len(self.numbers_in_play) > 0:
            for player in self.players:
                if not player.has_numbers():
                    continue
                
                input(f"{player.name}'s turn to spin the randomizer. Press Enter")
                random_number = random.choice(list(self.numbers_in_play))
                print(f'{player.name} is spinning the randomizer: {random_number}')

                for players in self.players:
                    players.remove_number(random_number)

                if not any(random_number in players.numbers for players in self.players):
                    self.numbers_in_play.discard(random_number)

                if not player.has_numbers():
                    print(f'{player.name} has lost all numbers and is out of the game!!!')

            active_players = [players for players in self.players if players.has_numbers()]
            if len(active_players) == 1:
                print(f'{active_players[0].name} is the winner!!!')
                return active_players
            elif len(active_players) == 0:
                print('Draw!, No players have any numbers left!')
                break
            
    def show_players_numbers(self):
        for player in self.players:
            print(f'{player.name}: {player.numbers}')

user_input = int(input('How many players will join the game?: '))
game = RandomNumberGame(user_input)
game.show_numbers()
game.start_game()
