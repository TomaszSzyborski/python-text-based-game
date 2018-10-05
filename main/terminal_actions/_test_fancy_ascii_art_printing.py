if __name__ == '__main__':
    import sys
    import os
    from colorama import init

    init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
    from termcolor import cprint
    from pyfiglet import figlet_format
    import pyfiglet

    fonts = pyfiglet.Figlet().getFonts()

    for font in fonts:
        print(f"printed font = {font}")
        cprint(
            figlet_format(
                'missile!',
                font=font),  # starwars #swampland #stforek
            'yellow',
            'on_red',
            attrs=['bold'])  # bold
        print()
