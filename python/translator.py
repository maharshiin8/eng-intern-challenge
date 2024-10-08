# -*- coding: utf-8 -*-
"""translator.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FExIazPX2OtiC99FXQPtAUsWrTB-ijFk
"""

import sys

# Braille mappings (simplified for demonstration)
braille_alphabet = {
    'a': 'O.....', 'b': 'O.O...', 'c': 'OO....', 'd': 'OO.O..', 'e': 'O..O..',
    'f': 'OOO...', 'g': 'OOOO..', 'h': 'O.OO..', 'i': '.OO...', 'j': '.OOO..',
    'k': 'O...O.', 'l': 'O.O.O.', 'm': 'OO..O.', 'n': 'OO.OO.', 'o': 'O..OO.',
    'p': 'OOO.O.', 'q': 'OOOOO.', 'r': 'O.OOO.', 's': '.OO.O.', 't': '.OOOO.',
    'u': 'O...OO', 'v': 'O.O.OO', 'w': '.OOO.O', 'x': 'OO..OO', 'y': 'OO.OOO',
    'z': 'O..OOO',
    ' ': '......',  # Space
    'cap': '.....O',  # Capital marker
    'num': '.O.OOO'   # Number marker
}

braille_numbers = {
    '1': 'O.....', '2': 'O.O...', '3': 'OO....', '4': 'OO.O..', '5': 'O..O..',
    '6': 'OOO...', '7': 'OOOO..', '8': 'O.OO..', '9': '.OO...', '0': '.OOO..'
}

# Reverse lookup for decoding Braille back to English
reverse_braille_alphabet = {v: k for k, v in braille_alphabet.items()}
reverse_braille_numbers = {v: k for k, v in braille_numbers.items()}

def is_braille(input_str):
    """ Determine if the input string is Braille (contains only 'O' and '.') """
    return all(char in "O." for char in input_str)

def validate_braille_input(braille_str):
    """ Ensure Braille input has valid length and characters """
    if len(braille_str) % 6 != 0:
        raise ValueError("Invalid Braille input length. Braille must be divisible by 6.")
    if not is_braille(braille_str):
        raise ValueError("Invalid Braille characters. Only 'O' and '.' are allowed.")

def translate_to_braille(english_str):
    """ Translate English string to Braille """
    result = []
    for char in english_str:
        if char.isupper():
            result.append(braille_alphabet['cap'])  # Capital marker
            char = char.lower()
        if char.isdigit():
            result.append(braille_alphabet['num'])  # Number marker
            result.append(braille_numbers[char])
        else:
            result.append(braille_alphabet.get(char, '......'))  # Space or letters
    return ''.join(result)

def translate_to_english(braille_str):
    """ Translate Braille string to English """
    result = []
    i = 0
    length = len(braille_str)
    is_cap = False
    is_num = False

    while i < length:
        braille_char = braille_str[i:i+6]
        if braille_char == braille_alphabet['cap']:
            is_cap = True
            i += 6
            continue
        elif braille_char == braille_alphabet['num']:
            is_num = True
            i += 6
            continue

        if is_num:
            result.append(reverse_braille_numbers.get(braille_char, ' '))
            is_num = False
        else:
            char = reverse_braille_alphabet.get(braille_char, ' ')
            if is_cap:
                char = char.upper()
                is_cap = False
            result.append(char)
        i += 6

    return ''.join(result)

def main():
    if len(sys.argv) != 2:
        print("Usage: python translator.py <string_to_translate>")
        return

    input_str = sys.argv[1]

    try:
        if is_braille(input_str):
            validate_braille_input(input_str)
            print(translate_to_english(input_str))
        else:
            print(translate_to_braille(input_str))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()