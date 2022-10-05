# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# file = open("words.txt", 'w')
# while True:
#     s=input('Введите исходный текст:')
#     # if s == "":
#     break
#     file.write(s)
# file.close()

# words.txt: Напишите Напабвишите программу, удаляющую из абв текста все слова, содерабвжащие ""абв""
with open("words.txt", encoding='utf_8') as fin:
    for line in fin:
        words=line.split()
        for word in words:
            if 'абв' in word:
                words.remove(word)
        result= " ".join(words)
        print(result)

