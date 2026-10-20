text = input("Введите текст: ")
counted = text.count(":")
text_changed = text.replace(":", "-")
print(f"{text_changed}, количество замен: {counted}")