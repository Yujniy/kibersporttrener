import tkinter as tk
from tkinter import messagebox

# Параметры для мужчин и женщин
clicks_male = 205
clicks_female = 195
time_limit = 30

# Функция для обработки выбора пола
def choose_gender():
    global click_limit, time_remaining
    gender = gender_var.get()
    if gender == "Мужчина":
        click_limit = clicks_male
    elif gender == "Женщина":
        click_limit = clicks_female
    else:
        messagebox.showerror("Ошибка", "Пожалуйста, выберите пол")
        return
    label_clicks.config(text="Клики: 0 / " + str(click_limit))
    button.config(state=tk.NORMAL)
    time_remaining = time_limit
    update_time()

# Функция для обработки кликов
def click_button():
    global click_count, click_limit
    click_count += 1
    label_clicks.config(text="Клики: " + str(click_count) + " / " + str(click_limit))
    if click_count >= click_limit:
        button.config(state=tk.DISABLED)
        messagebox.showinfo("Информация", "Вы достигли лимита кликов")

# Функция для обновления времени
def update_time():
    global time_remaining
    if time_remaining > 0:
        time_remaining -= 1
        label_time.config(text="Время: " + str(time_remaining) + " сек")
        root.after(1000, update_time)
    else:
        button.config(state=tk.DISABLED)
        messagebox.showinfo("Информация", "Время истекло")

# Создание окна
root = tk.Tk()
root.title("Программа с кнопкой кликать")

# Создание метки и выпадающего списка для выбора пола
gender_var = tk.StringVar()
gender_var.set("Мужчина")
label_gender = tk.Label(root, text="Выберите пол:")
label_gender.pack()
dropdown_gender = tk.OptionMenu(root, gender_var, "Мужчина", "Женщина")
dropdown_gender.pack()

# Создание кнопки выбора пола
button_choose_gender = tk.Button(root, text="Выбрать", command=choose_gender)
button_choose_gender.pack()

# Создание кнопки
click_count = 0
click_limit = 0
button = tk.Button(root, text="Кликни!", command=click_button, state=tk.DISABLED)
button.pack()

# Создание метки для счетчика кликов
label_clicks = tk.Label(root, text="Клики: 0 / " + str(click_limit))
label_clicks.pack()

# Создание метки для времени
time_remaining = time_limit
label_time = tk.Label(root, text="Время: " + str(time_remaining) + " сек")
label_time.pack()

# Запуск программы
root.mainloop()
