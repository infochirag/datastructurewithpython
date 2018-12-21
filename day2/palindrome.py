# Method 1

str = input("Enter string")

s = str[::-1]
if str == s:
  print("Yes , It is Palindrome")
else:
  print("No , it is not Palindrome")
  
  
  # Method 2
  
str = input("Enter string")
rev = ""
for i in str:
  rev  = i+rev
if(str == rev):
  print("Yes it is Palindrome")
else:
  print("No It is not palindrome")
