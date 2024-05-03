import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scst
import scipy.optimize as scop

data = 'Linear_regration_one_demetion_xy_format_100 (1).csv'

val_1 = np.array([], dtype=float)
val_2 = np.array([], dtype=float)

def Normality_checker(List_of_values, alpha = 0.05):
    n = len(List_of_values)
    Check_vector = []
    for i in range(n):
        if 1 - scst.shapiro(List_of_values[i]).statistic < alpha:
            Check_vector.append(True)
        else:
            Check_vector.append(False)
    return Check_vector # Information about values normality

def Mean_square_func(V_variavle, V_fixed):
    N = len(V_variavle) if len(V_variavle) == len(V_fixed) else 0
    try:
        S_square = np.sum(np.power(np.abs(V_variavle- V_fixed),2)) / (N-1)
    except ZeroDivisionError:
        if N == "0":
            raise("Mean_square_func - must have arg with equal lens!")
        else:
            raise("Mean_square_func - arg must be great then 1!")
    else:
        return S_square

with open(data, 'r') as INPUT:
    for String in INPUT:
        String_split = String.strip().split(',')
        try:
            String_split = [float(i) for i in String_split]
        except ValueError:
            continue
        else:
            val_1 = np.append(val_1, String_split[0])
            val_2 = np.append(val_2, String_split[1])


print(Normality_checker([val_1, val_2]))

def Linear_regression_one_demetion(X_values, Pars):
    N = len(X_values)
    if len(Pars) == 2 :
        return np.ones(N)*Pars[0]+ Pars[1]*X_values
    else:
        raise("* With 'Pars' troubles! *")

Target_func = lambda Pars: Mean_square_func(Linear_regression_one_demetion(val_1, Pars), val_2) #summ

Pars_init = [0,1]

res = scop.minimize(Target_func, Pars_init, method='SLSQP', options={'eps':1e-2, 'ftol':1e-5, 'disp': True, 'maxiter':90})

val_2_fitted = Linear_regression_one_demetion(val_1, res.x)

def Determination(Y_vector_exp, Y_vector_fit):
    Meanarf_np = lambda Y: np.sum(Y)/len(Y)
    Variance_np = lambda Y, y_mean: np.sum(np.power( Y - np.ones(len(Y))*y_mean , 2))
    y_mean_exp = Meanarf_np(Y_vector_exp)
    return Variance_np(Y_vector_fit, y_mean_exp)/Variance_np(Y_vector_exp, y_mean_exp)

print("Determination: ", Determination(val_1, val_2))

def Mean_error_of_approximation(Y_vector_exp, Y_vector_fit):
    n = len(Y_vector_exp)
    if n == len(Y_vector_fit):
        return np.sum(np.fabs( Y_vector_fit - Y_vector_exp)/( Y_vector_fit - Y_vector_exp))/n
    else:
        raise("* Mean_error_of_approximation(a1, a2) must have len a1 = len a2 *")

print("Средняя ошибка аппроксимации:" ,Mean_error_of_approximation(val_2,val_2_fitted))

# Tail checker
plt.plot(val_1, val_2_fitted, "--", val_1, val_2, "o")
plt.show()
plt.plot(val_1, val_2_fitted - val_2, "*")
plt.show()















