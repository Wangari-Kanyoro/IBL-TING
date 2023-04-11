from figlet import Figlet
import sys
import random

figlet = Figlet


fonts = figlet.get_fonts()


if len (sys.argv) == 1:
    figlet.set_font(font=random.choice(fonts))
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == '--font') and sys.argv[2] in fonts:
    figlet.set_font(font=sys.argv[2])
else:
    sys.exit("wrong use")

name= input("Enter:")


print (figlet.renderName(name))