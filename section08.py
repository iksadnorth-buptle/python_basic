# Sction08

from pkg.fibonacci import Fibonacci

fibonacci = Fibonacci()
print("ex2 : ", Fibonacci.fib2(400))
print("ex2 : ", fibonacci.title)

from pkg.fibonacci import *
Fibonacci.fib(300)

from pkg.fibonacci import Fibonacci as fi

import pkg.calculations as c
c.add(1,2)

from pkg.calculations import div as d
print("ex5 : ", int(d(100,10)))

import pkg.prints as p
import builtins
