
lesson = 'lists'

if lesson == 'exercise':

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

elif lesson == 'lists':

    # Play with lists
    my_list=['one', 'two', 'three']
    another_list=['four', 'five']
    print(my_list + another_list)

    #concat 2 lists by adding
    new_list = my_list+another_list
    print(new_list)

    # modify the first item in the new list
    new_list[0]='ONE ALL CAPS'
    print(new_list)

    #add a new item to end of list (append)
    new_list.append('six')
    print(new_list)

    #add a new item to end of list (append)
    new_list.append('seven')
    print(new_list)

    #remove an item from end of list
    new_list.pop()
    print(new_list)

    popped_item = new_list.pop()
    print(popped_item)

    # use .sort() to sort a list
    # NOTE: this sort occurs in-place
    redefined_list = ['z', 'r', 'e', 'a', 'q']
    num_list = [4, 1, 8, 3, 5, 11, 23, 2, 4, 22]

    # show the unsorted lists defined above
    print(redefined_list)
    print(num_list)

    # Sort the lists using the <list>.sort() method
    redefined_list.sort()
    num_list.sort()

    # Show that the sorting occurred inside the given lists
    print(redefined_list)
    print(str(num_list) + "\n")

    # The in-list sorting means that you MAY NOT assign the list
    # sort() function to a new list variable:
    new_sorted_list = redefined_list.sort()

    print(str(new_sorted_list) + "\n")
    # returns type "None" indicating that there was nothing to assign to 
    # the new sorted list variable.  The sorting occurred in-place

    # Use the <list>.reverse() method to reverse the list.
    # Like .sort(), .reverse() also occurs in-place.
    redefined_list.reverse()
    num_list.reverse()

    #Show the resulting reversed lists
    print(redefined_list)
    print(str(num_list) + '\n')

    #reverse them back
    redefined_list.reverse()
    num_list.reverse()

    #Show the resulting reversed lists
    print(redefined_list)
    print(num_list)

    # Slicing of lists is the same as strings
    print(f"this is ::-1    =>", num_list[::-1])
    print(f"this is 1::     =>", num_list[1::])
    print(f"this is 1:1     =>", num_list[1:1])
    print(f"this is 1:2     =>", num_list[1:2])
    print(f"this is 1:3     =>", num_list[1:3])
    print(f"this is 1:4     =>", num_list[1:4])
    print(f"this is 1:5     =>", num_list[1:5])
    print(f"this is 1:6     =>", num_list[1:6])
    print(f"this is 2:1     =>", num_list[2:1])
    print(f"this is 2:2     =>", num_list[2:2])
    print(f"this is 2:3     =>", num_list[2:3])
    print(f"this is 2:4     =>", num_list[2:4])
    print(f"this is :1:1    =>", num_list[:1:1])
    print(f"this is ::2     =>", num_list[::2])
    print(f"this is ::3     =>", num_list[::3])
    print(f"this is 1:2:1   =>", num_list[1:2:1])
    print(f"this is 1:9:2   =>", num_list[1:9:2])
    print(f"this is 1:10:3  =>", num_list[1:10:3])
    #
    # Output from above:
    #
    #['a', 'e', 'q', 'r', 'z']
    #[1, 2, 3, 4, 4, 5, 8, 11, 22, 23]
    #this is ::-1    => [23, 22, 11, 8, 5, 4, 4, 3, 2, 1]
    #this is 1::     => [2, 3, 4, 4, 5, 8, 11, 22, 23]
    #this is 1:1     => []
    #this is 1:2     => [2]
    #this is 1:3     => [2, 3]
    #this is 1:4     => [2, 3, 4]
    #this is 1:5     => [2, 3, 4, 4]
    #this is 1:6     => [2, 3, 4, 4, 5]
    #this is 2:1     => []
    #this is 2:2     => []
    #this is 2:3     => [3]
    #this is 2:4     => [3, 4]
    #this is :1:1    => [1]
    #this is ::2     => [1, 3, 4, 8, 22]
    #this is ::3     => [1, 4, 8, 23]
    #this is 1:2:1   => [2]
    #this is 1:9:2   => [2, 4, 5, 11]
    #this is 1:10:3  => [2, 4, 11]

else: 
    print("You didn't set a lesson string")