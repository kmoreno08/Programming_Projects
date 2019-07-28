'''Between 1 and 1000, there is only 1 number that meets the following criteria.
While it could be manually figured out with pen and paper, it would be much
more efficient to write a program that would do this for you.
With that being said, your goal is to find out which number meets these criteria.

1) The number has at least two digits
2) The number is prime
3) The number does NOT contain a 1 or 7 in it
4) The sum of all of the digits is less than or equal to 10
5) First two digits add up to be odd
6) The second to last digit is even
7) The last digit is equal to how many digits are in the number
'''

#Number has at least two digits
lower = 900
upper = 1000


#Prime numbers only
for num in range(lower, upper + 1):
    if num > 1:
        for i in range (2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
            #does not contain a 1 or 7 in it
            
    
  
    
        
