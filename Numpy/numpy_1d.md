### Работа с одномерными массивами numpy

1. Написать функцию для генерации распределения Пуассона без использования циклов. Это распределение числа событий, произошедших за фиксированное время, 
при условии, что данные события происходят с некоторой фиксированной средней интенсивностью и независимо друг от друга. Оно применяется для моделирования множества важных вещей:
 поломок оборудования, ошибок печати, электрических импульсов детектора фотонов при его облучении лазером. Единственный параметр распределения Пуассона -- среднее 
<img src="https://render.githubusercontent.com/render/math?math=\lambda\ge 0" >. Формула распределения:

<img src="https://render.githubusercontent.com/render/math?math=P(n) = \frac{\lambda^n}{n!}e^{-\lambda}" >

Здесь n -- это значения случайной величины.

Функция на вход принимает значение <img src="https://render.githubusercontent.com/render/math?math=\lambda\ge 0" > (если <img src="https://render.githubusercontent.com/render/math?math=\lambda< 0" >, то генерируется исключение)
и максимальное значение случайной величины N, случайная величина n меняется от 0 до N включительно.

2. Написать функцию для вычисления начальных моментов случайной величины без использования циклов. Начальным моментом называется величина
<img src="https://render.githubusercontent.com/render/math?math=\langle n^k\rangle=\sum_n n^k P(n)" >

На вход функция принимает распределение в виде массива numpy и порядок момента (целое число). Если распределение не является массивом или порядок нецелый, то генерируется исключение.

3. На основе функции из п. 2 реализовать функции вычисления среднего значения случайной величины <img src="https://render.githubusercontent.com/render/math?math=\langle n\rangle" > и 
её дисперсии <img src="https://render.githubusercontent.com/render/math?math=\langle (n - \langle n\rangle)^2\rangle" >.

4. Протестировать функцию из п. 1, вычислив значения среднего и дисперсии распределения Пуассона и сравнив с аналитическими предсказаниями для 3-4 значений <img src="https://render.githubusercontent.com/render/math?math=\lambda" >: 
<img src="https://render.githubusercontent.com/render/math?math=\langle n\rangle=\lambda" > и <img src="https://render.githubusercontent.com/render/math?math=\langle (n - \langle n\rangle)^2\rangle=\lambda" >.
Вычисленные результаты могут с ними не совпадать, если:
	- Вы берете слишком маленькое N, и рассчитанная кривая описывает недостаточную часть истинного распределения
	- Вы уперлись в точность вычислений, в этом случае нужно пользоваться функцией `numpy.allclose`
Полезно будет поиграться с параметрами и попасть в описанные ситуации.

Для более простого тестирования можно воспользоваться инструментами `matplotlib` для построения графиков, например, если Вам надо построить график массива `numpy_arr`, воспользуйтесь командой
```
import matplotlib.pyplot as plt
plt.plot(numpy_arr)
plt.show()
```
Пример использования `matplotlib` можно увидеть в [ноутбуке](https://github.com/vongostev/202-Advanced-Python-1/blob/main/Numpy/MatplotlibBasic.ipynb).

**Бонус:** За каждые 10 заданий из [самоучителя](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises.ipynb) ставится `+`.