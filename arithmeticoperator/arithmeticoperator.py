class arithmetic:
    def __init__(self, expression):
        self.expression = expression
        
    def operators(self):
        if "=" in self.expression:
            return 'Invalid expression: "=" sign is not supported'
        else:
            corrected_expression, suggestion = self.suggest_corrections(self.expression)
        if suggestion:
            return f'Did you mean: {corrected_expression}?'
        try:
            return eval(self.expression)
        except (SyntaxError, ZeroDivisionError, NameError, TypeError):
            return 'Invalid Expression'
    
    def suggest_corrections(self, expression):
        import re
        suggested_expression = re.sub(r'(\d)(\()', r'\1*\2', expression)
        if suggested_expression != expression:
            return suggested_expression, True
        else:
            return expression, False
while True:    
    user_input = input('Enter a arithmetic expression or type "end" to quit: ')
    if user_input == 'end':
        print('Exiting Program')
        break
    arithmetic_expression = arithmetic(user_input)
    result = arithmetic_expression.operators()
    print(f'The result of the expression {user_input} is: {result}')
        
    