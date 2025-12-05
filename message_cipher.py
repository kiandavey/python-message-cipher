def generate_keys():
    # create keys string
    keys = "abcdefghijklmnopqrstuvwxyz0123456789.,!?@#$%^&*()[]{}<>+-=_/\\| "

    # autogenerate the values string by offsetting original string
    values = keys[-1] + keys[0:-1]

    # create two dictionaries
    dict_encrypt = dict(zip(keys, values))
    dict_decrypt = dict(zip(values, keys))

    #user input 'the message' and mode
    msg = input("Enter your secret message : ")
    mode = input("Choose mode: encode (e) or decrypt as default : ")

    # run encode or decode
    if mode.lower() == 'e':
        new_msg = ''.join([dict_encrypt.get(letter, letter) for letter in msg.lower()])
        print("Encoded Message : " + new_msg)
    else:
        new_msg = ''.join([dict_encrypt.get(letter, letter) for letter in msg.lower()])
        print("Decoded Message : " + new_msg)

generate_keys()