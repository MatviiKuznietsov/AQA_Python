adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""
print(adwentures_of_tom_sawer)

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
print('Task 01============================================================================')
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer_new_line = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer_new_line)
print('Task 02 ============================================================================')
# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer_without_dots = adwentures_of_tom_sawer_new_line.replace("....", " ")
print(adwentures_of_tom_sawer_without_dots)
print('Task 03============================================================================')
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer_with_one_space = adwentures_of_tom_sawer_without_dots.replace("  ", "")
print(adwentures_of_tom_sawer_with_one_space)
print('Task 04============================================================================')
# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
words = adwentures_of_tom_sawer.split()
count = 0
for word in words:
    if 'h' in word.lower():
        count += 1
print(f'Quantity words with "h" = {count}')
print('Task 05============================================================================')
# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
words = adwentures_of_tom_sawer.split()
count = 0
for word in words:
    if word.istitle():
        count = count + 1
print(f'Quantity words start with capital letter = {count}')
print('Task 06============================================================================')
# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
positionWordTom = adwentures_of_tom_sawer.find('Tom', adwentures_of_tom_sawer.find('Tom') + 1)
print(f'Position "Tom" word  = {positionWordTom}')
print('Task 07============================================================================')
# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = [
    s.strip() for s in (
        adwentures_of_tom_sawer
        .replace("\n", " ")
        .replace("....", " ")
        .replace("  ", " ")
        .split('.')
    ) if s.strip()
]
print(adwentures_of_tom_sawer_sentences)
print('Task 08============================================================================')
# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(f'Fourth sentence - {adwentures_of_tom_sawer_sentences[3].lower()}')
print('Task 09============================================================================')
# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
count = 0
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.strip().startswith('By the time'):
        count = count + 1
print(f'{count} sentens begin from "By the time"')
print('Task 10============================================================================')
# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print(f'{len(adwentures_of_tom_sawer_sentences[-1].split())} words in the last sentence')
