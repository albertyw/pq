#!/usr/bin/env python3

import fileinput


def read_input():
    data = ''
    for line in fileinput.input():
        data += line
    return data


def newline(symbol, indentation):
    print_output(symbol)
    print_output("\n")
    spacing = ' ' * indentation * 2
    print_output(spacing)


def format_parens(data):
    indentation = 0
    symbol = ''
    for char in data:
        if char.strip() == '':
            newline(symbol, indentation)
            symbol = ''
        if char in [')']:
            indentation -= 1
            newline(symbol, indentation)
            symbol = ''
        symbol += char.strip()
        if char in ['(']:
            indentation += 1
            newline(symbol, indentation)
            symbol = ''
    if indentation != 0:
        indentation = 0
        newline('', indentation)


def print_output(output):
    print(output, end='')


if __name__ == '__main__':
    format_parens(read_input())
