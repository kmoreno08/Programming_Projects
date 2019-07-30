'''Between 1 and 1000, there is only 1 number that meets the following criteria.
While it could be manually figured out with pen and paper, it would be much
more efficient to write a program that would do this for you.
With that being said, your goal is to find out which number meets these criteria.

1) The number has at least two digits --complete
2) The number is prime --complete
3) The number does NOT contain a 1 or 7 in it --complete
4) The sum of all of the digits is less than or equal to 10
5) First two digits add up to be odd
6) The second to last digit is even
7) The last digit is equal to how many digits are in the number
'''

#Number has at least two digits
lower = 100
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
                #Sum of all digits is less than or equal to 10
                else:
                    print(final_num_list)
                    
    
  
    
        
