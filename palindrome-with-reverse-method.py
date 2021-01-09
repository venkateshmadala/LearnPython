value = input("Enter your string you want to check whether is it palindrome or not: ")
reversevalue = value[::-1]
if value==reversevalue:
    print("Given string is palindrome")
else:
    print("Given string is not palindrome")