# -*- coding: UTF-8 -*-

from tkinter import *
from tkinter import messagebox

# Создание окна
root = Tk()

# Массив с кодами районов
regions = {
    "Z": "Железнодорожный",
    "N": "Коминтерновский",
    "F": "Ленинский",
    "R": "Советский",
    "C": "Центральный",
    "0": "За пределами города"
}


# Создаём переменную для хранения результата, перебираем каждый элемент и значение элемента массива. Далее идут проверки на ошибки. Если первый символ кода не содержится в массиве, вызвать 1 вид ошибки. Если номер заказа содержит букву, то вызвать 1 вид ошибки. Если кол-во символов в коде не 5, то вызвать 2 вид ошибки. Далее сам результат. Если первый символ кода - это массиве, то найти его значение в массиве и добавить его в результат. Если первый символ - 0, то не добавлять к результату слово район. Далее добавляем к результату номер заказа(весь код, но без первого символа)
def recognize(string):
    output = ""
    for key, item in regions.items():
        try:
            if not string[0] in str(regions.keys()):
                raise ValueError
            if not string.replace(key, "").isalnum():
                raise ValueError
            if len(string) != 5:
                raise IndexError
            if key == string[0]:
                output += item
                if key != "0":
                    output += " район"
                output += ", номер заказа - " + string.replace(key, "")
                break
        except ValueError:
            messagebox.showerror("Ошибка!", "Ошибка! Недопустимый символ!")
            break
        except IndexError:
            messagebox.showerror("Ошибка!", "Ошибка! Недопустимое количество символов!")
            break
    return output


l = Label(root, text="Ввод")
l2 = Label(root, text="Вывод")
e = Entry(root, width=6)
e2 = Label(root, text="Здесь вывод", width=50)
b = Button(root, text="Определить", command=lambda: e2.config(text=recognize(e.get())))

# Располагаем виджеты по сетке
l.grid(row=0, column=0)
l2.grid(row=1, column=0, sticky=E)
e.grid(row=0, column=1)
e2.grid(row=1, column=1)
b.grid(row=2, column=1)

# Вызываем бесконечный цикл, чтобы окно не закрывалось
root.mainloop()
