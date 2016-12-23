#!/usr/bin/env python3

import fileinput


def read_input():
    data = ''
    for line in fileinput.input():
        data += line
    return data


def newline(symbol, indentation):
    spacing = ' ' * indentation * 2
    output = symbol + "\n" + spacing
    print_output(output)
    return output


def format_parens(data):
    output = ''
    indentation = 0
    symbol = ''
    for char in data:
        if char.strip() == '':
            output += newline(symbol, indentation)
            symbol = ''
        if char in [')']:
            indentation -= 1
            output += newline(symbol, indentation)
            symbol = ''
        symbol += char.strip()
        if char in ['(']:
            indentation += 1
            output += newline(symbol, indentation)
            symbol = ''
    if output[-1] != "\n":
        output += newline('', 0)
    return output


def print_output(output):
    print(output, end='')


if __name__ == '__main__':
    format_parens(read_input())
