print("Program starting.")
print("String comparisons")
#Prompt user to insert
#A word
word1=input("Insert first word: ")
#A character
char=input("Insert a character: ")
#Find if the character exists in the word. Possible prints below.
if char in word1:
    print(f'Word "{word1}" contains character "{char}"')
else:
    print(f'Word "{word1}" doesn\'t contain character "{char}"')
#Prompt user to insert one more word
word2=input("Insert second word: ")
#Compare the first word to the second word. Examples below:
if word1 < word2:
    print(f'The first word "{word1}" is before the second word "{word2}" alphabetically.')
elif word1 > word2:
    print(f'The second word "{word2}" is before the first word "{word1}" alphabetically.')
else:
    print(f'Both inserted words are the same alphabetically, "{word1}"')
print("Program ending.")