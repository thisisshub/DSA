import pytest
from A_mathematics import (
    A_count_digits,
    B_palindrome,
    C_gcd,
    D_lcm,
    E_factorial,
    F_prime_number,
    G_prime_factors,
    H_sieve_of_erathosthenes
)
 
class Test_A_mathematics:

    def test_A_count_digits(self):
        assert A_count_digits.method1(-1234) == 4
        assert A_count_digits.method1(0) == 1
        assert A_count_digits.method1(1234) == 4
        assert A_count_digits.method2(-1234) == 4
        assert A_count_digits.method2(0) == 1
        assert A_count_digits.method2(1234) == 4


    def test_B_palindrome(self):
        assert B_palindrome.method1('aibohphobia') == True
        assert B_palindrome.method1('string') == False


    def test_C_gcd(self):
        assert C_gcd.method1(-123, -32) == 1
        assert C_gcd.method1(12, 18) == 6
        assert C_gcd.method1(-4, 14) == 2
        assert C_gcd.method2(-123, -32) == 1
        assert C_gcd.method2(12, 18) == 6
        assert C_gcd.method2(-4, 14) == 2