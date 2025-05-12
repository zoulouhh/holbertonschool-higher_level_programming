#!/usr/bin/python3
str = "python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax"
str2 = str[39:67] + str[0:6] + str[107:112]
print(str2)
# The code above is a Python script that creates a string variable `str` containing a description of the Python programming language.
# It then creates a new string `str2` by concatenating specific slices of `str`:
# - `str[39:67]` extracts the substring "programming language"
# - `str[0:6]` extracts the substring "python"
# - `str[107:112]` extracts the substring "power" 