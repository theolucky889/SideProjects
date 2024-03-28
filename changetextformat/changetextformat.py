class StringConverter:
    def __init__(self, string):
        self.string = string.replace(' ', '')

    def sentence(self):
        if not self.string.isalpha():
            return '{Invalid input: only letters allowed}'
        
        snake_case_string = self.string[0].lower()
        for char in self.string[1:]:
            if char.isupper() and snake_case_string:
                snake_case_string += '_'
                snake_case_string += char.lower()
            else:
                snake_case_string += char.lower()
        return snake_case_string
    
max_length = 15

results = []

while True:
    user_input = input('Enter a sentence to convert to snake case (max = 15字) or type "end" to close program: ')
    if user_input.lower() == 'end':
        break
    
    limit_input = user_input[:max_length]
    sentence_input = StringConverter(limit_input)
    result = sentence_input.sentence()
    results.append(result)

for result in results:
    print(result)
