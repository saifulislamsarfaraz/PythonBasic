numOfWords = 0
numOfLetters = 0
numOfDigits = 0

text = input("Enter a text of numbers : ")
for x in text :
    x = x.lower()
    if x>= 'a' and x <= 'z':
        numOfLetters = numOfLetters+1
    if x>= 0 and x<=9:
        numOfDigits = numOfDigits + 1
    if x==" ":
        numOfWords = numOfWords + 1


print(numOfLetters)
print(numOfDigits)
print(numOfWords)
