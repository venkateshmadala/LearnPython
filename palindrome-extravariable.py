x=input("enter your input variable: ")
w=""
for i in x:
    w=i+w
if w==x:
    print("string is palindrome")
else:
    print("string is not palindrome")