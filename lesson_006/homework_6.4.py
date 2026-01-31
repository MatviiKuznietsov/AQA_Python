"""
Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
"""
lst1 = [1, 1, 33, 4, 22, 6, 324, 8, 9, 10]
summOdd = 0
summEven = 0
for i in lst1:
    if i % 2 == 0:
        summEven = summEven + int(i)
    else:
        summOdd = summOdd + int(i)
print(f"Summ odd numbers={summOdd}\nSumm even numbers={summEven}")
