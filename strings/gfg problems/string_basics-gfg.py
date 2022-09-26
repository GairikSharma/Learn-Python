x=input("Enter a string: ")
if(x[::-1]==x):
    print("Palindrome")
print("Not a palindrome")

# Python program to print all the palindromes in a given range
x=["obo", "gfg", "ball"]
for i in x:
    if(i[::-1]==i):
        print(i)

# Reverse words in a given String in Python
x= "My name is Gairik Sharma"
print(x[::-1])

p = 'Gairik Sharma'
q =' '.join(p.split(' ')[::-1])
print(q)

# Python program to remove ith character from a string
str = "Gairik sharma is a developer"
x=input("enter the string : ")
print(str.replace(x, ""))

# Python program to print even length words in a string

str = "my name is gairik"
str_split = str.split(" ")
for i in str_split:
    if(len(i)%2==0):
        print(i)

# Python program to capitalize the first and last character of each word in a string -> Needs lambda function