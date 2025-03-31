import sys
import random
import numpy as np
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QMessageBox, QSizePolicy)
from PyQt5.QtCore import QDateTime, Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# Функции из оригинального кода для генерации графика
def create_graphik():
    exist = []
    x, y = 0, random.randint(0, 4)
    x_all, y_all = np.array([]), np.array([])
    checked_up = True
    checked_down = True
    choice = None
    while len(exist) != 4:
        if x > 5:
            return None, None
        if y == 0 or (y == 1 and x == 0):
            lst = [1, 2, 4]
            for item in exist:
                if item in lst:
                    lst.remove(item)  

            if len(exist) != 0:
                if checked_up == False:
                    if 2 in lst:
                        lst.remove(2)
                    if 4 in lst:
                        lst.remove(4)
                if 5 in exist and 4 in lst:
                    lst.remove(4)
                

            if len(lst) != 0:
                choice = random.choice(lst)

                if choice:
                    if choice == 2:
                        checked_up = False
                        if checked_down == False:
                            checked_down = True
                    if choice == 4:
                        checked_up = False
                        if checked_down == False:
                            checked_down = True
                exist.append(choice)

        elif y == 1:
            lst = [1, 2, 3, 4]
            for item in exist:
                if item in lst:
                    lst.remove(item)
            
            if len(exist) != 0:
                if checked_up == False:
                    if 2 in lst:
                        lst.remove(2)
                    if 4 in lst:
                        lst.remove(4)
                if 5 in exist and 4 in lst:
                    lst.remove(4)

                if checked_down == False:
                    if 3 in lst:
                        lst.remove(3)

            if len(lst) != 0:
                choice = random.choice(lst)
                if choice:
                    if choice == 2:
                        checked_up = False
                        if checked_down == False:
                            checked_down = True
                    if choice == 4:
                        checked_up = False
                        if checked_down == False:
                            checked_down = True
                    if choice == 3:
                        checked_down = False
                        if checked_up == False:
                            checked_up = True
                exist.append(choice)
    
        elif y == 2:
            lst = [1, 2, 3, 4, 5]
            for item in exist:
                if item in lst:
                    lst.remove(item)
            
            if len(exist) != 0:
                if checked_up == False:
                    if 2 in lst:
                        lst.remove(2)
                    if 4 in lst:
                        lst.remove(4)
                if 5 in exist and 4 in lst:
                    lst.remove(4)

                if checked_down == False:
                    if 3 in lst:
                        lst.remove(3)
                    if 5 in lst:
                        lst.remove(5)
                if 4 in exist and 5 in lst:
                    lst.remove(5)
                

            if len(lst) != 0:
                choice = random.choice(lst)
                if choice:
                    if choice == 2:
                        checked_up = False
                        if checked_down == False:
                            checked_down = True
                    if choice == 4:
                        checked_up = False
                        if checked_down == False:
                            checked_down = True
                    if choice == 3:
                        checked_down = False
                        if checked_up == False:
                            checked_up = True
                    if choice == 5:
                        checked_down = False
                        if checked_up == False:
                            checked_up = True
                exist.append(choice)

        elif y == 3 and x != 0:
            lst = [1, 2, 3, 5]
            for item in exist:
                if item in lst:
                    lst.remove(item)
            
            if len(exist) != 0:
                if checked_up == False:
                    if 2 in lst:
                        lst.remove(2)

                if checked_down == False:
                    if 3 in lst:
                        lst.remove(3)
                    if 5 in lst:
                        lst.remove(5)
                if 4 in exist and 5 in lst:
                    lst.remove(5)

            if len(lst) != 0:
                choice = random.choice(lst)
                if choice:
                    if choice == 2:
                        checked_up = False
                        if checked_down == False:
                            checked_down = True
                    if choice == 3:
                        checked_down = False
                        if checked_up == False:
                            checked_up = True
                    if choice == 5:
                        checked_down = False
                        if checked_up == False:
                            checked_up = True
                exist.append(choice)

        elif y == 4 or (y == 3 and x == 0):
            lst = [1, 3, 5]
            for item in exist:
                if item in lst:
                    lst.remove(item)
            
            if len(exist) != 0:
                if checked_down == False:
                    if 3 in lst:
                        lst.remove(3)
                    if 5 in lst:
                        lst.remove(5)
                if 4 in exist and 5 in lst:
                    lst.remove(5)
            
            if len(lst) != 0:
                choice = random.choice(lst)
                if choice:
                    if choice == 3:
                        checked_down = False
                        if checked_up == False:
                            checked_up = True
                    if choice == 5:
                        checked_down = False
                        if checked_up == False:
                            checked_up = True
                exist.append(choice)
        
        if choice == 1:
            x1, y1, x, y = create_region1(x, y)
            x_all = np.concatenate((x_all, x1))
            y_all = np.concatenate((y_all, y1))
        elif choice == 2:
            x2, y2, x, y = create_region2(x, y)
            x_all = np.concatenate((x_all, x2))
            y_all = np.concatenate((y_all, y2))
        elif choice == 3: 
            x3, y3, x, y = create_region3(x, y)
            x_all = np.concatenate((x_all, x3))
            y_all = np.concatenate((y_all, y3))
        elif choice == 4:
            x4, y4, x, y = create_region4(x, y)
            x_all = np.concatenate((x_all, x4))
            y_all = np.concatenate((y_all, y4))
        elif choice == 5:
            x5, y5, x, y = create_region5(x, y)
            x_all = np.concatenate((x_all, x5))
            y_all = np.concatenate((y_all, y5))
        
    sorted_indices = np.argsort(x_all)
    x_sorted = x_all[sorted_indices]
    y_sorted = y_all[sorted_indices]
    return x_sorted, y_sorted

def create_region1(start_x, start_y):
    delay = 0.01
    const_value = start_y
    end_x = np.arange(start_x, start_x + 1 + delay, delay)
    end_y = np.full_like(end_x, const_value)
    x, y = start_x + 1, start_y
    return end_x, end_y, x, y

def create_region2(start_x, start_y):
    delay = 0.01
    end_x = np.arange(start_x, start_x + 1 + delay, delay)
    end_y = np.arange(start_y, start_y + 1 + delay, delay)
    x, y = start_x + 1, start_y + 1
    return end_x, end_y, x, y

def create_region3(start_x, start_y):
    delay = 0.01
    end_x = np.arange(start_x, start_x + 1 + delay, delay)
    end_y = -end_x + (start_y + start_x)
    x, y = start_x + 1, start_y - 1
    return end_x, end_y, x, y

def create_region4(start_x, start_y):
    delay = 0.01
    end_x = np.arange(start_x, start_x + 2 + delay, delay)
    end_y = np.arange(start_y, start_y + 2 + delay, delay)
    x, y = start_x + 2, start_y + 2
    return end_x, end_y, x, y

def create_region5(start_x, start_y):
    delay = 0.01
    end_x = np.arange(start_x, start_x + 2 + delay, delay)
    end_y = -end_x + (start_y + start_x)
    x, y = start_x + 2, start_y - 2
    return end_x, end_y, x, y

def determine_directions(y_list):
    directions = ["stand"] * len(y_list)
    for i in range(1, len(y_list)):
        if y_list[i] in {0.0, 1.0, 2.0, 3.0, 4.0}:
            directions[i] = "stand"
        elif y_list[i] > y_list[i - 1]:
            directions[i] = "up"
        elif y_list[i] < y_list[i - 1]:
            directions[i] = "down"
    return directions

def find_blocks(x_list, y_list, directions):
    blocks = []
    types = []  
    direction = None 

    for i, x in enumerate(x_list):
        if y_list.count(y_list[i]) == 3: 
            current_direction = directions[i]
            if current_direction != direction:
                direction = current_direction
                blocks.append([x])
                types.append(direction)
            elif direction in ["up", "down"]:
                blocks[-1].append(x)

    return blocks, types

class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ввод данных')
        self.fio_label = QLabel('ФИО:')
        self.fio_edit = QLineEdit()
        self.group_label = QLabel('Номер группы:')
        self.group_edit = QLineEdit()
        self.start_btn = QPushButton('Начать')
        self.start_btn.clicked.connect(self.on_start)

        layout = QVBoxLayout()
        layout.addWidget(self.fio_label)
        layout.addWidget(self.fio_edit)
        layout.addWidget(self.group_label)
        layout.addWidget(self.group_edit)
        layout.addWidget(self.start_btn)
        self.setLayout(layout)

    def on_start(self):
        fio = self.fio_edit.text().strip()
        group = self.group_edit.text().strip()
        if not fio or not group:
            QMessageBox.warning(self, 'Ошибка', 'Заполните все поля')
            return
        self.graph_window = GraphWindow(fio, group)
        self.graph_window.show()
        self.close()

class GraphWindow(QWidget):
    def __init__(self, fio, group):
        super().__init__()
        self.fio = fio
        self.group = group
        self.start_time = QDateTime.currentDateTime()
        self.x_list = []
        self.y_list = []
        self.blocks = []
        self.types = []
        self.lst_blocks = []
        self.num = 0
        self.initUI()
        self.generate_graph()

    def initUI(self):
        self.setWindowTitle('График и ввод формулы')
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.task_label = QLabel()
        self.formula_label = QLabel('Введите формулы (разделяйте ";"):')
        self.formula_edit = QLineEdit()
        self.submit_btn = QPushButton('Отправить')
        self.submit_btn.clicked.connect(self.on_submit)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.task_label)
        layout.addWidget(self.formula_label)
        layout.addWidget(self.formula_edit)
        layout.addWidget(self.submit_btn)
        self.setLayout(layout)

    def generate_graph(self):
        while True:
            x_values, y_values = create_graphik()
            if x_values is not None and y_values is not None:
                break

        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.plot(x_values, y_values, label="Regions")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_title("Graph of Mixed Regions")
        ax.legend()
        ax.grid(True)
        ax.set_xlim([0, 5.2])
        ax.set_ylim([0, 4.2])
        ax.set_xticks(np.arange(0, 6, 1))
        ax.set_yticks(np.arange(0, 5, 1))
        self.canvas.draw()

        self.x_list = np.round(x_values, 2).tolist()
        self.y_list = np.round(y_values, 2).tolist()
        directions = determine_directions(self.y_list)
        self.blocks, self.types = find_blocks(self.x_list, self.y_list, directions)
        if not self.blocks:
            QMessageBox.critical(self, 'Ошибка', 'Блоков не найдено')
            self.close()
            return
        self.lst_blocks = [i for i in range(len(self.blocks)) if len(self.blocks[i]) == 99]
        if not self.lst_blocks:
            QMessageBox.critical(self, 'Ошибка', 'Подходящих блоков не найдено')
            self.close()
            return
        self.num = random.choice(self.lst_blocks)
        start = int(self.blocks[self.num][0] - 0.01)
        end = int(self.blocks[self.num][-1] + 0.01)
        self.task_label.setText(f"Напишите класс эквивалентности [x], где x ∈ ({start}; {end})")

    def on_submit(self):
        formulas = [f.strip() for f in self.formula_edit.text().split(';') if f.strip()]
        if len(formulas) != 3 or len(set(formulas)) != 3:
            QMessageBox.warning(self, 'Ошибка', 'Должно быть ровно три уникальные формулы')
            return

        check = random.choice(self.blocks[self.num])
        check_y = next((y for x, y in zip(self.x_list, self.y_list) if x == check), None)
        lst_x = [x for x, y in zip(self.x_list, self.y_list) if y == check_y]

        results = []
        try:
            for expr in formulas:
                result = round(eval(expr, {'x': check}), 2)
                results.append(result)
        except Exception as e:
            QMessageBox.warning(self, 'Ошибка', f'Ошибка в формуле: {str(e)}')
            return

        if set(results) == set(lst_x):
            result_text = 'Класс эквивалентности найден правильно'
        else:
            result_text = 'Попробуйте ещё раз'

        end_time = QDateTime.currentDateTime()
        self.result_window = ResultWindow(self.fio, self.group, self.start_time, end_time, result_text)
        self.result_window.show()
        self.close()

class ResultWindow(QWidget):
    def __init__(self, fio, group, start_time, end_time, result):
        super().__init__()
        self.fio = fio
        self.group = group
        self.start_time = start_time
        self.end_time = end_time
        self.result = result
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Результаты')
        layout = QVBoxLayout()
        labels = [
            f'ФИО: {self.fio}',
            f'Группа: {self.group}',
            f'Время начала: {self.start_time.toString(Qt.DefaultLocaleLongDate)}',
            f'Время окончания: {self.end_time.toString(Qt.DefaultLocaleLongDate)}',
            f'Результат: {self.result}'
        ]
        for text in labels:
            label = QLabel(text)
            layout.addWidget(label)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    start_win = StartWindow()
    start_win.show()
    sys.exit(app.exec_())