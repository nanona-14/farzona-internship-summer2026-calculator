import unittest
from add import *
from subtract import *
from test_subtract import *

def main():
    x = 2
    y = 1
    print("x+y is", add(x,y))
    print("x-y is", subtract(x,y))

if __name__ == "__main__":
    main()
    unittest.main()
