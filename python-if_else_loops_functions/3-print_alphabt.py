#!/usr/bin/python3
for alphabet in range(97, 123):
    if alphabet != ord('q') and alphabet != ord('e'):
        print("{:c}".format(alphabet), end="")
