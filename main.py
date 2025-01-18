print("// CAESAR MESSAGE ENCODE //\n //This Is a message encoder. Type in help() for more info.")

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
def message_decode(message, offset):
    decoded_message = ""
    for word in message:
        for let in word:
            if let in ALPHABET:
                letfound = ALPHABET.find(let)
                if len(ALPHABET[letfound:]) - 1 < offset:
                    new_index = offset - len(ALPHABET[letfound:])
                    decoded_message += ALPHABET[new_index]
                else:
                    decoded_message += ALPHABET[letfound+offset]

            else:
                decoded_message += let
    return decoded_message

def message_encode(message, offset):
    encoded_message = ""
    for word in message:
        for let in word:
            if let in ALPHABET:
                letfound = ALPHABET.find(let)
                encoded_message += ALPHABET[letfound-offset]
            else:
                encoded_message += let
    return encoded_message

def help():
    print("""

**------------**    HELP    **------------**
How it works?
    Encoding and decoding process is fairly simple. In your encode/decode command, you include your message and offset as a parameter inside the\n
    parenthesis and proceed. Based on your chosen function, e.g. message_encode or message_decode, the program will decode or encode\n
    your message. Encoding/decoding process looks like so: \n
          \n
            For every letter, the program will shift the letter to the left (towards A in alphabet). For example, if there is letter\n
            "h" and offset 2, the encoded letter will be "f" - shifted left towards the start of the alphabet. Opposite works for the\n
            decode function.
          

    Function analysis:
        
        message_decode()
            param1: accepts a string type value. Include your message you want to decode as this parameter.
            param2: accepts an integer, which will offset every supported letter to the right by the offset amount\n
           (towards the end of the alphabet)

          return: returns "decoded_message", a str type.
        
        
        message_encode()
            param1: accepts a string type value. Include your message you want to decode as this parameter.
            param2: accepts an integer, which will offset every supported letter to the left by the offset amount\n
            (towards the start of the alphabet)

            return: returns "encoded_message", a str type.
        
          

        
        Enjoy your use.
""")