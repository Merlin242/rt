#1 Задание


#2 Задание
def anagram(word1, word2):

    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)

word1 = input("первое слово: ")
word2 = input("второе слово: ")
result = anagram(word1, word2)
print('Являются ли слова анаграммами:', result)

#3 Задача
a = int(input())
b = int(input())
c= int(input())

numbers = [a, b, c]
numbers.sort()
print(numbers[1])
#4 Задача
colors = ('красный', 'синий', 'желтый')
color1 = input()
color2 = input()
if color1 in colors and color2 in colors:
 if color1 != color2:
     if (color1 in ('красный', 'синий')) and (color2 in ('синий', 'красный')):
       print('фиолетивый')
       if (color1 in ('красный', 'желтый')) and (color2 in ('желтый', 'красный')):
           print('оранжевый')
           if (color1 in ('синий', 'желтый')) and (color2 in ('синий', 'желтый')):
                 print('зеленый')
     else:
        print(color2)
 else:
  print('ошибка цвета')

  #5 Задание
  n = int(input())

  total = 0
  for num in range(11, n + 1):
      square = num ** 2
      digits = square % 100
      if digits in {2, 52, 5, 88}:
          total += num

  print(total)
  #6 Задание
  number = input()
  decreasing = True

  for i in range(len(number) - 1, 0, -1):
      if int(number[i]) < int(number[i - 1]):
          decreasing = False
          break

  if decreasing:
      print("YES")
  else:
      print("NO")

  #7 Задание
  n = int(input())
  for i in range(1, 7):
      for j in range(n):
          print(i, end='')
      print()

#8 Задание
s = input()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[-1::-2])
#9 Задание
result = [chr(97 + i) * (i + 1) for i in range(26)]
print(result)
