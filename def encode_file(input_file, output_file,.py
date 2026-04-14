for char in message:
        asciiChar = ord(char)
        shiftedChar = asciiChar + shift
        finalChar = chr(shiftedChar)
        encoded += finalChar