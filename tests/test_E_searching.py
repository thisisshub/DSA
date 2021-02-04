import sys

sys.path.append("../")

from E_searching.iterative import A_binary_search_iterative
from E_searching.recursive import A_binary_search_recursive

class Test_E_searching:
    def test_A_binary_search_iterative(self):
        n = 9
        l = [i for i in range(10)]
        assert A_binary_search_iterative.method1_iterative(n, l) == 9

    def test_B_binary_search_recursive(self):
        n = 9
        l = [i for i in range(10)]
        assert A_binary_search_recursive.method1_recursive(l, 0, len(l) - 1, n) == 9
