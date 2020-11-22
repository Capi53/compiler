import argparse
import lexer

def arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="increase output file")
    args = parser.parse_args()
    return args

def main(fi):
    #1st read input
    contents = ""
    with open(fi, 'r') as f:
        contents = f.read()
    print(contents)

if __name__ == "__main__":
    arg = arg()
    main(arg.file)