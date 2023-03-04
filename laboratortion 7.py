# Балахничёва Мария ИСУ 367852 группа R3141
import time                                 # импортируем все необходимые нам библиотеки
from time import perf_counter
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import PillowWriter


# первый пункт 
def create_array(n):            # генерируем массивы
    a = []
    for i in range(n):
        x = random.randint(1, 1000)
        a.append(x)
    return a


def multip_normal(n):               # перемножаем массивы без использования NumPy, в ручную
    a = create_array(n)
    b = create_array(n)
    c = []
    t_start = time.perf_counter()     # записываем время, в которое начали вычисления
    for i in range(n):
        c.append(a[i]*b[i])
    all_time = time.perf_counter()-t_start     # считаем, сколько времени заняло перемножение
    return all_time

def multip_numpy(n):                # перемножаем массивы, используя NumPy. Аналогично прошлой функции засекаем время
    a = create_array(n)
    b = create_array(n)
    t_start = time.perf_counter()
    np.multiply(a, b)
    all_time = time.perf_counter()-t_start
    return all_time

print(f"{multip_numpy(1000000)} - время умножения в NumPy")
print(f"{multip_normal(1000000)} - время умножения без NumPy")


# второй пункт

numbers = np.genfromtxt('data2.csv', delimiter = ',', names = True)    # считываем весь файл с данными
data = numbers['ph']                    # выделяем нужный нам столбец
data = data.astype(float)               # переводим данные из строкового в численный тип
data= data[~np.isnan(data)]             # избавляемся от пустых строк в массиве

plt.hist(data, color = 'lightblue', ec = 'blue', bins=40)   # строим гистограмму, задаем ширину столбцов их цвет и окантовку
plt.title('Гистограмма')              # задаем название гистограммы
plt.xlabel('ph')                      # подписываем оси
plt.ylabel('частота')
plt.minorticks_on()                   # я решила добавить дополнительное разделение осей
plt.show()                            # выводим график

plt.hist(data, color = 'lightpink', ec = 'red', bins=40, density=True)   # аналогично строим нормализованную гистограмму
plt.title('Нормализованная гистограмма')
plt.xlabel('ph')
plt.ylabel('частота')
plt.minorticks_on()
plt.show()

sr_kvad_otkl = np.std(data)                                 # считаем среднеквадратичное отклонение
print(f'{sr_kvad_otkl} - среднеквадратичное отклонение')

# третий пункт

x = np.linspace(-2*np.pi, 2*np.pi, 50)              # задаем функции для графика
y = np.cos(x)*np.sin(x)
z = np.cos(x)*np.sin(x)

fig = plt.figure()                                  # строим график
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label = 'График для 3 пункта')
plt.show()

#дополнительное задание


def animation_sin():  
    fig = plt.figure()
    l, = plt.plot([], [], 'k-')  # без запятой после l не работает
    plt.xlabel('x')
    plt.ylabel('y')  # в едином стиле задали оси
    plt.title('Анимированный график синуса')
    plt.xlim(-5, 5)  
    plt.ylim(-2, 2)
    plt.setp(l, color='lightpink')  
    writer = PillowWriter(fps=60)  
    px = []  
    py = []  
    with writer.saving(fig, "SinAnimation.gif", 100):
        for x in np.linspace(-5, 5, 100):  
            px.append(x)  
            py.append(np.sin(x))  
            l.set_data(px, py)  
            writer.grab_frame() 
animation_sin()


