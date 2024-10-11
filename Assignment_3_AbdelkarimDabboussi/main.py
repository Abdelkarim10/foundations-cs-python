
def menu():
    print("1. Count Digits")
    print("2. Find Max")
    print("3. Count Tags")
    print("4. Exit ")


def countDigits(num):
    if num == 0:
        return 0
    return 1 + countDigits(num // 10)


def findMax(nums):
    if len(nums) == 0:
        return 0  
    if len(nums) == 1:
        return nums[0]
    else:
        max_of_rest = findMax(nums[1:])
        return nums[0] if nums[0] > max_of_rest else max_of_rest


def countTags(html, tag):
    opening_tag = f"<{tag}>"
    closing_tag = f"</{tag}>"
    
 
    if opening_tag not in html:
        return 0
    
    
    start_index = html.find(opening_tag)
    end_index = html.find(closing_tag, start_index)
    
    if start_index != -1 and end_index != -1:
       
        new_html = html[end_index + len(closing_tag):]
        return 1 + countTags(new_html, tag)
    
    return 0


while True:
    menu()
    option = int(input("Enter your option: "))
    
    if option == 1:
        num = int(input("Enter an integer to count its digits: "))
        if num == 0:
            print("The number has 1 digit.")
        else:
            print(f"The number {num} has {countDigits(abs(num))} digits.")
    
    elif option == 2:
        nums = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
        if not nums:
            print("List is empty, returning 0 as default.")
        else:
            print(f"The maximum value is: {findMax(nums)}")
    
    elif option == 3:
        html = """
        <html>
        <head>
        <title>My Website</title>
        </head>
        <body>
        <h1>Welcome to my website!</h1>
        <p>Here you'll find information about me and my hobbies</p>
        <h2>Hobbies</h2>
        <ul>
        <li>Playing guitar</li>
        <li>Reading books</li>
        <li>Traveling</li>
        <li>Writing cool h1 tags</li>
        </ul>
        </body>
        </html>
        """
        tag = input("Enter the HTML tag to count: ")
        count = countTags(html, tag)
        print(f"The tag <{tag}> appears {count} times in the HTML code.")
    
    elif option == 4:
        print("Exiting the program.")
        break
    
    else:
        print("Invalid option. Please try again.")
