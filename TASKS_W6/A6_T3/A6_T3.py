def readFile(filename):
    filehandler = open(filename, "r")
    content = ""
    row = filehandler.readline()
    while row != "":
        content += row
        row = filehandler.readline()
    filehandler.close()
    return content

def writefile(Pfilename, Pcontent):
    filehandle = open(Pfilename, "w")
    filehandle.write(Pcontent)
    filehandle.close()
    return None

def main():
    print("Program starting.")
    print("This program can copy a file.")
    source = input("Insert source filename: ")
    destination = input("Insert destination filename: ")
    content = readFile(source)
    writefile(destination, content)
    print(f"Reading file '{source}' content.")
    print("File content ready in memory.")
    print(f"Writing content into file '{destination}'.")
    print("File content ready in memory.")
    print("Copying operation complete.")
    print("Program ending.")
if __name__ == "__main__":
    main()