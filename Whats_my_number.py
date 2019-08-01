'''Between 1 and 1000, there is only 1 number that meets the following criteria.
While it could be manually figured out with pen and paper, it would be much
more efficient to write a program that would do this for you.
With that being said, your goal is to find out which number meets these criteria.

1) The number has at least two digits --complete
2) The number is prime --complete
3) The number does NOT contain a 1 or 7 in it --complete
4) The sum of all of the digits is less than or equal to 10 --complete
5) First two digits add up to be odd
6) The second to last digit is even
7) The last digit is equal to how many digits are in the number
'''

#Number has at least two digits
lower = 10
upper = 1000

#Empty list for all numbers
final_num_list = []



#Prime numbers only
for num in range(lower, upper + 1):
    #Add all numbers to list
    final_num_list.append(num)
    
    if num > 1:
        #Prime Numbers only
        for i in range (2, num):
            if (num % i) == 0:
                #Remove from list
                final_num_list.remove(num)
                break
        else:
            #Each digit in a list to check for 1 or 7
            num_list = [int(d) for d in str(num)]
            #Iterate through each digit
            for i in num_list:
                if i == 1:
                    #Remove number from list
                    final_num_list.remove(num)
                    break                  
                elif i == 7:
                    #Remove number from list
                    final_num_list.remove(num)
                    break
                #Keep number in final_num_list
                else:
                    pass


#Sum of all digits is less than or equal to 10
#Reverse list for index out of range error
for index in range(len(final_num_list)-1, -1, -1):
    #Split number in to list
    num_list = [int(d) for d in str(final_num_list[index])]
    #Get sum of total number
    sum_num = sum(num_list)
    #If sum is more then 10, remove from list
    if sum_num > 10:
        #Remove from list
        del final_num_list[index]
    else:
        pass

print(final_num_list)
#First two digits add up to be odd
for index in range(len(final_num_list)-1, -1, -1):
    #Split in to list
    num_list = [int(d) for d in str(final_num_list[index])]
    first_digit = num_list[0]
    second_digit = num_list[1]
    total_digit = first_digit + second_digit
    print(first_digit)
    print(second_digit)
    print(total_digit)
    print("***" * 10)
    if total_digit % 2 == 1:
        del final_num_list[index]
    else:
        pass

print(final_num_list)


    
  
    
        
