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
    base = 2
    power = 3
    print("x+y is", add(x,y))
    print("x*y is", multiply(x,y))
    print("x/y is", divide(x,y))
    print("x*y is", multiply_by_add(x,y))
    print("x*y is", divide_by_subtract(x,y))
    print("x*y is", exponent(base, power))
    # print("x*y is", module(x, y))



if __name__ == "__main__":
    main()
    unittest.main()


# in main do not forget to add everythin from the tset and the files themselves