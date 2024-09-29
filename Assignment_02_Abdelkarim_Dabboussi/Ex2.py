
n = int(input("Enter an integer: "))  # Taking input from the user

def divisors(n):
   my_list=[]   
   for i in range(1, n+1):
    if n % i ==0:
        my_list.append(i)
   print(*my_list)   

divisors(n)
 
    