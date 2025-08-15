from xmlrpc.client import Boolean

print("hello shiva")
#list and tupples and sttring
#ordered and mutaable collectiion of items and allow dduplicatesand hetrogeonus elementss=list

names=["aman","yash",'santhu',1,bool]
#indexing  negative and psoitive indexin
print(names[-1])
names.append(9)
print(names)
num=[1,2,4]
names.extend(num)
print(names)
names.insert(0,"shiva")
print(names)
#remove -specific ele removes
#pop -specigic ele particualr index
num.pop(2)
print(num)
names.remove("yash")
print(names)

ages=[1,2,3,5,6,7,2]
print(max(ages))  #o(n)
print(min(ages))

#couht -counts the number of item presenst in count
print(ages.count(2))
print(ages.sort())
ages.sort()  #n(log(n)
print(ages)
ages.reverse()
print(ages)

# imp copy deep and shallow copy
#1 deep copy
a=[1,2,3]
b=a
a.append(9)
print(a,id(a))
print(b,id(b))

#shallow copy -- copy()
a=[1,2,3]
b=a.copy()
a.append(9)
print(a,id(a))
print(b,id(b))

#slicing
#subarary=is contionus part of array
#subsequence =is non continous but it has order
range(1,10)
range(2,20,4)
range(10,2,-2)

#slicing
numbers = [10, 20,10, 30, 40, 50]

print("reverse the in the list")
print(numbers[::-1])
print("occurrence of 10")
print(numbers.count(10))
print(numbers[1:4:2])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]  (start from 0)
print(numbers[2:])    # [30, 40, 50]  (go till the end)
print(numbers[-3:])   # [30, 40, 50] (last 3 elements)
print(numbers[:-2])   # [10, 20, 30] (everything except last 2)


 #python tupple ,same as list ,immuatbel we cant modify allows duplicates orderd
# Empty tuple
empty_tuple = ()
print(empty_tuple)  # ()

# Tuple with integers
t1 = (1, 2, 3)
print(t1)  # (1, 2, 3)

# Tuple with mixed data types
t2 = (1, "hello", 3.14)
print(t2)  # (1, 'hello', 3.14)

# Without parentheses (tuple packing)
t3 = 1, 2, 3
print(t3)  # (1, 2, 3)

# Single element tuple (MUST have a comma)
t4 = (5,)
print(type(t4))  # <class 'tuple'>

# Using tuple() constructor
t5 = tuple([1, 2, 3])
print(t5)  # (1, 2, 3)
t = (10, 20, 30, 40, 50)

# Indexing
print(t[0])   # 10
print(t[-1])  # 50

# Slicing
print(t[1:4])  # (20, 30, 40)
print(t[::-1]) # (50, 40, 30, 20, 10)  # Reverse
t = (1, 2, 2, 3, 4, 2)

print(t.count(2))  # 3 → Occurrences of 2
print(t.index(3))  # 3 → First index of value 3
