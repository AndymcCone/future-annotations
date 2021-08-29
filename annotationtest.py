from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Complex:
    real: float
    imag: float

    def __add__(self, other: Complex) -> Complex:
        return Complex(self.real + other.real, self.imag + other.imag)

x = Complex(1, 2)
y = complex(2, 4)

c = x + y

print(c)

