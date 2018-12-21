# Method 1: Using indexing method

str = "Hello-World"
print(str[::-1])

# The above would reverse the string

""" 
Or the 
simple way
"""

str = "Input string"
rev = " "
for i in str:
  rev  = i+rev
print(rev)
