#!/usr/bin/python3
"""
    0-read_file
    Reads a text file (UTF8) and prints it to stdout
"""


def pascal_triangle(n):
    """Reads a text file (UTF8) and prints it to stdout"""
    if n <= 0:
        return []
    trian = []

    if n >= 1:
        row = []
        row.append(1)
        trian.append(row)

    if n > 1:
        for i in range(2, n + 1):
            row = []
            for j in range(i):
                if j == 0:
                    row.append(1)
                elif j == i - 1:
                    row.append(1)
                else:
                    row.append(trian[i - 2][j - 1] + trian[i - 2][j])
            trian.append(row)
    return trian
