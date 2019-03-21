import string

def alphabet_position(letter):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    
    if letter in upper:
        position = upper.index(letter)
    if letter in lower:
        position = lower.index(letter)
    return position

def rotate_character(char, rot):
    if char.isalpha() == False:
        return char
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    old = alphabet_position(char)
    new = old + rot
    while new > 25:
        new = new - 26
    if char in upper:
        newChar = upper[new]
    if char in lower:
        newChar = lower[new]
    return newChar
