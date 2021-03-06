# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
# imports from other .py files
# Main Menu
from week0 import christmastree,animation
from week1 import infodblistsandloops
from crossover import hi


main_menu = [
#  ["FunGame", "fungame.py"]
]
# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu0 = [
    ["Christmas Tree", christmastree.treeprint],
    ["Matrix Number Pad", "week0/matrixnumberpad.py"],
    ["Animation", animation.animation],
    

]

sub_menu1 = [

    ["Fibonacci", "week1/fibonacci.py"],
    ["Factorial", "week2/factorial.py"],
    ["Math Imperative + OOP", "week2/math.py"],
    ["Number Swap", "week0/numberswap.py"],
]

sub_menu2 = [
    ["Oogway Quote", "week0/oogwayquote.py"],
    ["Extra Credit Palindrome", "week2/palindrome.py"],
    ["InfoDBListsandLoops", infodblistsandloops.tester],
    ["Hi", hi.hi],
]

border = "=" * 25
banner = f"\n{border}\nPlease choose one of the following options: \n{border}"


def menu():
    title = "Lumoo's Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Patterns: Christmas Tree, Matrix Number Pad", submenu0])
    menu_list.append(["Math: Fibonacci, Number Swap, Factorial, Math Function", submenu1])
    menu_list.append(["Display: Oogway Quote, Palindrome, Lists, Loops", submenu2])
    buildMenu(title, menu_list)


def submenu0():
    title = "\nLumoo's Submenu" + banner
    buildMenu(title, sub_menu0)

def submenu1():
    title = "\nLumoo's Submenu" + banner
    buildMenu(title, sub_menu1)

def submenu2():
    title = "\nLumoo's Submenu" + banner
    buildMenu(title, sub_menu2)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()