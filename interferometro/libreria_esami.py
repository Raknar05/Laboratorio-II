import random
import math
import numpy as np

# esame della likelihood del 24 giugno
def rand_range (xMin, xMax) :
    return xMin + random.random () * (xMax - xMin)


def try_and_catch_exp (lamb, N):
    events = []
    x_max = 3/lamb
    for i in range (N):
      x = rand_range (0., x_max)
      y = rand_range (0., lamb)
      while (y > lamb * math.exp (-lamb * x)):
        x = rand_range (0., x_max)
        y = rand_range (0., lamb)
      events.append (x)
    return events
    
def try_and_catch_gau (mean, sigma, N):
    events = []
    for i in range (N):
      x = rand_range (mean - 3 * sigma, mean + 3 * sigma)
      y = rand_range (0., 1.)
      while (y > math.exp (-0.5 * ( (x - mean)/sigma)**2)):
        x = rand_range (mean - 3 * sigma, mean + 3 * sigma)
        y = rand_range (0, 1.)
      events.append (x)
    return events
    
# esame dei numeri in sequenza del 16 settembre 
class additive_recurrence :

    def __init__ (self, alpha = 0.618034) : # (sqrt(5)-1)/2
        self.alpha = alpha
        self.s_0 = 0.5
        self.s_n = 0.5
        
    def get_number (self) :
        self.s_n = (self.s_n + self.alpha) % 1
        return self.s_n

    def set_seed (self, seed) :
        self.s_0 = seed
        self.s_n = seed
   
    def get_numbers (self, N) :
        lista = []
        for i in range (N) : lista.append (self.get_number ())
        return lista

# esame del 13 gennaio punto 1 
def double_gauss(x, mu, sigma_sx, sigma_dx):

	A = 2 / (np.sqrt(2 * np.pi) * (sigma_sx + sigma_dx))
	if (x < mu) : return A * np.exp (-0.5 * ((x-mu)/sigma_sx)**2)
	return A * np.exp (-0.5 * ((x-mu)/sigma_dx)**2)

