# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

print(words.txt)

with open("text.txt", "r") as fin:
    for line in fin:
        text=line.split()
        for word in words:
            if "абв" in word:
                words.remove(word)
        result=" ".join(words)
        print(result)