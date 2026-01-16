# task 01 == Виправте синтаксичні помилки
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter, end="")

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = 4 * apples
print('\nBanana =', banana)

# task 05 == виправте назви змінних
first_side = 1
second_side = 2
third_side = 3
fourth_side = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimeter = first_side + second_side + third_side + fourth_side
print('Perimetr =', perimeter)

"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
appleTree = 4  # Quantity apples trees
pearTree = appleTree + 5  # Quantity pear trees
plumTree = appleTree - 2  # Quantity plum trees
allTrees = appleTree + pearTree + plumTree  # Summ trees
print('All trees =', allTrees)  # The answer

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
zeroTemperature = 0  # Zero temperature
beforeLunchTemperature = zeroTemperature + 5  # Temperature before lunch
afterLunchTemperature = beforeLunchTemperature - 10  # Temperature after lunch
eveningTemperature = afterLunchTemperature + 4  # Temperature in the evening
finalTemperature = eveningTemperature  # Final temperatura and answer on the main question (redundant step, but for child will be good option)
print('Evening temperature =', eveningTemperature)  # Print main answer

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
quantityBoys = 24  # Quantity of all boys
quantityGirls = quantityBoys / 2  # Quantity of all girls
illBoys = 1  # Quantity of ill boys
absentGirls = 2  # Quantity of ill girls
summChildren = quantityBoys + quantityGirls - (illBoys + absentGirls)  # Overall of all children
print('Overall Children =', int(summChildren))  # Print overall of all children (without int show 33.00)
# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
firstBookPrice = 8  # Price of first book
secondBookPrice = firstBookPrice + 2  # Price of second book
thirdBookPrice = (firstBookPrice + secondBookPrice) // 2  # Price of third book (// to get int number)
summBooksPrise = firstBookPrice + secondBookPrice + thirdBookPrice  # Overall price of all books
print('Overall books price =', summBooksPrise)  # Print overall of all  books
