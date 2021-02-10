import sys

sys.path.append("../")

from D_arrays.types_of_arrays import A_fixed_size_array, B_dynamic_size_array
from D_arrays.operation_on_arrays import A_searching


class Test_D_arrays:
    def test_A_fixed_array(self):
        assert len(A_fixed_size_array.method1()) == 5

    def test_B_dynamic_array(self):
        n = []
        assert len(B_dynamic_size_array.method1(n)) == 0
        n = [1, 2, 3, 4, 5, 6]
        assert len(B_dynamic_size_array.method1(n)) == 6

    def test_A_searching(self):
        n = 9
        l = [i for i in range(10)]
        assert A_searching.method1(l, 0, len(l) - 1, n) == 9
        assert A_searching.method2(n, l) == True
        assert A_searching.method3(n, l) == True
