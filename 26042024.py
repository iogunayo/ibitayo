# from math import sqrt
#
#
# def quadratic_eq(a, b, c):
#     x = (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
#     print(round(x, 2))
#     return x
#
#
# quadratic_eq(3, 4, -5)


def decrypt(s):
    return ''.join(chr(ord(c) - 10) for c in s)


x = decrypt('S}kkm*Xo\x81~yx')
print(x)