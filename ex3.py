import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

def distribution(lmbd, N):
  if lmbd < 0 or N < 0:
    raise ValueError
  n = np.arange(0, N + 1)
  return (n, np.float_power(lmbd, n) * np.exp(-lmbd) / factorial(n))

def moment(dist, k):
  if not isinstance(k, int) or not isinstance(dist[0], np.ndarray) or not isinstance(dist[1], np.ndarray):
    raise ValueError
  return np.sum(dist[0]**k * dist[1])

def average(dist):
  return moment(dist, 1)

def dispersion(dist):
  return average([(dist[0] - average(dist))**2, dist[1]])

if __name__ == '__main__':
  p = distribution(5, 150)
  print('Initial moment with k = 5 :', moment(p, 5))
  print('Average value :', average(p))
  print('Dispersion :', dispersion(p))
  print('lambda :', 5)
  plt.plot(p[0], p[1])
  plt.show()