Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#1. Найти все числа от 1 до 1000, которые делятся на 17 без остатка

result = 0
for i in range (1,1001):
    if i % 17 == 0:
        result += 1 
print(result)


#2. Найти все числа от 1 до 1000, которые содержат в себе цифру 2 

print(*(i for i in range(0, 1001) if '2' in str(i)))


#3. Найти все числа от 1 до 10000, которые являются палиндромом

for i in range(1,10001):
    for n in range(1,10001):
        number = str(n*i)
        if (number == number[::-1]):
            palindromic = number
            break
print(palindromic)

#4. Посчитать количество пробелов в строке

string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
print(string.count(" "))



#5. Есть любая последовательность непробельных символов латинского алфавита, удалить все гласные из этого слова

vowels = ["a", "e", "i", "o", "u", "y"]
input_str = "HelloEarth"
result = [c for c in input_str if c.lower() not in vowels]
result_str = "".join(result)
print (result_str)


#6. На входе строка со словами, разделенными через 1 пробел. Найти все слова, длина которых не больше 5

text = "'Maty', 'Gahjuro', 'Haus', 'Ikurdfsss', 'Glecho'"
print([e for e in eval('('+text+')') if len(e)<=5])

#7. На входе строка со словами, разделенными через 1 пробел. Получить словарь, где в качестве ключа используется само слово, а в значении длина этого слова.

string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"
new = string.split()
result = {i: len(str(i)) for i in new}
print(result)


#9. На входе список чисел, получить список квадратов этих чисел 

numbers = [2, 3, 4, 6]
def square(x):
    return  x*x 
print(list(map(square, numbers)))


# 11. Возвести в квадрат все четные числа от 2 до 27. На выходе список.

def square(x):
    return x * x
 
arr = [] 

for x in range(2, 27):
    if x % 2 == 0:
        arr.append(square(x))
    print(arr)
    
    
    
#12. На входе список из координат точек на плоскости. Найти расстояние до самой удаленной точку от начала координат (0, 0) в первой четверти

... coords = [(1, 1), (2, 2), (3, 3), (4, 4), (-1, -1), (-1, 5)]
... result_square_distance = {point: point[0] ** 2 + point[1] ** 2 for point in coords if point[0] > 0 and point[1] > 0}
... print(max(result_square_distance))
... 
... #13. На входе два списка чисел nums_first = [1, 2, 3, 5, 8] и nums_second = [2, 4, 8, 16, 32]. Получить пары сумм и разниц, [(3, -1), (6, -2), (11, -5), ...]
... 
... nums_first = [1, 2, 3, 5, 8] 
... nums_second = [2, 4, 8, 16, 32]
... plus_numbers = [x+y for x, y in zip(nums_first, nums_second)] 
... minus_numbers = [x-y for x, y in zip(nums_first, nums_second)]
... print((list(zip (plus_numbers, minus_numbers))))
... 
... #14. На входе список строк из чисел, например, ['43141', '32441', '431', '4154', '43121']. Найти четные квадраты этих чисел. Ответ записать снова в список из строк, то есть сформировать обратно список строк, но уже отфильтровать все четные квадраты
... 
... numbers = ['43141', '32441', '431', '4154', '43121']
... numm = map(int, numbers)
... def square(x):
...     return  x*x 
... print(list(map(square, numm)))
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> #16
>>> a = [[11.9, 12.2, 12.9], 
...     [15.3, 15.1, 15.1],  
...     [16.3, 16.5, 16.5], 
...     [17.7, 17.5, 18.1]] 
...  
... c=[] 
... for i in range (len(a[0])): 
...     stolbtsy=0 
...     for j in range (len(a)): 
...         stolbtsy+=a[j][i] 
...     c.append(stolbtsy) 
...   
