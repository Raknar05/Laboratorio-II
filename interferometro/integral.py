#!/usr/bin/python

from generator import generate_range, rand_range
from math import sqrt

def integral_HOM (func, xMin, xMax, yMax, N_evt) :

    x_coord = generate_range (xMin, xMax, N_evt)
    y_coord = generate_range (0., yMax, N_evt)

    points_under = 0
    for x, y in zip (x_coord, y_coord):
        if (func (x) > y) : points_under = points_under + 1 

    A_rett = (xMax - xMin) * yMax
    frac = float (points_under) / float (N_evt)
    integral = A_rett * frac
    integral_unc = A_rett**2 * frac * (1 - frac) / N_evt
    return integral, integral_unc


# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 


def integral_CrudeMC (g, xMin, xMax, N_rand) :
    somma     = 0.
    sommaQ    = 0.    
    for i in range (N_rand) :
       x = rand_range (xMin, xMax)
       somma += g(x)
       sommaQ += g(x) * g(x)     
     
    media = somma / float (N_rand)
    varianza = sommaQ /float (N_rand) - media * media 
    varianza = varianza * (N_rand - 1) / N_rand
    lunghezza = (xMax - xMin)
    return media * lunghezza, sqrt (varianza / float (N_rand)) * lunghezza


# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----


def MC_classic (N_points) :                                          # dall'esame del 16 settembre
    sotto = float (0)
    for i in range (N_points):
        x = rand_range (0., 1.)
        y = rand_range (0., 2.)
        if (y < 2 * x * x) : sotto += 1
    frazione = sotto / N_points
    integrale = 2 * frazione
    sigma = 2 * np.sqrt (frazione * (1 - frazione) / N_points)
    return integrale, sigma                             
