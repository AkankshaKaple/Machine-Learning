"""
Write a Python program to get the powers of an array values element-wise.

Note: First array elements raised to powers from second array
Expected Output:
Original array
[0 1 2 3 4 5 6]
First array elements raised to powers from second array, element-wise:
[ 0 1 8 27 64 125 216]
"""

import pandas as pd

data = ({'elements': i*i*i} for i in range(7))
data = pd.DataFrame(data)

print(data)

