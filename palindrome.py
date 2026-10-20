text = input("Введите текст: ")
text_filtered = text.strip()

palindrome = ' '
text_z = ' '

for z in text_filtered[::1]:
    if z == " ":
        continue
    else:
        text_z += z

for i in text_filtered[::-1]:
    if i == " ":
        continue
    else:
        palindrome += i

text_final = text_z.lower().strip()
palindrome_final = palindrome.lower().strip()

if len(text.strip()) == 0:
    print("Нет текста")
else:
    if text_final == palindrome_final:
        print("Палиндром")
    else:
        print("Не палиндром")