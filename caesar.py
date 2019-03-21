from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    newText = ''
    for i in text:
        newText += rotate_character(i, rot)
    return newText

def main():
    from sys import argv, exit
    if argv[1].isdigit() == False:
        print("usage: python caesar.py n")
        exit()
    message = input("Type a message:\n")
    jump = int(argv[1])
    print(encrypt(message, jump))

if __name__ == "__main__":
    main()
