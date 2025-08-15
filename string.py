str1 = 'Python'
str2 = "Hello World"
str3 = '''Triple quoted string'''
str4 = """Multi-line
string example"""

print(str1, str2, str3, str4)
text = "Python"

print(text[0])    # P
print(text[-1])   # n
text = "Python Programming"

print(text[0:6])    # Python
print(text[:6])     # Python
print(text[7:])     # Programming
print(text[::-1])   # gnimmargorP nohtyP  (Reverse)
s=["h","e","l","l","o"]
print("".join(s[::-1]))

a = "Hello"
b = "World"

# Concatenation
print(a + " " + b)   # Hello World

# Repetition
print(a * 3)         # HelloHelloHello

# Membership
print("H" in a)      # True
print("Z" not in a)  # True

# Length
print(len(a))        # 5
text = "  hello world  "

# Case Conversion
print(text.upper())        #   HELLO WORLD
print(text.lower())        #   hello world
print(text.title())        #   Hello World

# Removing spaces
print(text.strip())        # hello world
print(text.lstrip())       # hello world
print(text.rstrip())       #   hello world

# Finding & Counting
print(text.find("world"))  # 8
print(text.count("l"))     # 3

# Replace
print(text.replace("world", "Python"))  #   hello Python

# Split & Join
words = text.strip().split()    # ['hello', 'world']
print(words)
print("-".join(words))          # hello-world
name = "John"
age = 25

# f-String (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")

# format()
print("My name is {} and I am {} years old.".format(name, age))

# With positions
print("{1} is {0} years old".format(age, name))

# With formatting
pi = 3.14159
print(f"Value of pi: {pi:.2f}")   # 3.14
s = "Python3"

print(s.isalpha())   # False (contains numbers)
print(s.isdigit())   # False
print(s.isalnum())   # True
print(s.islower())   # False
print(s.isupper())   # False
print(s.isspace())   # False
s = "Hello"
# s[0] = "J" ❌ Error

# Correct way: create a new string
s = "J" + s[1:]
print(s)  # Jello
def lengthOfLastWord(self, s):
    """
    :type s: str
    :rtype: int
    """
    s=s.strip()
    s1=s.split(" ")
    word=s1[-1]
    ans=len(word)
    return ans

# List with duplicates
nums = [1, 2, 3, 2, 4, 5, 1, 6, 2]




seen={}
for num in nums:
    if num in seen:
        print("dup",num)
    else:
        seen[num]=1
# Dictionary to store frequency
freq = {}

# Count occurrences
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# Print duplicates
print("Duplicates are:")
for key, value in freq.items():
    if value > 1:
        print(key, "appears", value, "times")

