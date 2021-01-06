import sys
sys.path.append('../')

from D_arrays import (
    A_fixed_size_array
)


class Test_D_arrays:

    def test_A_fixed_array(self):
        n = [None] * 5
        assert len(A_fixed_size_array.method1(n)) == 5