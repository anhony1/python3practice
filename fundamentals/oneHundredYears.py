age = int(input("Enter your age"))
name = input("Enter your name")

def calculateOneHundredAge(age, name):
	oneHund = 100 - age + 2022
	print(name, ", you will turn 100 years old in year", oneHund)


calculateOneHundredAge(age, name)

