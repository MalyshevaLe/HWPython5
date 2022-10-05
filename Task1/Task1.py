# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def del_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

with open("text.txt", "r") as fin:
    for line in fin:
        text=line.split()
        for word in words:
            if "абв" in word:
                words.remove(word)
        result=" ".join(words)
        print(result)