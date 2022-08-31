from fractions import Fraction
from decimal import Decimal
import numpy as np

repetitions = 100
d = 2
r = 0
for n in range(repetitions):
    r += Fraction(1, (-d) ** n)
for n in range(2, repetitions + 2):
    r += Fraction(1, (-d) ** (n - 2))
print(Decimal(r.numerator) / Decimal(r.denominator))
print(r < np.inf)
