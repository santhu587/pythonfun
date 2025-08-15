s = "Python"
print(s[::-1])  # nohtyP
str="abc"
revstr=str[::-1]
if str==revstr:
    print("palindrome")
else:
    print("not palindrome")

for char in "Python":
    print(char, end="/")


s = "apple,banana,cherry"

# String → List
lst = s.split(" ")
print(lst)  # ['apple', 'banana', 'cherry']

# List → String
new_str = ",".join(lst)
print(new_str)  # apple,banana,cherry
sentence = "Python is fun"
print(" ".join(sentence.split()[::-1]))  # fun is Python
