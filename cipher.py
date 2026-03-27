message = input("Enter your message: ")
shift = int(input("Enter the shift number: "))

encoded = ""

for char in message:
    asciiChar = ord(char)
    shiftedChar = asciiChar + shift
    finalChar = chr(shiftedChar)
    encoded += finalChar

print(encoded)