import random

class Player:
    def __init__(self, name, dice):
        self.name = name
        self.dice = list(dice)
        
    def remove_number(self, numbers_to_remove):
        for number in numbers_to_remove:
            while number in self.dice:
                self.dice.remove(number)
        print(f"{self.name}'s remaining numbers: {self.hide_dice_count()}")
    
    def show_dice(self):
        # dice_show = ['*' for _ in self.dice]
        print(f'{self.name} has dice: {self.hide_dice_count()}')
            
    def hide_dice_count(self):
        return ' '.join(['*' for _ in self.dice])
            
    def remove_by_category(self, category):
        categories = {
        'odd': [1, 3, 5],
        'even': [2, 4, 6],
        'big': [4, 5, 6],
        'small': [1, 2, 3],
        'red': [1, 4],
        'black': [2, 3, 5, 6],
        }
        return categories.get(category, [])
    
    def reroll_dice(self):
        self.dice = [random.randint(1, 6) for _ in range(len(self.dice))]
        print(f'{self.name} rolls the dice again: {self.hide_dice_count()}')

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
            
    
    def start_game(self):
        print('Starting the game')
        
        while len(self.players) > 1:
            players_to_remove = []
            for player in self.players:
                if not player.has_dice():
                    continue
                
                for player in self.players:
                    player.reroll_dice()
                
                # print(f"{player.name}'s turn to roll the dice. Press Enter")
                # input()
                # dice_roll = random.randint(1, 6)
                # print(f'{player.name} is rolling the dice: {dice_roll}')
                
                choice = input(f'{player.name}, choose a category to remove (odd, even, red, black, big, small): ').lower().strip()
                while choice not in ['odd', 'even', 'red', 'black', 'big', 'small']:
                    choice = input('Invalid choice, please input a correct category(odd, even, red, black, big, small)').lower().strip()
                
                numbers_to_remove = player.remove_by_category(choice)
                
                for p in self.players:
                    p.remove_number(numbers_to_remove)
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
            
    # def show_players_numbers(self):
    #     for player in self.players:
    #         print(f'{player.name}: {player.numbers}')

user_input = int(input('How many players will join the game?: '))
game = RandomNumberGame(user_input)
game.start_game()
