#!/usr/bin/python3

for f in range(0, 10):
    for k in range(f + 1, 10):
        print(f"{f:02}{k:02}", end=", " if not (f == 8 and k == 9) else "\n")

