def factorial():
    n = int(input("Enter a non-negative integer: "))  
    result = 1
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        for i in range(1, n-1 , 1):
            result *= i
        print(f"The factorial of {n} is {result}")


factorial()