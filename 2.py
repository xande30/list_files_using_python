import subprocess as sub
from colorama import Fore

lsout = sub.Popen(['ls', '*'], shell=True, stdout=sub.PIPE).stdout
for line in lsout:
    print(Fore.MAGENTA, line)

