import argparse

def arg():
    parser = argparse.ArgumentParser()
    parser.parse_args()
    parser.add_argument("file", help="increase output file")
    args = parser.parse_args()
    return args

def main(fi):
    #1st read input
    contents = ""
    with open('fi', 'r') as f:
        contents = f.read()
    print(contents)

if __name__ == "__main__":
    args = arg()

    main(args.file)