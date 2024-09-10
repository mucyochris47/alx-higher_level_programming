#!/usr/bin/python3

f = 0
k = 0

while f < 10:
    k = 0
    while k < 10:
        if (f != k and f < k):
            print("{0:d}{1:d}".format(f, k), end="")
            if (f >= 8 and k >= 9):
                print()
            else:
                print(end=", ")
        k += 1
    f += 1

