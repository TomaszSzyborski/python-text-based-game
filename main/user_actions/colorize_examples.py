from colorama import Fore


def _Colorize(colour: Fore, text: str):
    # return getattr(Fore, color) + text + Fore.RESET
    return f"{colour}{text}{Fore.RESET}"

print(_Colorize(Fore.RED, "asdasd"))
# print(Fore.GREEN + "asdasd" + Fore.RESET)
# print(_Colorize("BLUE", "lololol"))