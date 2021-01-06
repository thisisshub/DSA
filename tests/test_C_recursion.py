import sys
sys.path.append('../')

from C_recursion import (
    A_factorial,
    B_fibonnaci,
    C_print_n_to_1,
    D_print_1_to_n,
    E_tail_recursion,
    F_checking_palindrome,
    G_sum_of_digits,
    H_rod_cutting,
    I_subset_of_set,
    J_tower_of_hanoi,
)


class Test_C_recursion:

    def test_A_factorial(self):
        assert A_factorial.method1(0) == 1
        assert A_factorial.method1(1) == 1
        assert A_factorial.method1(2) == 2
        assert A_factorial.method1(4) != 23
        assert A_factorial.method1(10) == 3628800

    
    def test_B_fibonnaci(self):
        assert B_fibonnaci.method1(0) == 0
        assert B_fibonnaci.method1(1) == 1
        assert B_fibonnaci.method1(2) == 1
        assert B_fibonnaci.method1(3) == 2
        assert B_fibonnaci.method1(4) == 3
        assert B_fibonnaci.method2(0) == 0
        assert B_fibonnaci.method2(1) == 1
        assert B_fibonnaci.method2(2) == 1
        assert B_fibonnaci.method2(3) == 2
        assert B_fibonnaci.method2(4) == 3


    def test_C_print_n_to_1(self):
        assert C_print_n_to_1.method1(10) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        assert C_print_n_to_1.method2(10) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


    def test_D_print_1_to_n(self):
        assert D_print_1_to_n.method1(10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


    def test_E_tail_recursion(self):
        assert E_tail_recursion.tailrecursive(10) == 3628800
        assert E_tail_recursion.nontailrecursive(10) == 3628800

    
    def test_F_checking_palindrome(self):
        assert F_checking_palindrome.method1('aibohphobia') == True
        assert F_checking_palindrome.method1('string') == False
        assert F_checking_palindrome.method1(1111) == True
        assert F_checking_palindrome.method1(1234) == False


    def test_G_sum_of_digits(self):
        assert G_sum_of_digits.method1(1234) == 10
        assert G_sum_of_digits.method2(1234) == 10
        assert G_sum_of_digits.method3(1234) == 10


    def test_H_rod_cutting(self):
        price = [1, 5, 8, 9, 10, 17, 17, 20]
        assert H_rod_cutting.method1(price, len(price)) == 22


    def test_I_subset_of_set(self):
        assert I_subset_of_set.method1([1, 2, 3]) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        assert I_subset_of_set.method2([{1, 2, 3}]) == [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]