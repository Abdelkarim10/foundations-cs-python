IPv4 = input("Enter a valid IPv4 address: ")

def checkIPS(IPv4):
    octets = IPv4.split('.')
    
   
    if len(octets) != 4:
        return False
    
    for octet in octets:
        
        if not octet.isdigit():
            return False
        
        num = int(octet)      
       
        if num < 0 or num > 255 or (octet != '0' and octet.startswith('0')):
            return False
    
    return True  


if checkIPS(IPv4):
    print("Valid IPv4 address")
else:
    print("Invalid IPv4 address")
