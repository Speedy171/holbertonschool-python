#!/usr/bin/python3
from sys import argv


def main():
    sum = 0
    for index in range(1, len(argv)):
        sum += int(argv[index])
    print(sum)

if __name__ == '__main__':
    main()
