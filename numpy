 import matplotlib.pyplot as plt
 import numpy as np
 import scipy.special as sci


 def Puasson(lambda, N):
     if lambda < 0:
         raise ValueError("Lambda must be positive")
     numpy_arr = np.arange(N)
     return lambda ** numpy_arr * np.exp(-lambda) / sci.factorial(numpy_arr)


 def Moment(arr, k=1):
     if k < 0:
         raise ValueError('"k" must be positive')
     elif k % 1:
         raise ValueError('"k" must be integer')
     elif not isinstance(arr, np.ndarray):
         raise ValueError('Wrong array format')
     return np.sum(arr * np.arange(len(arr)) ** k)


 def Mean(arr):
     return Moment(arr, 1)


 def Diviation(arr):
     return Moment(arr, 2) - Moment(arr, 1) ** 2


 def Plotter(arr):
     plt.plot(arr)
     plt.show()


 def Test(x, answer, error=0.1):
     if abs(x - answer) <= error:
         return "cовпадает в пределах погрешности " + str(error)
     return "не cовпадает в пределах погрешности " + str(error)


 if __name__ == '__main__':
     lambda = int(input())
     N = int(input())
     k = int(input())
     error = float(input())
     arr = Puasson(lambda, N)
     Plotter(arr)
     print("Начальный момент случайной великичны для k =",
           k, "равен", Moment(arr, k))
     print("Среднее значение равно", Mean(arr),
           Test(Mean(arr), lambda), "с реальным значением", lambda)
     print("Дисперсия случайной величины равна", Diviation(Puasson(lambda, N)),
           "она", Test(Diviation(arr), lambda), "с реальным значением", lambda)
