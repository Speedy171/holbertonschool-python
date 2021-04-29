#!/usr/bin/python3
from sys import argv


def main():
    arguments = len(argv) - 1
    if arguments == 0:
        print('{} arguments.'.format(arguments))
    elif arguments == 1:
        print('1 argument:')
        print('1: {}'.format(argvs[1]))
    else:
        print('{} arguments:'.format(arguments))
        for argument in range(0, arguments):
            print('{}: {}'.format(argument + 1, argv[argument + 1]))
if __name__ == '__main__':
    main()
