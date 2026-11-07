import math

"""
Soal: dy/dx = (4x^3 - 2x + 1)/(2 + y),  y(0) = 1,  cari y(2) = ...?
Diubah dulu ke bentuk dy/dx = f(x,y):
    f(x,y) = (4x^3 - 2x + 1) / (2 + y)
"""


def f(x, y):
    return (4 * x**3 - 2 * x + 1) / (2 + y)


def solusi_eksak(x):
    # (2+y)dy = (4x^3-2x+1)dx -> y^2/2 + 2y = x^4 - x^2 + x + 5/2
    # y = -2 + sqrt(4 + 2(x^4 - x^2 + x) + 5)
    return -2 + math.sqrt(9 + 2 * (x**4 - x**2 + x))


def metode_rk4(f, x_awal, y_awal, x_target, N):
    h = (x_target - x_awal) / N
    x, y = x_awal, y_awal
    tabel = []

    for i in range(N):
        k1 = f(x, y)
        k2 = f(x + h / 2, y + k1 * h / 2)
        k3 = f(x + h / 2, y + k2 * h / 2)
        k4 = f(x + h, y + k3 * h)
        y_next = y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        tabel.append((i, x, y, k1, k2, k3, k4, y_next))
        x = x + h
        y = y_next

    return tabel, y  # y terakhir = hasil pendekatan y(x_target)


def cetak_tabel(tabel):
    print(f"{'i':3}{'xi':9}{'yi':10}{'k1':9}{'k2':9}{'k3':9}{'k4':9}{'yi+1':10}")
    print("." * 68)
    for i, xi, yi, k1, k2, k3, k4, y_next in tabel:
        print(
            f"{i:<3}{xi:<9.4f}{yi:<10.4f}{k1:<9.4f}{k2:<9.4f}{k3:<9.4f}{k4:<9.4f}{y_next:<10.4f}"
        )


if __name__ == "__main__":
    x_awal, y_awal = 0.0, 1.0
    x_target = 2.0
    N = 15

    tabel, y_rk4 = metode_rk4(f, x_awal, y_awal, x_target, N)

    print("     Tabel Iterasi Metode Runge-Kutta Orde-4  \n")
    cetak_tabel(tabel)

    y_eksak = solusi_eksak(x_target)
    galat_absolut = abs(y_eksak - y_rk4)
    galat_relatif = galat_absolut / y_eksak * 100

    print("\n       Perbandingan Solusi Eksak")
    print(f"Solusi eksak y({x_target:.0f}) = -2 + sqrt(37) = {y_eksak:.6f}")
    print(f"Metode RK4   y({x_target:.0f})            = {y_rk4:.6f}")
    print(f"Galat absolut                      = {galat_absolut:.6f}")
    print(f"Galat relatif                      = {galat_relatif:.6f}%")
