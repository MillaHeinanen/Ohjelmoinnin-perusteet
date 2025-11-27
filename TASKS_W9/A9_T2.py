########################################################
# Task A9_T2
# Milla Heinänen
# 2025-11-26
########################################################

import sys

def main():
     print("Program starting.")
     Feed = input("Insert exit code(0-255): ")
     ExitCode = int(Feed)
     if ExitCode == 0:
         print("Clean exit.")
     else:
         print("Error code.")
     sys.exit(ExitCode)
     return None
main()