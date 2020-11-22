import argparse
import lexer

def arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="increase output file")
    args = parser.parse_args()
    return args

def main(fi):
    #1st read input
    contents = []
    with open(fi, 'r') as f:
        for line in f:
            contents.append(line)

    t = lexer.LexerAnalyzer()
    tokens = []

    for l in contents:
        tokens.append(t.create_tokens(l))

    print(tokens)


if __name__ == "__main__":
    arg = arg()
    main(arg.file)