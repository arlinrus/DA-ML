# Практическая работа номер 1
Используем библиотеки:

**numpy** - для работы с большими массивами данных

**scipy.stats** - для работы со статистически данными 

**scipy.optimaze** - для работы с оптимизацией функцией

**matplotlib** - для визуалмщации данных(построение графиков)

__________
Создадим функцию, которая проверяет данные на нормальность распределения значений списка, используя тест Шапир-Уилка.
Значение равно [True, True], что означет, что для для двух массивов данных нулевая гипотеза о нормальности распределения не отвергается на уровне значимости 0,05 .
Уровень доверия 95%
```
def Normality_checker(List_of_values, alpha = 0.05):
    n = len(List_of_values)
    Check_vector = []
    for i in range(n):
        if 1 - scst.shapiro(List_of_values[i]).statistic < alpha:
            Check_vector.append(True)
        else:
            Check_vector.append(False)
    return Check_vector
```
___________

Функция Mean_square_func вычислчет средне квадратиное отклонение между двумя массивами значений.

```
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
```
__________________
Вычисляет линейную регрессию для массива X_value с параметром Parse
```
def Linear_regression_one_demetion(X_values, Pars):
    N = len(X_values)
    if len(Pars) == 2 :
        return np.ones(N)*Pars[0]+ Pars[1]*X_values
    else:
        raise("* With 'Pars' troubles! *")
```
________________________
Target_func - целевая функция для оптимизации методом НМК
```
Current function value: 0.2263291801780936 - мера ошибки модели
         
        
```
Target_func = lambda Pars: Mean_square_func(Linear_regression_one_demetion(val_1, Pars), val_2) #summ

Pars_init = [0,1]

res = scop.minimize(Target_func, Pars_init, method='SLSQP', options={'eps':1e-2, 'ftol':1e-5, 'disp': True, 'maxiter':90})

val_2_fitted = Linear_regression_one_demetion(val_1, res.x)
```
________________________

```
def Determination(Y_vector_exp, Y_vector_fit):
    Meanarf_np = lambda Y: np.sum(Y)/len(Y)
    Variance_np = lambda Y, y_mean: np.sum(np.power( Y - np.ones(len(Y))*y_mean , 2))
    y_mean_exp = Meanarf_np(Y_vector_exp)
    return Variance_np(Y_vector_fit, y_mean_exp)/Variance_np(Y_vector_exp, y_mean_exp)


```


```



