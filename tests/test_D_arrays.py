import sys

sys.path.append("../")

from D_arrays import A_fixed_size_array, B_dynamic_size_array


class Test_D_arrays:
    def test_A_fixed_array(self):
        n = [None] * 5
        assert len(A_fixed_size_array.method1(n)) == 5

    def test_B_dynamic_array(self):
        n = []
        assert len(B_dynamic_size_array.method1(n)) == 0
        n = [1, 2, 3, 4, 5, 6]
        assert len(B_dynamic_size_array.method1(n)) == 6
