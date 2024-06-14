from Node import Node
from Tokenizer import Tokenizer

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    
    def parse(self):
        return self.parse_expression()

    def parse_expression(self):
        node = self.parse_term()
        while self.position < len(self.tokens) and self.tokens[self.position] in ['+', '-']:
            token = self.tokens[self.position]
            self.position += 1
            new_node = Node(token)
            new_node.left = node
            new_node.right = self.parse_term()
            node = new_node
        return node

    def parse_term(self):
        node = self.parse_factor()
        while self.position < len(self.tokens) and self.tokens[self.position] in ['*', '/']:
            token = self.tokens[self.position]
            self.position += 1
            new_node = Node(token)
            new_node.left = node
            new_node.right = self.parse_factor()
            node = new_node
        return node

    def parse_factor(self):
        node = self.parse_power()
        while self.position < len(self.tokens) and self.tokens[self.position] == '^':
            token = self.tokens[self.position]
            self.position += 1
            new_node = Node(token)
            new_node.left = node
            new_node.right = self.parse_power()
            node = new_node
        return node

    def parse_power(self):
        token = self.tokens[self.position]
        self.position += 1
        if token.isdigit():
            return Node(token)
        elif token == '(':
            node = self.parse_expression()
            self.position += 1  # Saltar el ')'
            return node
        elif token == '[':
            node = self.parse_expression()
            self.position += 1  # Saltar el ']'
            return node
        elif token == '{':
            node = self.parse_expression()
            self.position += 1  # Saltar el '}'
            return node
        else:
            raise ValueError(f"Unexpected token: {token}")