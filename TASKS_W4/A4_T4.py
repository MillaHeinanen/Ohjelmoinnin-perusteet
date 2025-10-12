print("Program starting.\n")
words=[]
while True:
    word=input("Insert word (empty stops): ")
    if word=="":
        break
    words.append(word)   
word_count=len(words)
char_count=sum(len(word) for word in words)
print("\nYou inserted:")
print(f"- {word_count} words")
print(f"- {char_count} characters")
print("\nProgram ending.")