word = str(input("Enter a word: "))

word = word[::-1]

if(word.lower() == word[::-1].lower()):
	print("Pali")
else:
	print("Not Pali")