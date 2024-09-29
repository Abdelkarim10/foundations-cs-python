
password = input("Enter a strong password: ")

def DoesItHave(password):
  size = len(password)
  if size >= 8:
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in '#?!$' for char in password)
    return has_upper and has_lower and has_digit and has_special
      

if DoesItHave(password) :
    print("Strong password")  
else:
     print("Weak password")  

