number = int(input("Enter a number: "))

divisors = []

for i in range(1, number):
	res = number % i
	if(res == 0):
		divisors.append(i)

divisors.append(number)

print(divisors)
