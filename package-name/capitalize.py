#!/usr/bin/env python3


def capitalize(text):
    first_char = text[0].upper()
    rest_substring = text[1:]
    return f'{first_char}{rest_substring}'


def main():
    print(capitalize('hello, hexlet!'))


if __name__ == '__main__':
    main()
