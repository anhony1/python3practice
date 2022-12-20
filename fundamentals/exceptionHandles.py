try:
	#Main Routine
	print("Hello World")
	print(1+2)
	print(1/0)
	print("Goodbye")
except ZeroDivisionError:
	#If a division error occurs this exception code block executes
	print("Error divide by 0")

except: 
	# if any other error occurs this block executes
	print("Error here")

finally:
	# Regard
	print("end of script")