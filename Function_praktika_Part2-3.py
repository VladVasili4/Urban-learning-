import tkinter as tk
def num_in():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    return num1, num2
def num_out(values):  # почему тут values ?
    answery.delete(0, 'end')  # для очистки поля вывода от предыдущих расчетов
    answery.insert(0, values)  # почему тут values ?
def plus_():
    num1, num2 = num_in()
    result = num1 + num2
    num_out(result)  # здесь мы вызываем функцию, указывая аргумент(result),
    # который становится параметром этой функции (num_out).
    # Поэтому (result) идет вместо (values), а уже потом
    # передается в answery.insert(0, values).
def minus_():
    num1, num2 = num_in()
    result = num1 - num2
    num_out(result)
def umnozh_():
    num1, num2 = num_in()
    result = num1 * num2
    num_out(result)
def div_():
    num1, num2 = num_in()
    result = num1 / num2
    num_out(result)

window = tk.Tk()

window.title('Calculator')
window.geometry('350x350')
window.resizable(False, False)
button_add = tk.Button(window, text='+', command=plus_)  # размеры кнопки можно задать и тут
button_add.place(x=100, y=200, width=30, height=30)  # есть еще методы грид и пат (кроме плэйс)
button_min = tk.Button(window, text='-', command=minus_)
button_min.place(x=150, y=200, width=30, height=30)
button_umn = tk.Button(window, text='*', command=umnozh_)
button_umn.place(x=100, y=250, width=30, height=30)
button_delen = tk.Button(window, text='/', command=div_)
button_delen.place(x=150, y=250, width=30, height=30)
entry1 = tk.Entry(window)
entry1.place(x=100, y=50, width=150, height=20)
entry2 = tk.Entry(window)
entry2.place(x=100, y=100, width=150, height=20)
answery = tk.Entry(window)
answery.place(x=100, y=150, width=150, height=20)
number1 = tk.Label(window, text='Enter first digit')
number1.place(x=100, y=25, width=150, height=20)
number2 = tk.Label(window, text='Enter second digit')
number2.place(x=100, y=75, width=150, height=20)
answeri = tk.Label(window, text='Answer')
answeri.place(x=100, y=125, width=150, height=20)

window.mainloop()

