# -*- coding: UTF-8 -*-

from tkinter import *

# Создание окна
root = Tk()

# Массив символов с их переводом на азбуку Морзе
letters = {
    'А': '.-',
    'Б': '-...',
    'В': '.--',
    'Г': '--.',
    'Д': '-..',
    'Е': '.',
    'Ж': '...-',
    'З': '--..',
    'И': '..',
    'Й': '.---',
    'К': '-.-',
    'Л': '.-..',
    'М': '--',
    'Н': '-.',
    'О': '---',
    'П': '.--.',
    'Р': '.-.',
    'С': '...',
    'Т': '-',
    'У': '..-',
    'Ф': '..-.',
    'Х': '....',
    'Ц': '-.-.',
    'Ч': '---.',
    'Ш': '----',
    'Щ': '--.-',
    'Ъ': '.--.-.',
    'Ы': '-.--',
    'Ь': '-..-',
    'Э': '..-..',
    'Ю': '..--',
    'Я': '.-.-',
    ' ': ''
}


# Если зашифровываем, то просчитываем каждую букву в слове, просчитываем каждый элемент в массиве, и если какая-то буква совпала с элементом в массиве, то получаем перевод этой буквы на азбуку Морзе и добавляем перевод в результат, добавляем пробел.
def encrypt(string):
    result = ""
    for i in string:
        for j in letters:
            if i.upper() == j:
                code = letters.get(j)
                result += code + ' '
    return result


# Если расшифровываем, то в конце добавляем пробел для доступа к последнему коду Морзе, создаем доп. переменную для хранения промежуточных результатов, переменную для хранения пробелов. Просчитываем каждый символ, если кол-во пробелов равно 2, добавляем пробел, иначе добавляем букву в результат расшифровки.
def decrypt(string):
    result = ""
    string += " "
    temp = ""
    i = 0
    for k in string:
        if k != " ":
            i = 0
            temp += k
        else:
            i += 1
            if i == 2:
                result += " "
            else:
                result += list(letters.keys())[list(letters.values()).index(temp)]
                temp = ""
    return result


# Создание виджетов
l = Label(root, text="Ввод")
l2 = Label(root, text="Вывод")
e = Entry(root, width=100, font="Arial, 20")
e2 = Label(root, text="Здесь вывод", font="Arial, 20")
b = Button(root, text="Зашифровать", command=lambda: e2.config(text=encrypt(e.get())))
b2 = Button(root, text="Расшифровать", command=lambda: e2.config(text=decrypt(e.get())))

# Располагаем виджеты по сетке
l.grid(row=0, column=0)
l2.grid(row=1, column=0)
e.grid(row=0, column=1)
e2.grid(row=1, column=1)
b.grid(row=0, column=2)
b2.grid(row=1, column=2)

# Вызываем бесконечный цикл, чтобы окно не закрывалось
root.mainloop()
