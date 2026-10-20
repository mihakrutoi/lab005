text = str(input("Введите текст: "))
text_normalized = ' '.join(text.strip().split())
if len(text_normalized) != 0:
    number = int(text_normalized.count(' ')) + 1
else:
    number = 0

print(f'''
    Длина исходного текста: {len(text)}
    Длина полученного текста: {len(text_normalized)}
    Полученный текст: {text_normalized}
    Количество слов: {number}''')