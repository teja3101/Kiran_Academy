# module1 contains its own print statements, and when you import a module, Python executes the entire file once.
# Python runs all lines in module1.py, including its print statements.

# import module1
# print(module1.price)

# import keyword
# print(keyword.kwlist)

# from module1 import price, tax_rate
# print("imported Price Rate: ", price)
# print("imported Tax Rate: ", tax_rate)

from module1 import *
print("imported Price Rate: ", price)
print("imported Tax Rate: ", tax_rate)

addTwo(10,20)

import this