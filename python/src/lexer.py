import re
class LexerAnalyzer:
    def __init__(self):
        # self.token = Token()
        self.reserved_words = {}
        with open('Tokens', 'r') as f:
            for line in f:
                key, value = line.split(",")
                reserved_words[key] = value

# class Token:
#     def __init__(self):
#         self.reserved_words = {}
#         with open('Tokens', 'r') as f:
#             for line in f:
#                 key, value = line.split(",")
#                 reserved_words[key] = value
        


