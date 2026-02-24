from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 3:
    if (sys.argv[1] == '-f' or sys.argv[1] == '--font') and (sys.argv[2] in fonts):
        user_font = sys.argv[2]
        figlet.setFont(font=user_font)
        word = input("Input: ").strip()
        print(figlet.renderText(word))
    elif sys.argv[1] != '-f' and sys.argv[1] != '--font':
        sys.exit("Incorrect first argument")
    else:
        sys.exit("Error - no font provided")
elif len(sys.argv) == 1:
    user_font = random.choice(fonts)
    figlet.setFont(font=user_font)
    word = input("Input: ").strip()
    print(figlet.renderText(word))
else:
    sys.exit("Error - incorrect argument size")