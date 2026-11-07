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


def metode_euler(f, x_awal, y_awal, x_target, N):
    h = (x_target - x_awal) / N
    x, y = x_awal, y_awal
    tabel = []

    for i in range(N):
        fi = f(x, y)
        y_next = y + h * fi
        tabel.append((i, x, y, fi, y_next))
        x = x + h
        y = y_next

    return tabel, y  # y terakhir = hasil pendekatan y(x_target)


def cetak_tabel(tabel):
    print(f"{'i':3}{'xi':10}{'yi':12}{'f(xi,yi)':14}{'yi+1':12}")
    print("." * 51)
    for i, xi, yi, fi, y_next in tabel:
        print(f"{i:<3}{xi:<10.4f}{yi:<12.4f}{fi:<14.4f}{y_next:<12.4f}")


if __name__ == "__main__":
    x_awal, y_awal = 0.0, 1.0
    x_target = 2.0
    N = 15

    tabel, y_euler = metode_euler(f, x_awal, y_awal, x_target, N)

    print("     Tabel Iterasi Metode Euler  \n")
    cetak_tabel(tabel)

    y_eksak = solusi_eksak(x_target)
    galat_absolut = abs(y_eksak - y_euler)
    galat_relatif = galat_absolut / y_eksak * 100

    print("\n       Perbandingan Solusi Eksak")
    print(f"Solusi eksak y({x_target:.0f}) = -2 + sqrt(37) = {y_eksak:.6f}")
    print(f"Metode euler y({x_target:.0f})            = {y_euler:.6f}")
    print(f"Galat absolut                      = {galat_absolut:.6f}")
    print(f"Galat relatif                      = {galat_relatif:.6f}%")
