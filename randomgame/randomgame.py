import random

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

class RandomNumberGame:
    def __init__(self, num_players):
        self.players = []
        self.initialize_players(num_players)
            
    def initialize_players(self, num_players):
        for i in range(num_players):
            dice_roll = [random.randint(1, 6) for _ in range(6)]
            player = Player(f'Player {i + 1}', dice_roll)
            self.players.append(player)
            
    def show_dice(self):
        for player in self.players:
            print(f'{player.name}: {player.dice}')
    
    def start_game(self):
        print('Starting the game')

        while len(self.players) > 1:
            players_to_remove = []
            for player in self.players:
                if not player.has_dice():
                    continue
                
                input(f"{player.name}'s turn to roll the dice. Press Enter")
                dice_roll = random.randint(1, 6)
                print(f'{player.name} is rolling the dice: {dice_roll}')
                
                for p in self.players:
                    p.remove_number(dice_roll)
                    if not p.has_dice() and p not in players_to_remove:
                        players_to_remove.append(p)
                        
                        
            for player in players_to_remove:
                if player in self.players:
                    print(f'{player.name} has lost all dice and is out of the game!!!')
                    self.players.remove(player)

            if len(self.players) == 1:
                print(f'{self.players[0].name} is the winner!!!')
                break
            elif len(self.players) == 0:
                print('Draw!, No players have any dice left!')
                break
            
    def show_players_numbers(self):
        for player in self.players:
            print(f'{player.name}: {player.numbers}')

user_input = int(input('How many players will join the game?: '))
game = RandomNumberGame(user_input)
game.show_dice()
game.start_game()
