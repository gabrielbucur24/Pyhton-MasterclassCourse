import colorama

RED = '\u001b[31m'
GREEN = '\u001b[32m'
CYAN = '\u001b[36m'
RESET = '\u001b[0m'


def colour_print(text: str, effect: str) -> None:
    """
    Print `text` using the ANSI sequences to change the colour, etc.

    :param text:The text to print
    :param effect: The effect we want. One of the constants
    """
    output_string = "{0}{1}{2}".format(effect, text, RESET)
    print(output_string)


colorama.init()
colour_print("Hello, Red", RED)
# test the reset
print("This should be in the default terminal colour")
colour_print("Hello, Cyan", CYAN)
colorama.deinit()

