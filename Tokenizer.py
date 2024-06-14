import re

class Tokenizer:
    def __init__(self, expression):
        self.expression = expression
        self.tokens = self.tokenize(expression)
    
    def tokenize(self, expression):
        token_pattern = re.compile(r'(\d+|[+\-*/^(){}\[\]])')
        return token_pattern.findall(expression)

    def get_tokens(self):
        return self.tokens