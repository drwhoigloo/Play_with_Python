
numberlist = []
for number in range(1, 200):
    if ( number % 7 ) and (number %5 !=0):
        numberlist.append(str(number))
print (', '.join(numberlist))
