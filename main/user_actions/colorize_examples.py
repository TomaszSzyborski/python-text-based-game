from colorama import Fore, Back


def _Colorize(background: Back = "", foreground: Fore = "", text: str = ""):
    # return getattr(Fore, color) + text + Fore.RESET
    return f"{background}{foreground}{text}{Fore.RESET}{Back.RESET}"

# print(_Colorize(Fore.RED, "asdasd"))
# print(Fore.GREEN + "asdasd" + Fore.RESET)
# print(_Colorize(Fore.BLUE, "lololol"))
# print(_Colorize(Back.BLUE, "lololol"))


print(_Colorize(foreground=Fore.RED, text="asdasd"))
print(_Colorize(foreground=Fore.GREEN, text="lololol"))
# print(Fore.GREEN + "asdasd" + Fore.RESET)
print(_Colorize(foreground=Fore.BLUE, text="lololol"))
print(_Colorize(background=Back.CYAN, foreground=Fore.YELLOW, text="lololol"))