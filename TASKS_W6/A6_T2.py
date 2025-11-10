def writefile(Pfilename, Pcontent):
    filehandle = open(Pfilename, "w")
    filehandle.write(Pcontent)
    filehandle.close()
    return None

def main():
    print("Program starting.")
    firstname = input("Insert first name: ")
    lastname = input("Insert last name: ")
    filename = input("Insert filename: ")
    content = "{}\n{}".format(firstname,lastname)
    
    writefile(filename, content)
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()