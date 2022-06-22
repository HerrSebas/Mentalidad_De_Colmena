#Function to encode a message
def encode(message):
    # converts message to a list
    message_list = list(message)
    # evaluates each element in message_list and encodes it
    for number in range(len(message_list)):
        if message_list[number] == "9":
            message_list[number] = "1"
        elif message_list[number] == "1":
            message_list[number] = "9"
        elif message_list[number] == "2":
            message_list[number] = "8"
        elif message_list[number] == "8":
            message_list[number] = "2"
        elif message_list[number] == "3":
            message_list[number] = "7"
        elif message_list[number] == "7":
            message_list[number] = "3"
        elif message_list[number] == "4":
            message_list[number] = "6"
        elif message_list[number] == "6":
            message_list[number] = "4"
        elif message_list[number] == "5":
            message_list[number] = "0"
        elif message_list[number] == "0":
            message_list[number] = "5"
    # empty string to save the encoded message
    encoded_message = ""
    # iterates over message_list and adds each element to encoded_message
    for element in message_list:
        encoded_message += element
    # return encoded_message
    return encoded_message
#Function to decode a message
def decode(message):
    # converts message to a list
    message_list = list(message)
    # evaluates each element in message_list and decodes it
    for number in range(len(message_list)):
        if message_list[number] == "9":
            message_list[number] = "1"
        elif message_list[number] == "1":
            message_list[number] = "9"
        elif message_list[number] == "2":
            message_list[number] = "8"
        elif message_list[number] == "8":
            message_list[number] = "2"
        elif message_list[number] == "3":
            message_list[number] = "7"
        elif message_list[number] == "7":
            message_list[number] = "3"
        elif message_list[number] == "4":
            message_list[number] = "6"
        elif message_list[number] == "6":
            message_list[number] = "4"
        elif message_list[number] == "5":
            message_list[number] = "0"
        elif message_list[number] == "0":
            message_list[number] = "5"
    # empty string to save the decoded message
    decoded_message = ""
    # iterates over message_list and adds each element to encoded_message
    for element in message_list:
        decoded_message += element
    # returns decoded_message
    return decoded_message
# initialize user´s interface
def start():
    # shows a message
    print ("""Bienvenido al buzón de espías\n
           Ingrese su mensaje: """)
    # captures user's entry and saves it in message
    message = input()
    #shows a message
    print("¿Desea codificar o decodificar su mensaje?")
    # captures user's decision (encode or decode) and saves it in decision
    decision = input("""escribe 'decode' para decodificar o 'encode' para codificar """)
    # checks if the user wants to encode or decode the message
    if decision == "decode":
        # calls decode function and prints its result
        print (decode(message))
    else:
        # calls encode function and prints its result
        print(encode(message))
# calls start function. 
start()