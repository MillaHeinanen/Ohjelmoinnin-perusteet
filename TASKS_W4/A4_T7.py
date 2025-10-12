def multiplicative_persistence():
    print("Program starting.\n")
    print("Check multiplicative persistence.")
    number=input("Insert an integer: ")
    steps=0
    while len(number)>1:
        digits=[int(d) for d in number]
        product=1
        for d in digits:
            product*=d
        print(f"{' * '.join(number)} = {product}")
        number=str(product)
        steps+=1
    print("No more steps.\n")
    print(f"This program took {steps} step(s)\n")
    print("Program ending.")
multiplicative_persistence()