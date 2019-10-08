code_mapping = {
    1 : "wink",
    2 : "double blink",
    4 : "close your eyes",
    8 : "jump"
}

def commands(number):
    s_code = []
    s_code = [code for key,code in code_mapping.items() if (number & key)]
    if number & 16:
        s_code.reverse()
    return s_code

def secret_code(actions):
    cmd = 0
    reverse = False
    if len(actions) > 1 and actions[0] != code_mapping[1]:
        reverse = True
    for action in actions:
        print(action)
        for key,code in code_mapping.items():
            if action == code:
                print(key)
                cmd = cmd | key
    if reverse:
        cmd = cmd & 16
    return cmd