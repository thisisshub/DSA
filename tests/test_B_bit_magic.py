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

    
    def test_C_operation_xor(self):
        assert C_operation_xor.method1(10, 12) == '0b110'
        assert C_operation_xor.method1(25, 30) != '0b110'
        assert C_operation_xor.method1(-25, -30) == '0b101'

    
    def test_D_operation_complement(self):
        assert D_operation_complement.method1(60) == '-0b111101'
        assert D_operation_complement.method1(61) != '-0b111100'
        assert D_operation_complement.method1(-20) == '0b10011'


    def test_E_operation_leftshit_rightshift(self):
        assert E_operation_leftshit_rightshift.method_leftshift(60) == '0b11110000'
        assert E_operation_leftshit_rightshift.method_rightshift(60) == '0b1111'

    
    def test_F_count_setbit(self):
        assert F_count_setbit.method1(0) == 0
        assert F_count_setbit.method1(1) == 1
        assert F_count_setbit.method1(10) == 2
        assert F_count_setbit.method2(0) == 0
        assert F_count_setbit.method2(1) == 1
        assert F_count_setbit.method2(10) == 2


    def test_G_brian_kerningham(self):
        assert G_brian_kerningham.method1(0) == 0
        assert G_brian_kerningham.method1(1) == 1
        assert G_brian_kerningham.method1(10) == 2