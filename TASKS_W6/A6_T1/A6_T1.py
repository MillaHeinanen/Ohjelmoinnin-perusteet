def readFile(filename):
    filehandler = open(filename, "r")
    content = ""
    row = filehandler.readline()
    while row != "":
        content += row
        row = filehandler.readline()
    filehandler.close()
    return content #palaa takaisin kutsukohtaan

def main():
    print("Program starting.")
    print("This program can read a file.")
    filename = input("Insert filename: ")
    filecontent = readFile(filename) #Hyppää readfile funktioon
#   print("#### START {} ####".format(filename)) // Alternative way to format string
    print(f'#### START "{filename}" ####')
    print(filecontent)
    print(f'#### END "{filename}" ####')
   
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()