from iminuit import Minuit
from iminuit.cost import LeastSquares
import numpy as np

def fit (list_1, list_2, dev_list, f):
    
    least_squares = LeastSquares(list_1, list_2, dev_list, f)
    my_minuit = Minuit(least_squares, A = 0, B = 0)
    my_minuit.migrad() 
    my_minuit.hesse()
    
    display(my_minuit)
    
    # il fit è valido
    is_valid = my_minuit.valid
    print ('success of the fit: ', is_valid)
    print ('\n')

    # dammi il valore del ki-quadro ed i gradi di libertà
    Q_squared = my_minuit.fval
    print ('Valore del fit ki-quadro: ', Q_squared)
    print('\n')
    N_dof = my_minuit.ndof
    print ('Valore del numero di gradi di libertà: ', N_dof)
    print('\n')

    # dammi il valore del ki-quadro ridotto
    Q_squared_reduced = my_minuit.fval / my_minuit.ndof
    print ('Valore del fit ki-quadro ridotto: ', Q_squared_reduced)
    print('\n')

    # dammi il p-value associato al fit
    from scipy.stats import chi2
    print ('associated p-value: ', 1. - chi2.cdf (my_minuit.fval, df = my_minuit.ndof))
    print('\n')

    # dammi i valori dei parametri di fit con le rispettive incertezze
    print ('Valori dei parametri di fit con le rispettive incertezze: ')
    for par, val, err in zip (my_minuit.parameters, my_minuit.values, my_minuit.errors) :
        print(f'{par} = {val:.5f} +/- {err:.5f}')
    A_fit = my_minuit.values[0]
    B_fit = my_minuit.values[1]
    A_err = my_minuit.errors[0]
    B_err = my_minuit.errors[1]
    print('\n')  

    # dammi la matrice di covarianza
    print (my_minuit.covariance)
    cov_AB = my_minuit.covariance[0][1]
    print('\n')
    print ('covarianza tra A e B: ', cov_AB)

    return A_fit, B_fit, A_err, B_err, cov_AB

def calc_mean_dev (list_1):
    mean = np.mean(list_1)
    dev = np.std(list_1)
    return mean, dev