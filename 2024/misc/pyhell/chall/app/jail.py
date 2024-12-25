import re
import builtins
import sys

def safe_eval(user_input):
    safe_builtins = {
        "__builtins__": {name: getattr(builtins, name) for name in ['print', 'int', 'float', '__import__', 'getattr', 'chr']}
    }

    try:
        exec(user_input, safe_builtins, {})
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def jail():
    ascii_art = """
                                                                                                        _..._                                  
                                .---..---.                                                           .-'_..._''.                    .---..---. 
   .              __.....__     |   ||   |          .--.   _..._                                   .' .'      '.\\     __.....__     |   ||   | 
 .'|          .-''         '.   |   ||   |          |__| .'     '.                                / .'            .-''         '.   |   ||   | 
<  |         /     .-''"'-.  `. |   ||   |          .--..   .-.   .                              . '             /     .-''"'-.  `. |   ||   | 
 | |        /     /________\\   \\|   ||   |          |  ||  '   '  |              __              | |            /     /________\\   \\|   ||   | 
 | | .'''-. |                  ||   ||   |          |  ||  |   |  |           .:--.'.            | |            |                  ||   ||   | 
 | |/.'''. \\\\    .-------------'|   ||   |          |  ||  |   |  |          / |   \\ |           . '            \\\\    .-------------'|   ||   | 
 |  /    | | \\    '-.____...---.|   ||   |          |  ||  |   |  |          `" __ | |            \\ '.          .\\    '-.____...---.|   ||   | 
 | |     | |  `.             .' |   ||   |          |__||  |   |  |           .'.''| |             '. `._____.-'/ `.             .' |   ||   | 
 | |     | |    `''-...... -'   '---''---'              |  |   |  |          / /   | |_              `-.______ /    `''-...... -'   '---''---' 
 | '.    | '.                                           |  |   |  |          \\ \\._,\\ '/                       `                                
 '---'   '---'                                          '--'   '--'           `--'  `"                                                         
!! Even Michael Scofield can not escape this .
    """
    print(ascii_art)

    max_input_length = 553

    while True:
        user_input = input(">>> ")

        if len(user_input) > max_input_length:
            print("Bro chill !!! That's kinda long")
            continue

        blacklist = ['exec', 'eval', 'os', 'sys', 'subprocess', 'file', 'open', 'register', 'setattr', 'input', 'mro', 'globals', 'class', 'getitem', 'breakpoint', '_', '.','[',']']

        for block in blacklist:
            if block in user_input:
                print(f"No no {block} is not allowed in here")
                break
        else:
            safe_eval(user_input)

if __name__ == "__main__":
    jail()
