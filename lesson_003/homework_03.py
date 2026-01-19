import math

alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n'
                       '"Then it doesn\'t matter which way you go," said the Cat.\n'
                       '"—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
print('\n===Task_04===')
areaBlackSea = 436402  # area of Black Sea in square km
areaAzovSea = 37800  # area of Azov Sea in square km
overallArea = areaBlackSea + areaAzovSea  # add both areas
print('Overall area Azov sea and Black sea =', overallArea, 'km')  # print result
# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
print('\n===Task_05===')
quantityAllGoods = 375291  # total goods in all storages
quantityGoodsFirstAndSecondStorage = 250449  # goods in first + second storage
quantityGoodsThirdAndSecondStorage = 222950  # goods in third + second storage
quantityGoodsFirstStorage = quantityAllGoods - quantityGoodsThirdAndSecondStorage  # first storage only
quantityGoodsThirdStorage = quantityAllGoods - quantityGoodsFirstAndSecondStorage  # third storage only
quantityGoodsSecondStorage = quantityAllGoods - (
            quantityGoodsFirstStorage + quantityGoodsThirdStorage)  # second storage
# Print number of goods in each storage
print('First storage contains =', quantityGoodsFirstStorage, 'goods'
                                                             '\nSecond storage contains =', quantityGoodsSecondStorage,
      'goods'
      '\nThird storage contains =', quantityGoodsThirdStorage, 'goods')
# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
print('\n===Task_06===')
termLength = 1.5  # 1.5 years
termMonth = 1.5 * 12  # convert years to months
priceOneMonth = 1179  # monthly payment in grn
pricePc = priceOneMonth * termMonth  # total price of the computer
print('Pc price =', int(pricePc), 'grn')  # print total price as integer
# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print('\n===Task_07===')
numA1 = 8019
numA2 = 8
numB1 = 9907
numB2 = 9
numC1 = 2789
numC2 = 5
numD1 = 7248
numD2 = 6
numE1 = 7128
numE2 = 5
numF1 = 19224
numF2 = 9
# calculate remainders
answerA = numA1 % numA2  # remainder of 8019 / 8
answerB = numB1 % numB2  # remainder of 9907 / 9
answerC = numC1 % numC2  # remainder of 2789 / 5
answerD = numD1 % numD2  # remainder of 7248 / 6
answerE = numE1 % numE2  # remainder of 7128 / 5
answerF = numF1 % numF2  # remainder of 19224 / 9
# print all remainders
print('"A" remainder of division =', answerA,
      '\n"B" remainder of division =', answerB,
      '\n"C" remainder of division =', answerC,
      '\n"D" remainder of division =', answerD,
      '\n"E" remainder of division =', answerE,
      '\n"F" remainder of division =', answerF)
# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
print('\n===Task_08===')
pizzaBig = 274  # price for big pizza
quantityPizzaBig = 4  # quantity big pizza
pizzaMiddle = 218  # price for medium pizza
quantityPizzaMiddle = 2  # quantity medium pizza
Juice = 35  # price for juice
quantityJuice = 4  # quantity juice
Cake = 350  # price for cake
quantityCake = 1  # quantity cake
Water = 21  # price for water
quantityWater = 3  # quantity water
# calculate total price
overallPrice = sum([pizzaBig * quantityPizzaBig,
                    pizzaMiddle * quantityPizzaMiddle,
                    Juice * quantityJuice,
                    Cake * quantityCake,
                    Water * quantityWater])
print('Overall order price =', overallPrice)
# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
print('\n===Task_09===')
quantityPhotos = 232  # total photos
maxQuantityPhotos = 8  # max photos per page
quantityPages = math.ceil(232 / 8)
print('Quantity pages =', quantityPages)
# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
print('\n===Task_10===')
distanceKharkivBudapest = 1600  # distance in km
defaultDistance = 100  # every 100 km
quantityGasolineOnOneHundredKm = 9  # liters needed per 100 km
tankCapacity = 48  # tank capacity in liters
# total gasoline needed for trip
quantityGasolineOnTrip = distanceKharkivBudapest / defaultDistance * quantityGasolineOnOneHundredKm
# minimum number of tank refills (round up)
minNumberTankRefills = math.ceil(quantityGasolineOnTrip / tankCapacity)
# print results
print('Quantity Gasoline On Trip =', int(quantityGasolineOnTrip),
      '\nMin Number Tank Refills = ', minNumberTankRefills)
