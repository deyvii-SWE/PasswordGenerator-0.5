
# imports
from secrets import choice
import string
import pyperclip

# classes
class Interface():
    # this time the interface gonna store the password pattern settings
    def __init__(self):
        self.alphabet_stats = True
        self.punctuations_stats = True
        self.password_size = 15
        self.board_size = 40
        self.password = ""

    # displays
    # main menu
    def display_main_menu(self):
        print("+ " + ("-"*(self.board_size)) + " +")
        print(f"| {f'PASSWORD GENERATOR':^{self.board_size}} |")
        print("+ " + ("-"*(self.board_size)) + " +")
        print("| " + (" "*self.board_size) + " |")
        print(f"| {f' 1. Generate':<{self.board_size}} |")
        print(f"| {f' 2. Settings':<{self.board_size}} |")
        print(f"| {f' 3. Save (Not Working)':<{self.board_size}} |")
        print(f"| {f' 4. Exit':<{self.board_size}} |")
        print("| " + (" "*self.board_size) + " |")
        print("+ " + ("-"*(self.board_size)) + " +")

    # settings menu
    def display_settings_menu(self):
        print("+ " + ("-"*(self.board_size)) + " +")
        print(f"| {f'PASSWORD GENERATOR':^{self.board_size}} |")
        print("+ " + ("-"*(self.board_size)) + " +")
        print("| " + (" "*self.board_size) + " |")
        print(f"| {f' 1. Alphabet ({"ON" if self.alphabet_stats else "OFF"})':<{self.board_size}} |")
        print(f"| {f' 2. Punctuations ({"ON" if self.punctuations_stats else "OFF"})':<{self.board_size}} |")
        print(f"| {f' 3. Size ({self.password_size})':<{self.board_size}} |")
        print(f"| {f' 4. Exit':<{self.board_size}} |")
        print("| " + (" "*self.board_size) + " |")
        print("+ " + ("-"*(self.board_size)) + " +")

    # shows the password menu
    def display_password_generated(self):
        print("+ " + ("-"*(self.board_size)) + " +")
        print(f"| {f'PASSWORD GENERATOR':^{self.board_size}} |")
        print("+ " + ("-"*(self.board_size)) + " +")
        print("| " + (" "*self.board_size) + " |")
        print(f"| {f' Password: {self.password}':<{self.board_size}} |")
        print("| " + (" "*self.board_size) + " |")
        print("+ " + ("-"*(self.board_size)) + " +")
        print("| " + (" "*self.board_size) + " |")
        print(f"| {f' 1. Generate':<{self.board_size}} |")
        print(f"| {f' 2. Copy':<{self.board_size}} |")
        print(f"| {f' 3. Exit':<{self.board_size}} |")
        print("| " + (" "*self.board_size) + " |")
        print("+ " + ("-"*(self.board_size)) + " +")

    # invalid option message
    def display_invalid_option(self):
        print("+ " + ("-"*(self.board_size)) + " +")
        print("| " + (" "*self.board_size) + " |")
        print(f"| {f' Please, insert an valid option.':<{self.board_size}} |")
        print("| " + (" "*self.board_size) + " |")
        print("+ " + ("-"*(self.board_size)) + " +")
        print()
        input("...")

    # display the maximum and minimun size
    def display_password_size_info(self):
        print("+ " + ("-"*(self.board_size)) + " +")
        print("| " + (" "*self.board_size) + " |")
        print(f"| {f'The password size have a':<{self.board_size}} |")
        print(f"| {f'min of 15 and a max of 29':<{self.board_size}} |")
        print("| " + (" "*self.board_size) + " |")
        print("+ " + ("-"*(self.board_size)) + " +")

    # invert booleans
    def turn_alphabet_stats(self):
        self.alphabet_stats = not self.alphabet_stats
    
    def turn_punctuations_stats(self):
        self.punctuations_stats = not self.punctuations_stats

    # setters
    def set_password_size(self, new_size):
        self.password_size = new_size

    def set_password(self, new_password):
        self.password = new_password

# to reapeat it in less lines
def get_option():
    option = int(input(" +- Option: "))
    
    if option < 1 or option > 4:
        raise ValueError

    return option

# password generation logic
def generate_password(interface):
    # get all number as a string
    numbers = string.digits

    # get upper and lower alpha and merge them as a string
    alpha_lower = string.ascii_lowercase
    alpha_upper = alpha_lower.upper()
    alpha = alpha_lower + alpha_upper

    # get all punctuations as a string
    punctuations = string.punctuation

    # put them all together
    everything = numbers

    if interface.alphabet_stats:
        everything += alpha

    if interface.punctuations_stats:
        everything += punctuations

    # generate
    interface.set_password("".join(
            choice(everything)
            for _ in range(interface.password_size)
        )
    )
    

# just space
def space():
    print("\n"*30)

# instancing interface
interface = Interface()
# starting main loop
while True:
    space()
    interface.display_main_menu()
    print()

    try:
        option = get_option()
    except ValueError:
        interface.display_invalid_option()
        continue

    # exit
    if option == 4:
        break

    in_option = 1
    while True:
        match option:
            case 1: # generate option
                if in_option == 1:
                    generate_password(interface)

                space()
                interface.display_password_generated()

                try:
                    in_option = get_option()
                except ValueError:
                    interface.display_invalid_option()
                    in_option = None

                if in_option != None:
                    match in_option:
                        case 1: # generate
                            pass
                        case 2: # copy
                            pyperclip.copy(interface.password)
                        case 3: # exit
                            break
                        case _:
                            interface.display_invalid_option()
            case 2: # settings option
                space()
                interface.display_settings_menu()
                print()

                try:
                    in_option = get_option()
                except ValueError:
                    interface.display_invalid_option()
                    in_option = None

                if in_option != None:
                    match in_option:
                        case 1: # turn alhabet stats 
                             interface.turn_alphabet_stats()
                        case 2: # turn ponctuation stats
                            interface.turn_punctuations_stats()
                        case 3: # set password size
                            space()

                            try:
                                new_size = int(input(" +- Password size: "))

                                if new_size < 15 or new_size > 29:
                                    interface.display_password_size_info()
                                    raise ValueError

                                interface.set_password_size(new_size)
                            except ValueError:
                               interface.display_invalid_option()
                        case 4:
                            break
                        case _:
                            interface.display_invalid_option()
            case _: # else
                interface.display_invalid_option()
                break
                
