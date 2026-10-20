#Вариант 12
text = str(input("Введите текст: "))
words = text.split()

words1 = []
n = 0
for word in words:
    word = word.strip(".,!?;:").lower()
    words1.append(word)
    if "ра" in word:
        n += 1
        print(word)

if n != 0:
    print(f"Количество: {n}")
else:
    print("Нет совпадений и количество 0")