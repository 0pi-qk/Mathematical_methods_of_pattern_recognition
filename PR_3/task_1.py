import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import statsmodels.api as sm

mpl.use("TkAgg")  # Используем бэкенд для Windows 


class Noise:
    @staticmethod
    def make_noise(y, p: float, law="uniform"):
        """
        p - уровень шума, от 0 до 1
        """
        eps = abs(y * p)
        if law == "uniform":
            return np.random.uniform(y - eps, y + eps)
        elif law == "normal":
            return np.random.normal(y, eps / 3)


def f1(x, *args) -> float:
    return 5 * np.sin(x) + 20 * np.sin(x / 10)


def f2(x, *args) -> float:
    return x + 5 * np.sin(x)


def f3(x, *args) -> float:
    return 0.005 * x ** 2


def tls(x, y):
    if x.ndim == 1:
        n = 1  # число переменных в x
        x = x.reshape(len(x), 1)
    else:
        n = np.array(x).shape[1]

    Z = np.vstack((x.T, y)).T
    U, s, Vt = la.svd(Z, full_matrices=True)

    V = Vt.T
    Vxy = V[:n, n:]
    Vyy = V[n:, n:]
    a_tls = - Vxy / Vyy  # решение методом общих наименьших квадратов

    xtyt = - Z.dot(V[:, n:]).dot(V[:, n:].T)
    xt = xtyt[:, :n]  # ошибка x
    y_tls = (x + xt).dot(a_tls)
    fro_norm = la.norm(xtyt, 'fro')

    return y_tls, x + xt, a_tls, fro_norm


if __name__ == '__main__':
    func = f3  # Выбор функции для генерации данных (f1, f2 or f3)

    p = 0.15  # Процент шума, который будет добавлен к данным (от 0 до 1)
    N = 30  # Количество точек данных
    x_min, x_max = 25, 60  # Минимальное и максимальное значение для генерации данных

    # Создание массива значений X от x_min до x_max с N точками и вычисление соответствующих значений y с помощью выбранной функции
    X = np.linspace(x_min, x_max, N)
    y = func(X)  # Вычисление значений y на основе выбранной функции
    print(X)
    print(y)

    # Добавление шума к данным
    x_noised = Noise.make_noise(X, p)  # Добавление шума к массиву X
    y_noised = Noise.make_noise(y, p)  # Добавление шума к массиву y

    print(x_noised)
    print(y_noised)

    # OLS (Метод наименьших квадратов)
    fit_ols = sm.OLS(y_noised, sm.add_constant(X)).fit()  # Подгонка модели методом OLS

    print(fit_ols.summary())  # Вывод сводной статистики о модели
    print("Параметры: ", fit_ols.params)  # Вывод параметров модели
    print("Стандартные ошибки: ", fit_ols.bse)  # Вывод стандартных ошибок параметров
    print("R2: ", fit_ols.rsquared)  # Вывод коэффициента детерминации

    # WLS (Метод взвешенных наименьших квадратов)
    weights = np.ones(N)
    weights[N * 6 // 10:] = 3
    weights = 1.0 / (weights ** 2)
    fit_wls = sm.WLS(y, X, weights=weights).fit()  # Подгонка модели методом WLS

    print(fit_wls.summary())  # Вывод сводной статистики о модели
    print("Параметры: ", fit_wls.params)  # Вывод параметров модели
    print("Стандартные ошибки: ", fit_wls.bse)  # Вывод стандартных ошибок параметров
    print("R2: ", fit_wls.rsquared)  # Вывод коэффициента детерминации

    # TLS (Метод общих наименьших квадратов)
    y_tls, x_tls, a_tls, from_norm = tls(x_noised, y_noised)  # Подгонка модели методом TLS

    # Подготовка данных для построения графика
    y_ols = fit_ols.fittedvalues  # Предсказанные значения модели OLS
    y_wls = fit_wls.fittedvalues  # Предсказанные значения модели WLS

    # Статистика об ошибке
    print("==============НОРМА ОШИБКИ==============")
    print("--------------------------------------")
    print(f'       err_noised: {round(np.linalg.norm(y - y_noised), 5)}')  # Норма ошибки для данных с шумом
    print(f'       err_ols: {round(np.linalg.norm(y - y_ols), 5)}')  # Норма ошибки для модели OLS
    print(f'       err_wls: {round(np.linalg.norm(y - y_wls), 5)}')  # Норма ошибки для модели WLS
    print(f'       err_tls: {round(np.linalg.norm(y - y_tls), 5)}')  # Норма ошибки для модели TLS
    print(f'       err_ols_noised: {round(np.linalg.norm(y_noised - y_ols), 5)}')  # Норма ошибки для модели OLS с шумом
    print(f'       err_wls_noised: {round(np.linalg.norm(y_noised - y_wls), 5)}')  # Норма ошибки для модели WLS с шумом
    print(f'       err_tls_noised: {round(np.linalg.norm(y_noised - y_tls), 5)}')  # Норма ошибки для модели TLS с шумом
    print("--------------------------------------")

    # Построение графика
    plt.plot(X, y, "-", label="оригинал")  # Оригинальные данные
    plt.plot(X, fit_ols.fittedvalues, "--", label="OLS")  # Предсказанные значения модели OLS
    plt.plot(X, fit_wls.fittedvalues, "--", label="WLS")  # Предсказанные значения модели WLS
    plt.plot(x_tls, y_tls, "--", label="TLS")  # Предсказанные значения модели TLS
    plt.plot(X, y_noised, "o", label="с шумом(y)", markersize=3)  # Данные с шумом
    plt.plot(x_noised, y_noised, "o", label="с шумом(x,y)", markersize=3)  # Данные с шумом
    plt.legend()  # Добавление легенды
    plt.show()  # Показать график
