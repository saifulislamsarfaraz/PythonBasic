numOfWords = 0
numOfLetters = 0
numOfDigits = 0

text = input("Enter a text of numbers : ")
for x in text :
    x = x.lower()
    if x>= 'a' and x <= 'z':
        numOfLetters = numOfLetters+1

print(numOfLetters)
