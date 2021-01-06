import sys
sys.path.append('../')

from B_bit_magic import (
    A_operation_and,
    B_operation_or,
    C_operation_xor,
    D_operation_complement,
    E_operation_leftshit_rightshift,
    F_count_setbit,
    G_brian_kerningham,
    H_using_lookuptable
)

class Test_B_palindrome:

    def test_A_operation_and(self):
        assert A_operation_and.method1(25, 30) == '0b11000'
        assert A_operation_and.method1(25, 30) != '0b10000'
        assert A_operation_and.method1(-25, -30) == '-0b11110'
    

    def test_B_operation_or(self):
        assert B_operation_or.method1(60, 13) == '0b111101'
        assert B_operation_or.method1(60, 13) != '0b110001'
        assert B_operation_or.method1(-10, -12) == '-0b1010'