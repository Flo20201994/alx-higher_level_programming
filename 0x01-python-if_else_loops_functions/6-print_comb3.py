#!/usr/bin/python3
for k in range(9):
    for f in range(k + 1, 10):
        if k * 10 + f < 89:
            print("{:d}{:d}".format(k, f), end=", ")
print("{:d}".format(89))

