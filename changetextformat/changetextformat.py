class StringConverter:
    def __init__(self, string):
        self.string = string

    def sentence(self):
        if not self.string.isalpha():
            return '{Invalid input: only letters allowed}'
        
        snake_case_string = self.string[0].lower()
        for char in self.string[1:]:
            if char.isupper() and snake_case_string:
                snake_case_string += char.lower()
            else:
                snake_case_string += char.lower()
        return snake_case_string
    

user_input = input('Enter a sentence to convert to snake case: ')
sentence_input = StringConverter(user_input)
result = sentence_input.sentence()
print(result)