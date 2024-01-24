import numpy as np
import tkinter as tk
from tkinter import messagebox

def calculate_weights(n, comparisons):
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            value = comparisons[(i, j)].get()
            inv_value = 1 / float(value)
            matrix[i, j] = value
            matrix[j, i] = inv_value
    weights = np.mean(matrix, axis=1)
    weights /= np.sum(weights)
    return weights

def submit():
    n = int(num_criteria_entry.get())
    comparisons = {}
    for i in range(n):
        for j in range(i+1, n):
            comparisons[(i, j)] = comparison_entries[(i, j)]
    weights = calculate_weights(n, comparisons)
    result_label.config(text="Весовые коэффициенты: " + " ".join([f"{w:.2f}" for w in weights]))

def request_comparisons():
    n = int(num_criteria_entry.get())
    for i in range(n):
        for j in range(i+1, n):
            comparison_label = tk.Label(window, text=f"Сравните критерий {i+1} и критерий {j+1} (чем больше, тем важнее):")
            comparison_label.pack()
            entry = tk.Entry(window)
            entry.pack()
            comparison_entries[(i, j)] = entry
    submit_button.pack()

# Создание графического интерфейса
window = tk.Tk()
window.title("Метод анализа иерархий Томаса Саати(М.А.И.Т.С.)")
window.geometry("400x600-0+0")

num_criteria_label = tk.Label(window, text="Количество критериев:")
num_criteria_label.pack()
num_criteria_entry = tk.Entry(window)
num_criteria_entry.pack()


result_label = tk.Label(window, text="")
result_label.pack()

request_button = tk.Button(window, text="Ввести данные", command=request_comparisons)
request_button.pack()


comparison_entries = {}
submit_button = tk.Button(window, text="Рассчитать", command=submit)
submit_button.place(x=155, y=120)








window.mainloop()