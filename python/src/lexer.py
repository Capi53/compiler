import re
class LexerAnalyzer:
    def __init__(self):
        # self.token = Token()
        self.reserved_words = {}
        with open('Tokens', 'r') as f:
            for line in f:
                key, value = line.rstrip('\n').split(",")
                self.reserved_words[key] = value
    
    def create_tokens(self, l):
        self.l = l

# class Token:
#     def __init__(se lf):
#         self.reserved_words = {}
#         with open('Tokens', 'r') as f:
#             for line in f:
#                 key, value = line.split(",")
#                 reserved_words[key] = value
        


