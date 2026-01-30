"""
Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()
"""
stroke = input('Input string ')
distinctStroke = set(stroke)
print(f"Quantity distinct chars from stroke = {len(distinctStroke)}")
if len(distinctStroke) > 10:
    print('true')
else:
    print('false')
