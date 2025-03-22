import random
import matplotlib.pyplot as plt
import numpy as np

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

                # if exist[-1] == 4 and 2 in lst:
                #     lst.remove(2)
                # if exist[-1] == 5 and 3 in lst:
                #     lst.remove(3)
                # if (exist[-1] == 3 or 4 in exist) and 5 in lst:
                #     lst.remove(5)

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


                # if exist[-1] == 5 and 3 in lst:
                #     lst.remove(3)
                # if (exist[-1] == 3 or 4 in exist) and 5 in lst:
                #     lst.remove(5)
            
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
        
        print(choice, x, y)
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


def generate_data():
    x = np.round(np.arange(0, 5.01, 0.01), 2)
    y = np.concatenate((np.arange(3.0, 1.0, -0.01), 
                        np.ones(100), 
                        np.arange(1.0, 2.0, 0.01), 
                        np.arange(2.0, 0.99, -0.01)))
    return x.tolist(), np.round(y, 2).tolist()

def count_unique(y_list):
    return [{str(val): y_list.count(val)} for val in sorted(set(y_list))]

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
    blocks = []  # Пустой список для блоков
    types = []   # Пустой список для типов
    direction = None  # Начальное направление None, чтобы отличать первый блок

    for i, x in enumerate(x_list):
        if y_list.count(y_list[i]) == 3:  # Если y встречается ровно 3 раза
            current_direction = directions[i]
            if current_direction != direction:  # Если направление изменилось
                direction = current_direction
                blocks.append([x])  # Начать новый блок с текущим x
                types.append(direction)  # Добавить новое направление
            elif direction in ["up", "down"]:  # Если направление то же и оно "up" или "down"
                blocks[-1].append(x)  # Добавить x в текущий блок

    return blocks, types

def main():
    while True:
        x_values, y_values = create_graphik()
        if x_values is not None and y_values is not None:
            break
        
    plt.plot(x_values, y_values, label="Regions")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Graph of Mixed Regions")
    plt.legend()
    plt.grid(True)

    plt.xlim([0, 5.2])
    plt.ylim([0, 4.2]) 
    plt.xticks(np.arange(0, np.ceil(plt.xlim()[1]), 1))
    plt.yticks(np.arange(0, np.ceil(plt.ylim()[1]), 1))
    plt.show()

    x_list, y_list = np.round(x_values, 2).tolist(), np.round(y_values, 2).tolist()
    directions = determine_directions(y_list)
    blocks, types = find_blocks(x_list, y_list, directions)
    
    if not blocks:  # Проверка на случай, если блоков нет
        print("Блоков не найдено.")
        return
    lst_blocks = [i for i in range(len(blocks)) if len(blocks[i]) == 99]
    num = random.choice(lst_blocks)  # Выбор случайного блока
    print(types)
    print(num)
    print(f"Напишите класс эквивалентности [x], где x ∈ ({int(blocks[num][0] - 0.01)}; {int(blocks[num][-1] + 0.01)})")

    strings = sorted(input("Введите формулу\n").split(";"), key=len)
    check = random.choice(blocks[num])
    
    check_y = next((y_list[i] for i in range(len(x_list)) if x_list[i] == check), None)
    lst_x = [x for i, x in enumerate(x_list) if y_list[i] == check_y]
    
    print(strings)
    print(lst_x)
    print(strings)

    if len(strings) != 3 or len(set(strings)) != 3:
        print("Должно быть ровно три уникальные формулы")
    else:
        results = [round(eval(expr, {"x": check}), 2) for expr in strings]
        if set(results) == set(lst_x):
            print("Класс эквивалентности найден правильно")
        else:
            print("Попробуй ещё раз")
            
if __name__ == "__main__":
    main()
        