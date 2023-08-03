# 1-Write a Python program to calculate the length of a string using 2 ways
str1 = "ahmed ghonem"
# (1)
print(len(str1))
# (2)
x = 0
for i in str1:
    x += 1
print("the len:", x)

''' 2-Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string 
length is less than 2, return the empty string instead(Sample String : 'w3resource' Expected Result : 'w3ce' 
##Sample String : 'w3' Expected Result : 'w3w3' ##Sample String : ' w' Expected Result : Empty String)'''
str2 = input("inter your string")
if len(str2) < 2:
    str2 = ""
    print(str2)
else:
    if len(str2) == 2:
        print(str2 * 2)
    else:
        print(str2[0:2] + str2[-2:])

'''3-Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string
 already ends with 'ing', add 'ly' instead.If the string length of the given string is less than 3, leave it unchanged. 
 (Sample String : 'abc' Expected Result : 'abcing') '''
str3 = input("inter your string")
if str3[-3:] == "ing":
    print(str3 + "ly")
else:
    if len(str3) < 2:
        print(str3)
    else:
        print(str3 + "ing")

# 4-Write a Python function that takes a list of words and return the longest word and the length of the longest one
# (Longest word: Exercises Length of the longest word: 9)
long_str = ""
length_of_long_str = 0


def longest_str(list_str):
    long_str = ""
    length_of_long_str = 0
    for i in list_str:
        if len(i) > len(long_str):
            long_str = i
            length_of_long_str = len(i)
    return long_str, length_of_long_str


print(longest_str(["ahmed", "mohamed", "amr", "zezo"]))

# 5-Write a Python program to change a given string to a newly string where the first and last chars have been exchanged
# (Sample String:abca Expected Result:ebce)
str4 = input("inter your string")
print(str4[-1] + str4[1:-1] + str4[0])

# 6-Write a Python program to remove characters that have odd index values in a given string (Sample String:abca Expected Result:ac)
str5 = input("inter your string")
print(str5[::2])

# 7-Write a Python program to count the occurrences of each word in a given sentence
# (Sample String:amr and ahmed are frindes but amr is the tallest Expected Result:2)
str1 = "amr and ahmed are frindes but amr is the tallest Expected"
str_list = str1.split()
tuple1 = tuple(str_list)
for i in tuple1:
    print(i, str_list.count(i))

# 8-Write a Python script that takes input from the user and displays that input back in upper and lower cases
x = input()
print("the upper", x.upper())
print("the lower", x.lower())


# 9-Write a Python function to reverse a string if its length is a multiple of 4
def reverse1(str1):
    if len(str1) % 4 == 0:
        print(str1[-1::-1])


reverse1("emad")

# 10-Write a Python program to remove a newline in Python
mystring = '\nThis is my string. \n'
print("With newlines:" + mystring)
print("After deleting the newlines:", mystring.strip())  # strip() methode

# 11-Write a Python program to check whether a string starts with specified characters
string = "ahmed ghonem"
print(string.startswith("ahm"))  # startswith() methods

# 12_Write a Python program to add prefix text to all of the lines in a string
start = "start"
text = " ahmed \n mohamed \n amr "
print(start, text[1:8], start, text[9:18], start, text[19:22])
# another answer
pargraph = '''Hey i am a ahmed.Now days i am doing training in AI and Machine learning.I am doing training from 
Goeduhub '''
list1 = pargraph.split('.')  # string to list the space is .
for i in list1:
    print("start " + i)

# 13-Write a Python program to print the following numbers up to 2 decimal places
x = 2.255464646
number = round(x, 2)  # round() methode take veriable and number of decimal number
print(number)

# 14_Write a Python program to print the following numbers up to 2 decimal places with a sign
v = 2.646464616
v = str(v)
list2 = v.split(".")
print(list2[0] + "." + list2[1][0:2])

# 15_Write a Python program to display a number with a comma separator
num = 1000000000
print(f"{num:,d}")

# 16-Write a Python program to reverse a string using 2 ways
string2 = "ahmed"
print(string2[::-1])
# two-way
string1 = "ahmed"
str_revarse = ""
for x in string1:
    str_revarse = x + str_revarse
print(str_revarse)

# 17_Write a Python program to count repeated characters in a string (hint:use dictionary)
list1 = [1, 1, 2, 2, 3, 4, 4, 5, 6]
dish = {}
list2 = tuple(list1)
for i in list2:
    if list1.count(i) > 1:
        dish[i] = list1.count(i)
print(dish)

# 18-Write a Python program to find the first non-repeating character in a given string
list1 = [1, 1, 2, 2, 3, 4, 4, 5, 6]
list2 = tuple(list1)
for i in list2:
    if list1.count(i) == 1:
        print("the num is:", i)
        break

# 19-Write a Python program to remove spaces from a given string
str_given = "Ahmed Gho nem"
text = ""
for i in str_given:
    if i != " ":
        text += i
print(text)

# 20-Write a Python program to count the number of non-empty substrings of a given string #!!!
str_given = "Ahm ed Gh on em"
num = 0
for m in str_given:
    if m != " ":
        num += 1
print(num)

# 21-write a Python program to swap first and last element of any list.
lis1 = [1, 2, 3, 4, 5, 6]
elm1 = lis1[0]
elm2 = lis1[-1]
lis1[-1] = elm1
lis1[0] = elm2
print(lis1)

# 22_Given a list in Python and provided the positions of the elements
sl = list(input("insert the element of list"))
pos1 = int(input())
pos2 = int(input())
sl[pos1], sl[pos2] = sl[pos2], sl[pos1]
print(sl)

# 23-search for the all ways to know the length of the list
lis2 = [1, 2, 3, 4, 5, 6]
# (1)
print(len(lis2))
# (2)
x = 0
for i in lis2:
    x += 1
print(x)
# (3)
print(lis2.index(lis2[-1]) + 1)
# (4)


# 24-write a Python code to find the Maximum number of list of numbers.
nums = [1, 5, 4, 9, 77, 99, 54]
print(max(nums))

# 25-write a Python code to find the Minimum number of list of numbers.
nums2 = [1, 5, 4, 9, 77, 99, 54]
print(min(nums2))

# 26-search for if an elem is existing in list
list3 = ["ahmed", "amr", "ali"]
elem = "ahmed"
for i in list3:
    if i == elem:
        print("yes")
        break
    else:
        print("no")
        break

# 27- clear python list using different ways
list3 = ["ahmed", "amr", "ali"]
# (1)
list3.clear()
print(list3)
# (2)
list3 = []
print(list3)
# (3)
del list3[:]
print(list3)
# (4)
for e in list3:
    del list3[e]
print(list3)
# (5)
while len(list3) != 0:
    list3.pop()
print(list3)
# (6)
list3 = list3[:0]
print(list3)

# 28-remove duplicated elements from a list
list4 = [1, 2, 2, 3, 4, 4, 5, 6]
print(list(set(list4)))

# 29-Given list values and keys list, convert these values to key value pairs in form of list of dictionaries.
# (Input : test_list = [“Gfg”, 3, “is”, 8], key_list = [“name”, “id”] Output : [{‘name’: ‘Gfg’, ‘id’: 3}, {‘name’: ‘is’, ‘id’: 8}])
test_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]
# printing original list
print("The original list : " + str(test_list))
# initializing key list
key_list = ["name", "number"]
# using list comprehension to perform as shorthand
n = len(test_list)
res = [{key_list[0]: test_list[idx], key_list[1]: test_list[idx + 1]}
       for idx in range(0, n, 2)]
# printing result
print("The constructed dictionary list : " + str(res))

# 30-write a python program to count unique values inside a list using different ways
# (1)
a_list = ['apple', 'orage', 'apple', 'banana', 'apple', 'apple', 'orange', 'grape', 'grape', 'apple']
set = set(a_list)
num_values = len(set)
print(num_values)
# (2)
a_list = ['apple', 'orage', 'apple', 'banana', 'apple', 'apple', 'orange', 'grape', 'grape', 'apple']
num_values = len(set(a_list))
print(num_values)
# (3)
a_list = ['apple', 'orage', 'apple', 'banana', 'apple', 'apple', 'orange', 'grape', 'grape', 'apple']
unique_list = list()
unique_items = 0
for item in a_list:
    if item not in unique_list:
        unique_list.append(item)
        unique_items += 1
print(unique_items)

# 31-write a python program Extract all elements with Frequency greater than K (Input :
# test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3 Output : [4, 3,6] )
list_test = list(input())
list_save = []
k = int(input())
for i in set(list_test):
    if int(i) > k:
        list_save += i
print(list_save)

# 32-write a python program to find the Strongest Neighbour (Input: 1 2 2 3 4 5 Output: 2 2 3 4 5)
test_list = [5, 4, 2, 5, 8, 2, 1, 9]
# printing original list
print("The original list is : ", test_list)
for i in range(1, len(test_list) - 1):
    # using max() to get maximum of Neighbours
    test_list[i] = max(test_list[i - 1], test_list[i + 1])
# printing result
print("The elements after replacing : ", test_list)

# 33-write a Python Program to print all Possible Combinations from the three Digits
# (Input: [1, 2, 3] Output: 1 2 3 ## 1 3 2 ## 2 1 3 ## 2 3 1 ## 3 1 2 ## 3 2 1)
list2 = list(input())
for i in range(3):
    for j in range(3):
        for k in range(3):

            # check if the indexes are not
            # same
            if (i != j and j != k and i != k or i == j, i == k, j == k):
                print(list2[i], list2[j], list2[k])

# 34-write a Python program to find all the Combinations in the list with the given condition (Input:
# test_list = [1,2,3] Output: [1], [1, 2], [1, 2, 3], [1, 3] [2], [2, 3], [3])
from itertools import combinations

# initializing list
test_list = ["GFG", [5, 4], "is",
             ["best", "good", "better", "average"]]
idx = 0
temp = combinations(test_list, 2)
for i in list(temp):
    idx = idx + 1
    print("Combination", idx, ": ", i)

# 35-write a Python program to get all unique combinations of two Lists (List_1 = ["a","b"] List_2 = [1,2]
# Unique_combination = [[('a',1),('b',2)],[('a',2),('b',1)]] )
list_1 = ["a", "b"]
list_2 = [1, 2]
unique_combinations = []
for i in range(len(list_1)):
    for j in range(len(list_2)):
        unique_combinations.append((list_1[i], list_2[j]))
print(unique_combinations[:2], unique_combinations[2:])

# 36-Remove all the occurrences of an element from a list in Python (Input : 1 1 2 3 4 5 1 2 1Output : 2 3 4 5 2)
mylist = [21, 5, 8, 52, 21, 87]
r_item = 21
# remove the item for all its occurrences
for item in mylist:
    if item == r_item:
        mylist.remove(r_item)
print(mylist)

# 37-write a python program to Replace index elements with elements in Other List (The original list 1 is :  [‘Gfg’, ‘is’, ‘best’]
# The original list 2 is : [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0] The lists after index elements replacements is :
# [‘Gfg’, ‘is’, ‘best’, ‘is’, ‘Gfg’, ‘Gfg’, ‘Gfg’, ‘best’, ‘is’, ‘is’, ‘best’, ‘Gfg’])
list1 = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]
list2 = ["Gfg", "is", "best"]
list3 = []
for i in list1:
    list3 += [list2[i]]
print(list3)

# 38- write python program to Retain records with N occurrences of K(Input : test_list = [(4, 5, 5, 4), (5, 4, 3)],
# K = 5, N = 2 Output : [(4, 5, 5, 4)] Input : test_list = [(4, 5, 5, 4), (5, 4, 3)], K = 5, N = 3 Output : [] )
test_list = [(4, 5, 6, 4, 4), (4, 4, 3), (4, 4, 4), (3, 4, 9)]
K = 4
N = 3
res = [ele for ele in test_list if ele.count(K) == N]
print("Filtered tuples : ", res)


# 39-write a Python Program to Sort the list according to the column using lambda array = [[1, 3, 3], [2, 1, 2], [3, 2, 1]]
# Output : Sorted array specific to column 0, [[1, 3, 3], [2, 1, 2], [3, 2, 1]] Sorted array specific to column
# 1, [[2, 1, 2], [3, 2, 1], [1, 3, 3]] Sorted array specific to column 2, [[3, 2, 1], [2, 1, 2], [1, 3, 3]]
# Python code to sorting list
# according to the column
# sortarray function is defined
def sortarray(array):
    for i in range(len(array[0])):
        # sorting array in ascending
        # order specific to column i,
        # here i is the column index
        sortedcolumn = sorted(array, key=lambda x: x[i])
        # After sorting array Column 1
        print("Sorted array specific to column {}, \
		{}".format(i, sortedcolumn))


# Driver code
if __name__ == '__main__':
    # array of size 3 X 2
    array = [['java', 1995], ['c++', 1983],
             ['python', 1989]]
    # passing array in sortarray function
    sortarray(array)

# 40- write a program to Sort Python Dictionaries by Key or Value
dist1 = {'c': 1, 'b': 2, 'a': 3}
list1 = list(dist1)
list1.sort()
print(list1)

# 41-write python program to Remove keys with Values Greater than K ( Including mixed values ) nput :
# test_dict = {‘Gfg’ : 3, ‘is’ : 7, ‘best’ : 10, ‘for’ : 6, ‘geeks’ : ‘CS’}, K = 7 Output : {‘Gfg’ : 3, ‘for’ : 6, ‘geeks’ : ‘CS’}
test_dict = {"Gfg": 3, "is": 7, "best": 10, "for": 6, "geeks": 0}
k = int(input("insertthe value"))
keys = list(test_dict)
for i in keys:
    if test_dict[i] > k:
        del test_dict[i]
print(test_dict)

# 42-Write a Python program to concatenate the following dictionaries to create a new oneSample Dictionary :
# dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60} Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
print(dic1 | dic2 | dic3)

# 43-Write a Python program to iterate over dictionaries using for loops
my_dict = {'Name': 'Sam', 'Age': 26, 'City': 'Toronto', 'Degree': 'Masters'}
for i in my_dict.items():
    print(i)

# 44- Write a Python script to merge two Python dictionaries
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}
print(dict_1 | dict_2)

# 45-Write a Python program to get the maximum and minimum values of a dictionary values
dist1 = {'c1': 1, 'c2': 2, 'c3': 3}
print(max(dist1.values()))

# 46- Write a Python program to drop empty items from a given dictionary. Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None} New Dictionary after dropping empty items: {'c1': 'Red', 'c2': 'Green'}
dist1 = {'c1': 'Red', 'c2': 'Green', 'c3': None}
print(dist1['c3'])
d = list(dist1)
for i in d:
    if dist1[i] == None:
        dist1.pop(i)
print(dist1)

# 47-Write a Python program to create a tuple of numbers and print one item
tuble_new = tuple(input("insert the element of tuple"))
list_to_tuble = list(tuble_new)
print("the tuple = ", tuble_new, "one element is ", list_to_tuble[0])

# 48-Write a Python program to unpack a tuple into several variables
tuple_add = ("ahmed", 20, "kafr_elshekh")
(name, age, adress) = tuple_add
print(name, age, adress)

# 49-Write a Python program to add an item to a tuple
tuple_add = (1, 2, 3, 4)
list_add = list(tuple_add)
list_add.append(5)
print(tuple(list_add))

# 50-Write a Python program to convert a tuple to a string
tuples = ('welcome', ' to', ' sparkbyexamples', '.com')
string = "".join(tuples)
print(string)

# 51-Write a Python program to convert a list to a tuple
x = [5, 6, 7]
x = tuple(x)
print(x)

# 52-Write a Python program to reverse a tuple
tuple_reverse = (1, 2, 3, 4, 5, 6)
list_of_tuple = list(tuple_reverse)
list_of_tuple.reverse()
print(tuple(list_of_tuple))

# 53-Write a Python program to replace the last value of tuples in a list. Sample list:
# [(10, 20, 40), (40, 50, 60), (70, 80, 90)] Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
list5 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
list6 = []
for x in list5:
    x = list(x)
    x[2] = 100
    list6 += x
list6[0] = tuple(list6[0:3:])
list6[1] = tuple(list6[3:6:])
list6[2] = tuple(list6[6:9:])
del list6[3:9]
print(list6)

# 54-Write a Python program to convert a given string list to a tuple Original string:
# python 3.0 <class 'str'> Convert the said string to a tuple: ('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
x = input("insert the string")
x = tuple(x)
print(x)

# 55-Write a Python program to calculate the average value of the numbers in a given tuple of tuples
tuple1 = tuple(input("insert the elemant"))
sum = 0
for u in tuple1:
    sum += int(u)
print(sum / len(tuple1))

# 56-Write a Python program to add member(s) to a set.
set1 = {1, 2, 3, 4}
set1.add("s")
print(set1)

# 57-Write a Python program to remove an item from a set if it is present in the set.
num = 5
set_found = {1, 2, 3, 6, 5}
for i in list(set_found):
    if i == num:
        set_found.discard(i)
print(set_found)

# 58-Write a Python program to create an intersection,union,difference and symmetric difference of sets
E = {0, 2, 4, 6, 8};
N = {1, 2, 3, 4, 5};
# set union
print("Union of E and N is", E | N)
# set intersection
print("Intersection of E and N is", E & N)
# set difference
print("Difference of E and N is", E - N)
# set symmetric difference
print("Symmetric difference of E and N is", E ^ N)

# 59-Write a Python program to find the maximum and minimum values in a set
set2 = {1, 2, 3, 4}
print(max(set2))
print(min(set2))

# 60- Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.
lst = [1, 5, 3, 7, 9]
k = int(input())

res = []
while lst:
    num = lst.pop()
    diff = k - num
    if diff in lst:
        res.append((diff, num))

res.reverse()
print(res)
