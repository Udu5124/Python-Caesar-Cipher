# Function for encryption
def encrypt(text, s):
    '''
    Encrypts given text and replaces each character by a given position.
    parameters : text - Input text to be converted to caesar cipher
                 s - replace by s characters ahead
    return : String
    '''

    result = ""

    # Iterate through plain text
    for char in text:
        #char = Character in the string

        # Encrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Skip mostly used characters
        elif (char in [' ','0','1','2','3','4','5','6','7','8','9','"','.','!','#','@','&','?','$','(',')']):
            result += char

        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


# Function for decryption
def decrypt(text, s):
    '''
        Decrypts given text and replaces each character by a given position.
        parameters : text - Cipher text to be converted to Plain text
                     s - replace by s characters ahead
        return : String
        '''

    result = ""

    # Iterate through Cipher text
    for char in text:
        #char = Character in the string

        # Decrypt uppercase characters in plain text
        if (char.isupper()):
            result += chr((ord(char) - s - 65) % 26 + 65)
        # Skip mostly used characters
        elif (char in [' ','0','1','2','3','4','5','6','7','8','9','.','.','!','#','@','&','?','$','(',')']):
            result += char
        # Decrypt lowercase characters in plain text
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)

    return result


# Take shift pattern number input
s = 0
check = True
while (check):
    s = input("Enter Shift Pattern Number (2-9):")
    if s in ['2','3','4','5','6','7','8','9']:
        check = False
    else:
        print('Please enter value between (2 to 9)')

#Repeat until you get a valid input
while True:
    choice  = input('Press E for Encryption OR D for Decryption :')

    # For encryption
    if choice in ["E","e"]:
        text = input('Enter your message to be encrypted :\n')

        print("Plain Text : " + text)
        print("Shift pattern : " + str(s))
        print("Cipher: " + encrypt(text, int(s)))

        break

    # For decryption
    elif choice in ["D","d"]:
        text = input('Enter your message to be decrypted :\n')

        print("Cipher Text : " + text)
        print("Shift pattern : " + str(s))
        print("Original text: " + decrypt(text, int(s)))

        break

    # When choice is not valid
    else:
        print('Enter a valid input !!!')