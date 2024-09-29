
user_input = input("Enter your list of numbers separated by spaces: ")
user_list = [int(i) for i in user_input.split()]



def newList(user_list):
 TheNewList=[]
 for i in user_list:
    if (i%2==0):
     TheNewList.append(i)
 print("The new list of even numbers:")  
 print(*TheNewList)   
     

newList(user_list)    
   
   
