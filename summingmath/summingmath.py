class Number:
    def __init__(self, number):
        self.number = number
    
    def number_root(self):
        result = self.number
        while result > 9:
            result = sum(int(digit) for digit in str(result))
        return result
    
user_input = input('Enter a positive number: ')
number = int(user_input)

number_result = Number(number)
result = number_result.number_root()
print(result)
