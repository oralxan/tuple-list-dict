#1
'''
a = [1, -2, 3, -4, 5]
def negative_numbers(numbers):
 squared_numbers = [x ** 2 if x < 0 else x for x in numbers]
 return squared_numbers
my_list = [1, -2, 3, -4, 5]
new_list = negative_numbers(my_list)
print(new_list)'''
#2\

'''def num(number):
    a=0
    b=0
    for num in number:
        if a%2==0:
            a+=1
        else:
            b+=1
        return a,b

list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


a,b = num(list_num)
print(a,b)'''
#3
'''def a(list1, list2):
    b = []
    for element in list1:
        if element in list2:
            b.append(element)
    return b


list1 = [1, 2, 3, 3, 5]
list2 = [4, 5, 6, 7, 8]
result = a(list1, list2)
print(result)'''

#5
'''def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


my_list = [2, 2, 3, 6, 4, 4, 7]
result = remove_duplicates(my_list)
print(result)'''

#6
'''def a(lst):
    b = 0
    for i in range(1, len(lst), 2):
        b += lst[i]
    return b


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result =a (my_list)
print(result)'''
#7
'''def unique_elements(list1, list2):
    unique = []
    for element in list1:
        if element not in list2:
            unique.append(element)
    for element in list2:
        if element not in list1:
            unique.append(element)
    return unique
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = unique_elements(list1, list2)
print(result)'''
#8
'''def is_palindrome(lst):
    reversed_lst = lst[::-1]
    return lst == reversed_lst
my_list = [1, 2, 3, 2, 1]# это полидром
result = is_palindrome(my_list)
print(result)'''
#9
#bubble sort

#homework
#tuple
#1
'''num= (1, 2, 3, 4, 5)
sum= sum(num)
print(sum)'''
#2
'''def a(c):
    b = tuple(set(c))
    return b
strings = ('a','b','c','c')
b = a(strings)
print(b)'''
#2.2
'''def setting(tpl):
    a=set(tpl)
    return tuple(a)
tpl=('','',)
print(setting(tpl))'''
#3
'''def a(c):
    for number in c:
        if number < 0:
            return True
    return False
numbers = (1, 2, -3, 4, 5)
b= a(numbers)
if b:
    print("В кортеже есть отрицательное число.")
else:
    print("В кортеже нет отрицательных чисел.")'''
#4
#4.1
'''def a(c):
    for d in c:
        if len(d) <=5:
            return d
letter = ('oppop','b','bhdjgdb')
result=a(letter)
print(result)'''

#4.2
'''strings = ("adnss", "bnwww", "oefe", "pnekfe", "kfgrg")
strings_2 = tuple(s for s in strings if len(s) < 5)
for s in strings_2:
    print(s)'''
#5
#*args=list,str,tuple
#**kwargs=dict
'''def a(*args):
    b = tuple(sum(t) / len(t) for t in args)
    return b
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (2, 4, 6, 8, 10)
tuple3 = (3, 6, 9, 12, 15)

result = a(tuple1, tuple2, tuple3)
print(result)'''
'''def mid(*args):
    lst=[]
    for i in args:
        lst.append(int(sum(i)/len(i)))
        return tuple(lst)
    tuple1=(1,2,3)
    tuple2=(4,5,6)
print(mid(tuple1,tuple2))'''
#dict
#1
'''grades = {
    "aziz": 85,
    "aziza": 92,
    "marsel": 78,
    "alisher": 90,
    "azamat": 88
}

grades_1 = sum(grades.values())
grade_2 = grades_1 / len(grades)
print("student:", grade_2)'''
'''summa=0
for k,v in grades.items():
    summa+=v
    count+=1
print(summa/count)'''
#2
'''my_dict = {'key1': 'value1', 'key2': 'value2',}

if 'key3' not in my_dict:
    print(my_dict)'''
#3
'''def sorting (dictionary):
    k=lst=[]
    for value in dictionary.keys():
        lst.append(value)
        return sorted'''

#4
'''def keys_1(dictionary):
    keys = list(dictionary.keys())
    keys.sort()
    return keys
my_dict = {'b': 2, 'a': 1, 'c': 3}
result = keys_1(my_dict)
print(result)'''
#5
'''prices = {'apple': 0.5, 'banana': 0.3, 'orange': 0.4, 'grape': 0.8}
max_price_product = max(prices, key=prices.get)
max_price = prices[max_price_product]

min_price_product = min(prices, key=prices.get)
min_price = prices[min_price_product]

print("Самый дорогой продукт:", max_price_product, "Цена:", max_price)
print("Самый дешевый продукт:", min_price_product, "Цена:", min_price)'''

#6
a = {'apple': 3, 'banana': 2, 'orange': 4, 'grape': 8}
b = []
for key in a.keys():
    if isinstance(key, int) and key % 2 == 0:
        b.append(key)
for key in b:
    del a[key]
print(a)




