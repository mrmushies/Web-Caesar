
def alphabet_position(char):
    lowerc = string.ascii_lowercase
    upperc = string.ascii_uppercase
    if char in lowerc:
        return lowerc.index(char)
    elif char in upperc:
        return upperc.index(char)

def rotate_character(char, rot):
    lowerc = string.ascii_lowercase
    upperc = string.ascii_uppercase
    if char in lowerc:
        return lowerc[(alphabet_position(char) + rot) %26]
    if char in upperc:
        return upperc[(alphabet_position(char) + rot) %26]

def encrypt(text, rot):
    new = ""
    for c in text:
        if c.isalpha():
            new += rotate_character(c, rot)
        else:
            new += c
    return new

def main():
    msg = input("Type a message:")
    print(encrypt(msg, 13))

if __name__=="__main__":
    main()
