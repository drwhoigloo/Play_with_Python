

# Exercise to list all numbers in the given range that:
#		- not evenly divisible by 7
#         ex.  7%7 = 0 i.e. any number divisible by 7 will not get listed
#				AND
#		- not evenly divisible by 5
#         ex.  5%5 = 0 i.e. any number divisible by 5 will not get listed

# Declare working list, place to hold results so they may be printed.
numberlist = []

# Set the range for number to be between 1 and 200
for number in range(1, 200):
	# Show the number and the results of modulus operations
	print(number, " : ", number%7, " : ", number%5)

	# This would only print numbers that are both evenly
	# divisible by 7 AND 5 (so 35, 70, 105, etc...)
	# 	if ( number % 7 == 0) and (number %5 == 0):
	#
	# This would only print numbers that are evenly
	# divisible by 7 AND not evenly divisible by 5 (so 35, 70, 105, etc...)
	# 	if ( number % 7 == 0) and (number %5 != 0):
	#
 	# Calculate the modulus of the number and if not evenly
	# divisible by 7 and 5, append to the list
	if ( number % 7 != 0) and (number %5 != 0):
		numberlist.append(str(number))

print (', '.join(numberlist))

# OUTPUT LIST for number % 7 and number % 5
# 1, 2, 3, 4, 6, 8, 9, 11, 12, 13, 16, 17, 18, 19,
# 22, 23, 24, 26, 27, 29, 31, 32, 33, 34, 36, 37, 
# 38, 39, 41, 43, 44, 46, 47, 48, 51, 52, 53, 54, 
# 57, 58, 59, 61, 62, 64, 66, 67, 68, 69, 71, 72,
# 73, 74, 76, 78, 79, 81, 82, 83, 86, 87, 88, 89,
# 92, 93, 94, 96, 97, 99, 101, 102, 103, 104, 106, 
# 107, 108, 109, 111, 113, 114, 116, 117, 118, 121,
# 122, 123, 124, 127, 128, 129, 131, 132, 134, 136, 
# 137, 138, 139, 141, 142, 143, 144, 146, 148, 149, 
# 151, 152, 153, 156, 157, 158, 159, 162, 163, 164, 
# 166, 167, 169, 171, 172, 173, 174, 176, 177, 178, 
# 179, 181, 183, 184, 186, 187, 188, 191, 192, 193, 
# 194, 197, 198, 199