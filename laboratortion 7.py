import time
from time import perf_counter
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# первый пункт 
def create_array(n):
    a = []
    for i in range(n):
        x = random.randint(1, 1000)
        a.append(x)
    return a


def multip_normal(n):
    a = create_array(n)
    b = create_array(n)
    c = []
    t_start = time.perf_counter()
    for i in range(n):
        c.append(a[i]*b[i])
    all_time = time.perf_counter()-t_start
    return all_time

def multip_numpy(n):
    a = create_array(n)
    b = create_array(n)
    t_start = time.perf_counter()
    np.multiply(a, b)
    all_time = time.perf_counter()-t_start
    return all_time

#print(f"{multip_numpy(1000000)} - время умножения в NumPy")
#print(f"{multip_normal(1000000)} - время умножения без NumPy")


# второй пункт

numbers = np.genfromtxt('data2.csv', delimiter = ',', names = True)
data = numbers['ph']
data = data.astype(float)
data= data[~np.isnan(data)]  #избавляемся от пустых строк в массиве

plt.hist(data, color = 'lightblue', ec = 'blue', bins=40)
plt.title('Гистограмма')
plt.xlabel('ph')
plt.ylabel('частота')
plt.minorticks_on()
plt.show()

plt.hist(data, color = 'lightpink', ec = 'red', bins=40, density=True)
plt.title('Нормализованная гистограмма')
plt.xlabel('ph')
plt.ylabel('частота')
plt.minorticks_on()
plt.show()

sr_kvad_otkl = np.std(data)
print(f'{sr_kvad_otkl} - среднеквадратичное отклонение')

# третий пункт

x = np.linspace(-2*np.pi, 2*np.pi, 50)
y = np.cos(x)*np.sin(x)
z = np.cos(x)*np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label = 'График для 3 пункта')
plt.show()