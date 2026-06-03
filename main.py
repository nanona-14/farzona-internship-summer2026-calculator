import unittest

from add import *

# By Farzona:
from multiply import *
from test_multiply import *
from multiply_by_add import *
from test_multiply_by_add import *
from divide import *
from test_divide import *

# By Elbek:
from subtract import *
from TestSubtract import *
from modulo import *
from testmodulo import *
from divide_by_subtract import *
from Testdbs import *

# By Javohir:
from exponent import *
from test_exponent import *

def main():
    x = 1
    y = 1
    print("x+y is", add(x,y))

if __name__ == "__main__":
    main()
    print("\n--- Running Unit Tests ---")
    unittest.main()
