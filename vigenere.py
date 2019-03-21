from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    newText = ''
    keyPosition = 0
    for i in text:
        keyRot = alphabet_position(key[keyPosition])
        newText += rotate_character(i, keyRot)
        if i.isalpha():
            keyPosition += 1
        if keyPosition == len(key):
            keyPosition = 0
    return newText

def main():
    from sys import argv, exit
    if argv[1].isalpha() == False:
        print("usage: python vigenere.py keyword")
        exit()
    message = input("Type a message:\n")
    jump = argv[1]
    print(encrypt(message, jump))

if __name__ == "__main__":
    main()
