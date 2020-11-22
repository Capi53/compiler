import re

pattern1 = '[0-9]'

class LexerAnalyzer:
    def __init__(self):
        # self.token = Token()
        self.reserved_words = {}
        with open('Tokens', 'r') as f:
            for line in f:
                key, value = line.rstrip('\n').split(",")
                self.reserved_words[key] = value
    
    def create_tokens(self, li):
        self.li = li
        self.ts = []
        for l in self.li.split():
            if l in [v for k,v in self.reserved_words.items()]:
                key = [k for k,v in self.reserved_words.items() if v == l]
                if key:
                    self.ts.append('<'+ key[0] +','+ l +'>')
            elif re.match(pattern1, l):
                self.ts.append('<INT,' + l + '>')
            else:
                self.ts.append('<VARIABLE,'+ l +'>')
        return self.ts

# class Token:
#     def __init__(se lf):
#         self.reserved_words = {}
#         with open('Tokens', 'r') as f:
#             for line in f:
#                 key, value = line.split(",")
#                 reserved_words[key] = value
        


